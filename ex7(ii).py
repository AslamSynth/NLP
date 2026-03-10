from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.metrics.pairwise import cosine_similarity

p1 = "The language learning platform helps users improve vocabulary."

p2 = "This system suggests synonyms to expand vocabulary."

vec = TfidfVectorizer().fit_transform([p1, p2])

score = cosine_similarity(vec[0], vec[1])[0][0]

level = "High" if score>=0.75 else "Medium" if score>=0.40 else "Low"

print("Cosine Score:", score)

print("Similarity Level:", level)
