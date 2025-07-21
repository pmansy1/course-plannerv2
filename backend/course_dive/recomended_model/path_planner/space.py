import pandas as pd
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Your CSV file path
input_csv = "final_cleaned_courses_v1.csv"

def spacy_extract_phrases(text):
    """
    Extract meaningful phrases from text using spaCy:
    - noun chunks longer than 1 word (exclude pronouns)
    - single nouns, proper nouns, adjectives (lemmatized)
    Returns a string of joined phrases separated by spaces (for TF-IDF vectorizer).
    """
    doc = nlp(text.lower())
    noun_chunks = set(
        chunk.text.strip()
        for chunk in doc.noun_chunks
        if len(chunk.text.split()) > 1 and not any(tok.pos_ == "PRON" for tok in chunk)
    )
    single_words = set(
        token.lemma_
        for token in doc
        if token.pos_ in ("NOUN", "PROPN", "ADJ") and not token.is_stop and token.is_alpha
    )
    # Combine and join with spaces (TF-IDF needs string input)
    combined = noun_chunks.union(single_words)
    return " ".join(combined)

# Load your data
df = pd.read_csv(input_csv)

# Apply spaCy phrase extraction on course descriptions
df["SpaCy_Phrases"] = df["Description"].fillna("").apply(spacy_extract_phrases)

# Step 1: TF-IDF on spaCy-extracted phrases
vectorizer = TfidfVectorizer(max_df=0.9, min_df=2, stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df["SpaCy_Phrases"])
feature_names = vectorizer.get_feature_names_out()

def extract_top_keywords(tfidf_vec, row_idx, top_n=10):
    row = tfidf_vec[row_idx].tocoo()
    top_indices = row.col[row.data.argsort()[::-1][:top_n]]
    return ", ".join([feature_names[i] for i in top_indices])

df["TFIDF_Keywords"] = [extract_top_keywords(tfidf_matrix, i) for i in range(len(df))]

# Step 2: LDA topic modeling on the same TF-IDF matrix
lda = LatentDirichletAllocation(n_components=8, random_state=42)
lda_matrix = lda.fit_transform(tfidf_matrix)

def get_topic_keywords(model, feature_names, n_top_words=6):
    topics = []
    for topic_weights in model.components_:
        top_words = [feature_names[i] for i in topic_weights.argsort()[:-n_top_words - 1:-1]]
        topics.append(top_words)
    return topics

topic_keywords = get_topic_keywords(lda, feature_names)

# Assign dominant topic and keywords
df["Topic"] = lda_matrix.argmax(axis=1)
df["Topic_Keywords"] = df["Topic"].apply(lambda x: ", ".join(topic_keywords[x]))

# Combine TF-IDF keywords and topic keywords for final output
df["Final_Keywords"] = df.apply(
    lambda row: "; ".join(set(row["TFIDF_Keywords"].split(", ") + row["Topic_Keywords"].split(", "))),
    axis=1
)

# Save results back to CSV if needed
df.to_csv("final_cleaned_courses_v1.csv", index=False)