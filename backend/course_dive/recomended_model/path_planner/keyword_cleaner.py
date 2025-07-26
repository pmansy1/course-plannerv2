import pandas as pd
import spacy
import re

# Load spaCy English model
# For better quality phrase extraction, consider 'en_core_web_md' or 'en_core_web_lg' if performance allows.
# If you haven't downloaded them, run in your environment's terminal: python -m spacy download en_core_web_md
nlp = spacy.load("en_core_web_sm")

# Refined Custom words to exclude
# Removed redundancies and focused on academic boilerplate and generic terms.
# Words covered by spaCy's default stop list are generally removed.
EXCLUDED_TERMS = {
    "course", "courses", "student", "students", "introduction", "intended", "topics",
    "including", "overview", "focus", "required", "basic", "advanced",
    "background", "discussion", "examines", "explores", "emphasis", 
    "lecture", "prerequisite", "credit", "credits", "offered", "class", 
    "learn", "study", "develop", "provide", "process", "issue", "skill",
    "work", "practice", "society", "requirement", "business", "design",
    "world", "cultural", "social", "explore", "topic", "culture", "include",
    "program", "university", "department", "academic", "major", "minor",
    "areas", "area", "various", "different", "specific", "fundamental", 
    "understand", "knowledge", "ability", "concepts", "concept", "theory",
    "problem", "problems", "analysis", "application", "aspects", "framework",
    "approaches", "approach", "tools", "techniques", "methods", "method", 
    "principles", "principle", "context", "practical", "critical", "theoretical", 
    "history", "historical", "current", "contemporary", "case", "studies", "study",
    "data", "model", "models", "modeling", "system", "systems", "research", 
    "project", "projects", "activity", "activities", "role", "roles", 
    "function", "functions", "key", "main", "interdisciplinary", 
    "global", "national", "international", "local", "community", "communities", 
    "environment", "environments", "field", "fields", "discipline", "disciplines",
    "human", "political", "economic", "technological", "scientific",
    "communication", "decision", "making", "development", "will", "able", "well",
    # Specific terms identified from initial keyword analysis that are often not valuable
    "datum", "popular", "remove", "change", "allow", "perform", "daniels", "path", "ui", "rpa",
    "robot", "robotic", "robotic process automation", # If RPA is too specific, but for keywords, this might be good.
    "statement", "content", "reporting", "accounting process", "cycle", "income determination",
    "official statement", "official accounting theory", "fact pattern", "guidance"
}

def spacy_extract_keywords(text):
    """
    Extracts meaningful phrases and filtered lemmatized words using spaCy.
    Returns a list of unique, cleaned keywords.
    """
    if not isinstance(text, str) or text.strip() == "":
        return []

    # Basic text cleaning before spaCy:
    # 1. Convert to lowercase.
    # 2. Remove text in brackets or parentheses (e.g., administrative notes).
    # 3. Normalize whitespace (multiple spaces to single space).
    text = text.lower()
    text = re.sub(r'\[.*?\]|\(.*?\)', '', text) 
    text = re.sub(r'\s+', ' ', text).strip()

    doc = nlp(text)

    extracted_terms = set()

    # 1. Extract multi-word noun chunks (phrases)
    for chunk in doc.noun_chunks:
        chunk_text = chunk.text.strip()
        # Filter:
        # - Longer than one word
        # - Not composed entirely of stopwords (e.g., "the of")
        # - Not in EXCLUDED_TERMS
        # - Minimum length to avoid very short phrases
        # - At least one alpha character (to avoid chunks like "123")
        if len(chunk_text.split()) > 1 and \
           not all(token.is_stop for token in chunk) and \
           chunk_text not in EXCLUDED_TERMS and \
           len(chunk_text) > 2 and \
           any(char.isalpha() for char in chunk_text):
            extracted_terms.add(chunk_text)

    # 2. Extract filtered single-word tokens (lemmatized)
    # Focusing on Nouns, Proper Nouns, and Adjectives for high-value content keywords.
    # Removed 'VERB' from the default POS check for content keywords.
    for token in doc:
        if token.pos_ in {"NOUN", "PROPN", "ADJ"} and \
           token.is_alpha and \
           not token.is_stop and \
           token.lemma_ not in EXCLUDED_TERMS and \
           len(token.lemma_) > 2: # Filter very short words
            extracted_terms.add(token.lemma_)

    # Convert the set to a list and sort for consistent output
    return sorted(list(extracted_terms))

def clean_keywords(keywords_list):
    """
    Converts a list of keywords into a comma-separated string for CSV storage.
    Handles empty lists gracefully.
    """
    if not keywords_list:
        return ""
    return ", ".join(keywords_list)

# Main execution block

if __name__ == "__main__":
    # Load your CSV file (replace with your file path)
    df = pd.read_csv("/Users/joy/Downloads/course_planner/course-plannerv2/final_cleaned_courses_v1.csv") # Assuming it's in the same directory or provide full path

    # Extract and clean keywords from course descriptions
    # Apply the function to the 'Description' column
    df['Keywords'] = df['Description'].apply(spacy_extract_keywords)

    # Convert the list of keywords to a comma-separated string for CSV storage
    # This creates a new column for the string representation, keeping the list for potential further processing
    df['Keywords'] = df['Keywords'].apply(clean_keywords)

    # You might want to overwrite the original 'Keywords' column or create a new one.
    # If you want to replace the original 'Keywords' column:
    # df['Keywords'] = df['Keywords_Cleaned_String']
    # If you want to keep the original and have a new clean one:
    # (as done above with 'Keywords_Cleaned_String')

    # Save the updated DataFrame with cleaned keywords for later use
    # Make sure to save to a new file or be careful overwriting if you need the original for comparison
    output_path = "/Users/joy/Downloads/course_planner/course-plannerv2/final_cleaned_courses_v1.csv"
    df.to_csv(output_path, index=False)

    print(f"Keyword extraction and cleaning complete. Saved to {output_path}")
    print("\nSample output of new 'Keywords' column:")
    print(df[['Course Code', 'Course Title', 'Description', 'Keywords']].head())

    print("\nSample output of 'Keywords List' column (actual Python list):")
    print(df[['Course Code', 'Course Title', 'Keywords']].head())
    print("\nCheck a specific row to see the list format:")
    print(df['Keywords'].iloc[0])