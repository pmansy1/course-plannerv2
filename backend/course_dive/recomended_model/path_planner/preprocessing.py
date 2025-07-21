# Final Complete Cleaning Solution Based on Analyzed Issues

import pandas as pd
import re
from collections import Counter

# --- Load Dataset ---
df = pd.read_csv('/Users/joy/Downloads/final_cleaned_courses.csv', dtype={'Course Code': str})

# --- Step 1: Clean Description (Spacing Fixes Only) ---
def fix_description_spacing(text):
    if not isinstance(text, str):
        return ''
    text = text.replace('\n', ' ').replace('\r', ' ').replace('\xa0', ' ')
    text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
    text = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1 \2', text)
    text = re.sub(r'([a-zA-Z])(\d)', r'\1 \2', text)
    text = re.sub(r'(\d)([a-zA-Z])', r'\1 \2', text)
    text = re.sub(r'\s{2,}', ' ', text)
    return text.strip().capitalize()

df['Description'] = df['Description'].apply(fix_description_spacing)

# --- Step 2: Extract Prerequisites ---
def extract_course_codes(text):
    if not isinstance(text, str):
        return ''
    codes = re.findall(r'\b[A-Z]{2,4}\s*\d{3,4}\b', text)
    codes = [re.sub(r'\s+', '', c) for c in codes]
    return ', '.join(sorted(set(codes)))

def normalize_prerequisites(row):
    combined = f"{row.get('Description', '')} {row.get('Prerequisites', '')} {row.get('Preq_Notes', '')}"
    return extract_course_codes(combined)

df['Prerequisites'] = df.apply(normalize_prerequisites, axis=1)

# --- Step 3: Clean Preq_Notes (Restrictions Only) ---
restriction_phrases = [
    'sophomore standing', 'junior standing', 'senior standing',
    'business minors only', 'admission to daniels college of business',
    'microsoft excel certification', 'declared minor', 'must be a daniels student',
    'instructor\'s permission', 'honors program', 'common curriculum requirements'
]

def extract_restrictions(text):
    if not isinstance(text, str):
        return ''
    restrictions = []
    for phrase in restriction_phrases:
        if re.search(phrase, text, re.IGNORECASE):
            restrictions.append(phrase.capitalize() + '.')
    return ' '.join(sorted(set(restrictions)))

df['Preq_Notes'] = df.apply(lambda row: extract_restrictions(f"{row.get('Description', '')} {row.get('Preq_Notes', '')}"), axis=1)

# --- Step 4: Clean Keywords ---
stopwords = set(['students', 'course', 'including', 'focuses', 'introduction', 'overview', 'this', 'will'])

def generate_keywords(description):
    if not isinstance(description, str):
        return ''
    words = re.findall(r'\b[a-z]{3,}\b', description.lower())
    filtered = [w for w in words if w not in stopwords]
    common = Counter(filtered).most_common(10)
    return ', '.join([w for w, _ in common])

df['Keywords'] = df['Description'].apply(generate_keywords)

# --- Step 5: Normalize Course Code Column ---
def clean_course_code(code):
    if not isinstance(code, str):
        return ''
    return ''.join(re.findall(r'\d+', code))

df['Course Code'] = df['Course Code'].apply(clean_course_code)

# --- Step 6: Deduplicate Rows ---
df.drop_duplicates(inplace=True)

# --- Step 7: Save Final Output ---
df.to_csv('final_cleaned_output.csv', index=False)
print("Cleaning complete. Saved to final_cleaned_output.csv")
