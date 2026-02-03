import re
from collections import counter
import nltk
from nltk.corpus import stopwords
posts=["I love this new phone battery life is amazing","This updates is very bad and disappointing","Amazing camera and great perfomance","The app is slow and the interface is bad","I love the camera quality and battery performance"]
nltk.download('stopwords')
stwords=set(stopwords.words('english'))
ug,bg,tg=[],[],[]
for post in posts:
    post =post.lower()
    post =re.sub(r'[^a-z\s]'",",post)
    words=[w for w in post.split() if w not in stwords]
    ug.extend(words)
    bg.extend(zip(words,words[1:]))
    tg.extend(zip(words,words[1:],words[2:]))
    ugc=Counter(ug)
    bgc=Counter(bg)
    tgc=Counter(tg)
    print("top Unigrams:",ugc.most_common(3))
    print("\ntop Bnigrams:",bgc.most_common(3))
    print("\ntop Trigrams:",tgc.most_common(3))
    from textblob import TextBlob
    print("\n Sentiment Analysis:")
    for post in posts:
        blob =TextBlob(post)
        polarity =blob.sentiment.polarity
        if polarity >0:
            print("postive")
        elif polarity <0:
                     print ("negative")
        else:
                    print("netural")
                    print(f"post:{post}'Polarity:polarity")
