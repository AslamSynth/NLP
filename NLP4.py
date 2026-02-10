from collections import Counter
from nltk.util import ngrams
import nltk
text = """
speech recognition system help users type faster .
speech recognition model predict the next word .
speech recognition and predictive text are important .
"""
tokens = text.lower().split()
ug = Counter(tokens)
bg = Counter(ngrams(tokens, 2))
tg = Counter(ngrams(tokens, 3))
V = len(ug)
k = 1
input_words = ["speech", "recognition"]
next_words = set(tokens)
scores = {}
for word in next_words:
    if tg[(input_words[0], input_words[1], word)] > 0:
        prob = tg[(input_words[0], input_words[1], word)] / bg[(input_words[0], input_words[1])]
    elif bg[(input_words[1], word)] > 0:
        prob = (bg[(input_words[1], word)] + k) / (ug[input_words[1]] + k * V)
    else:
        prob = (ug[word] + k) / (sum(ug.values()) + k * V)

    scores[word] = prob
sorted_predictions = sorted(scores.items(), key=lambda x: x[1], reverse=True)
print("Next word predictions:")
for word, score in sorted_predictions[:5]:
    print(f"{word} → {score:.4f}")
