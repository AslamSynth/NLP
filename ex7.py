from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

p1 = "the language learning platform helps users improve vocabulary."
p2 = "this system suggests synonyms to expand vocabulary"

vec = TfidfVectorizer().fit_transform([p1, p2])
score = cosine_similarity(vec[0], vec[1])[0][0]

if score >= 0.75:
    level = "High"
elif score >= 0.40:
    level = "Medium"
else:
    level = "Low"

print("Cosine Score:", score)
print("Similarity Level:", level)
