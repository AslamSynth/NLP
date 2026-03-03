
import spacy
base = spacy.load("en_core_web_sm")
text = """Wow! Yesterday, Dr. Arun Kumar, the chief scientist of India, announced that he will quickly launch three innovative AI-based projects in Chennai. Because they can significantly improve public safety. It may not only reduce accidents but also save lives. There were over 50 experts working on the project."""
doc = base(text)
for token in doc:
print(token.text, "->", token.pos_)

