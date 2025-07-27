import pandas as pd
import re

def normalize_text(text):
    if not isinstance(text, str):
        return ''
    text = text.replace('\u00A0', ' ').replace('\xa0', ' ')
    text = re.sub(r'([A-Z]{3,4})(\d{3,4})', r'\1 \2', text)
    text = re.sub(r'(\d{3,4})([A-Z]{3,4})', r'\1 \2', text)
    text = re.sub(r'([a-z])([A-Z]{3,4})', r'\1 \2', text)
    return text

def extract_valid_prereqs(description, course_title):
    if not isinstance(description, str):
        return ''

    text = normalize_text(description)
    text = text.replace('\n', ' ').replace('\r', ' ')

    code_pattern = re.compile(r'\b([A-Z]{3,4}\s?\d{3,4}[A-Za-z]?)\b')
    codes = code_pattern.findall(text)
    cleaned_codes = sorted(set(c.replace(" ", "").upper() for c in codes))

    # If COMP course has no codes, insert warning or leave blank
    if re.search(r'\bCOMP\s?\d{3,4}', course_title.upper()) and not cleaned_codes:
        return '[⚠ COMP course has no explicit prerequisites]'

    return ', '.join(cleaned_codes)

def update_prerequisites_column(input_file, output_file):
    df = pd.read_csv(input_file)
    df["Prerequisites"] = df.apply(
        lambda row: extract_valid_prereqs(row.get("Description", ""), row.get("Course Title", "")),
        axis=1
    )

    df.to_csv(output_file, index=False)
    print(f"✅ Prerequisites column updated and saved to: {output_file}")
    return df

# === Usage ===
input_path = '/Users/joy/Downloads/preprocessed_courses_high_quality_keywords.csv'
output_path =  '/Users/joy/Downloads/preprocessed_courses_high_quality_keywords.csv' 
update_prerequisites_column(input_path, output_path)# Overwrites same file
