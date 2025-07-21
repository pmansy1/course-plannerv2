# keyword_cleaner.py
import pandas as pd
import spacy
import re

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

def clean_keywords(text):
    """
    Clean and extract keywords from text:
    - Lowercase
    - Remove punctuation and digits
    - Remove stopwords and short words
    - Lemmatize tokens to base form
    Returns cleaned keywords as a space-separated string.
    """
    if not isinstance(text, str):
        return ""

    # Lowercase
    text = text.lower()

    # Remove punctuation and digits (keep only letters and spaces)
    text = re.sub(r"[^a-z\s]", " ", text)

    # Remove multiple spaces
    text = re.sub(r"\s+", " ", text).strip()

    # Process text with spaCy
    doc = nlp(text)

    # Filter tokens: keep only alphabetic tokens that are not stopwords and longer than 2 characters
    keywords = [
        token.lemma_ for token in doc
        if token.is_alpha and not token.is_stop and len(token) > 2
    ]

    # Join keywords back into a single string
    cleaned_text = " ".join(keywords)
    return cleaned_text

def extract_keywords_from_df(df, source_column='Description', target_column='Keywords'):
    """
    Given a dataframe, clean the text in source_column and save cleaned keywords
    into target_column.
    """
    df[target_column] = df[source_column].fillna('').apply(clean_keywords)
    return df

if __name__ == "__main__":
    # Example usage

    # Load your CSV file (replace with your file path)
    df = pd.read_csv("final_cleaned_courses_v1.csv")

    # Extract and clean keywords from course descriptions (or whichever column)
    df = extract_keywords_from_df(df, source_column='Description', target_column='Keywords')

    # Save the updated DataFrame with cleaned keywords for later use
    df.to_csv("final_cleaned_courses_v1.csv", index=False)

    print("Keyword extraction and cleaning complete. Sample output:")
    print(df[['Course Code', 'Course Title', 'Keywords']].head())
