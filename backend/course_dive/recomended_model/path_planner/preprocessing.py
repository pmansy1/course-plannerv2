import pandas as pd
import re
from collections import Counter

def extract_keywords(text, top_n=5):
    if not isinstance(text, str):
        return ""
    # Remove punctuation and split
    words = re.findall(r'\b\w{4,}\b', text.lower())  # skip short/common words
    common = Counter(words).most_common(top_n)
    return ", ".join(word for word, _ in common)

def extract_prerequisites(text):
    if not isinstance(text, str):
        return ""
    text = text.lower()
    match = re.search(r'(prerequisite[s]?:.*?\.|must complete.*?\.|required.*?\.)', text)
    return match.group(0).strip() if match else ""

def extract_credit_hours(title):
    if not isinstance(title, str):
        return 0
    match = re.search(r'\((\d+)[–-]?(\d+)?\s*credits?\)', title.lower())
    if match:
        return int(match.group(2)) if match.group(2) else int(match.group(1))
    return 0

def extract_level(description):
    if not description or not isinstance(description, str):
        return "Unknown"

    desc = description.lower()
    if any(term in desc for term in ['advanced', 'capstone', 'upper-level']):
        return "Advanced"
    elif any(term in desc for term in ['intermediate', '2000-level']):
        return "Intermediate"
    elif any(term in desc for term in ['introduction', 'intro', '1000-level']):
        return "Beginner"
    return "Unknown"

# Load and preprocess
df = pd.read_csv("/Users/joy/Downloads/course_planner/course-plannerv2/all_course_du.csv")
df.fillna('', inplace=True)

df['keywords'] = df['Description'].apply(extract_keywords)
df['prerequisites'] = df['Description'].apply(extract_prerequisites)
df['credit_hours'] = df['Course Title'].apply(extract_credit_hours)
df['level'] = df['Description'].apply(extract_level)

# Save for import into Django
df.to_csv("/Users/joy/Downloads/course_planner/course-plannerv2/preprocessed_courses.csv", index=False)
df[['Course Title', 'keywords', 'prerequisites', 'credit_hours', 'level']].head()
