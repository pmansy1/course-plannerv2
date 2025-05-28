import pandas as pd
import re
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer


nlp = spacy.load("en_core_web_sm")

def extract_keywords(text, top_n=5):
    if not text or not isinstance(text, str):
        return ""
    vectorizer = TfidfVectorizer(stop_words='english', max_features=top_n)
    tfidf_matrix = vectorizer.fit_transform([text])
    return ", ".join(vectorizer.get_feature_names_out())

def extract_prerequisites(text):
    if not text or not isinstance(text, str):
        return ""
    doc = nlp(text.lower())
    for sent in doc.sents:
        if 'prerequisite' in sent.text or 'must complete' in sent.text or 'required' in sent.text:
            return sent.text.strip()
    return ""


def extract_credit_hours(title):
    match = re.search(r'\((\d+)[–-]?(\d+)?\s*Credits?\)', title)
    if match:
        if match.group(2):
            return int(match.group(2)) 
        return int(match.group(1))
    return 0

def extract_level(description):
    desc = description.lower()
    if any(term in desc for term in ['advanced', 'capstone', 'upper-level']):
        return "Advanced"
    elif any(term in desc for term in ['intermediate', '2000-level']):
        return "Intermediate"
    elif any(term in desc for term in ['introduction', 'intro', '1000-level']):
        return "Beginner"
    return "Unknown"



def load_courses(path):
    path = "all_courses.csv" if path == "all_courses.csv" else path
    df = pd.read_csv(path)
    df.fillna('', inplace=True)

    df['keywords'] = df['Description'].apply(extract_keywords)
    df['prerequisites'] = df['Description'].apply(extract_prerequisites)
    return df

