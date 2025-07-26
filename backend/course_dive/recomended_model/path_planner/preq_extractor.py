import pandas as pd
import re


def extract_course_codes(text):
    if not isinstance(text, str):
        return ''
    codes = re.findall(r'\b[A-Z]{2,4}\s*\d{3,4}\b', text)
    codes = [re.sub(r'\s+', '', c) for c in codes]
    return ', '.join(sorted(set(codes)))
# --- Phase 1: Extract sentence/segment after 'prerequisite' keywords ---
def extract_after_prerequisite(text):
    if not isinstance(text, str):
        return ''
    
    # Look for common prerequisite phrases (can expand this)
    patterns = [
        r'prerequisites?:\s*(.*?)(?:\.|;|$)',
        r'pre-?reqs?:\s*(.*?)(?:\.|;|$)',
        r'requires?:\s*(.*?)(?:\.|;|$)',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(1).strip()
    
    return ''  # Nothing found

# --- Phase 2: Extract known restrictions from the text (user can expand this list) ---
prereq_patterns = [
        r"prerequisite[s]*[:\-]?\s*(.*?)(?:\.|\n|$)",  # Prerequisite: CSCI 1010
        r"students must have completed\s+(.*?)(?:\.|\n|$)",
        r"completion of\s+(.*?)(?:\.|\n|$)",  # Completion of BIOL 1010 and CHEM 1020.
        r"requires prior completion of\s+(.*?)(?:\.|\n|$)",
        r"should have taken\s+(.*?)(?:\.|\n|$)",
        r"must complete[d]*\s+(.*?)(?:\.|\n|$)",
        r"recommended:\s*(.*?)(?:\.|\n|$)",  # Recommended: PSYC 1010
        r"previous experience in\s+(.*?)(?:\.|\n|$)",
        r"requires knowledge of\s+(.*?)(?:\.|\n|$)",
        r"entrance requirement[s]*[:\-]?\s*(.*?)(?:\.|\n|$)",
        r"student[s]* should complete[d]*\s+(.*?)(?:\.|\n|$)",
        r"admission to the Daniels College of Business",
        r"business minors only +(.*?)(?:\.|\n|$",
        r"microsoft excel certification",
        r"+(.*?)(?:\.|\n|$declared minor",
        r"must be a Daniels student",
        r"instructor's permission",
        r"honors program",
        r"common curriculum requirements",
        r"sophomore standing",
        r"junior standing",
        r"senior standing"
        r"instructor\'s permission"
    ]

def extract_restrictions(text):
    if not isinstance(text, str):
        return ''
    
    restrictions = []
    for phrase in prereq_patterns:
        if re.search(re.escape(phrase), text, re.IGNORECASE):
            restrictions.append(phrase.capitalize() + '.')
    return ' '.join(sorted(set(restrictions)))

# --- Combine both phases into a clean column transformation ---
def extract_preq_notes(row):
    combined_text = f"{row.get('Description', '')} {row.get('Preq_Notes', '')}"
    
    # Phase 1: Extract sentence after 'prerequisite:' or similar
    after_prereq = extract_after_prerequisite(combined_text)
    print(f"Extracted after prerequisite: {after_prereq}")  # Debugging line
    
    # Phase 2: Apply restriction matcher to that segment
    return extract_restrictions(after_prereq)

# --- Apply to DataFrame ---
def extract_prerequisites_and_notes(df):
    # Extract course codes from all fields (you can keep this logic from earlier)
    df['Prerequisites'] = df.apply(lambda row: extract_course_codes(
        f"{row.get('Description', '')} {row.get('Prerequisites', '')} {row.get('Preq_Notes', '')}"), axis=1)

    # Extract preq note restrictions in two-phase logic
    df['Preq_Notes'] = df.apply(extract_preq_notes, axis=1)
    
    return df
def add_diffuclty_column(df):
    # Add a 'Difficulty' column based on the 'Description' field
    def determine_difficulty(description):
        if not isinstance(description, str):
            return 'Unknown'
        description = description.lower()
        if 'advanced' in description or 'graduate' in description:
            return 'Advanced'
        elif 'beginner' in description or 'introductory' in description or 'intro' in description or 'basic' in description or 'fundamental' in description or 'elementary' in description:
            return 'Beginner'
        elif 'intermediate' in description:
            return 'Intermediate'
        elif 'honors' in description:
            return 'Honors'
        else:
            return 'Unknown'
    def course_title(course_title):
        if not isinstance(course_title, str):
            return ''
        if 'honors' in course_title.lower():
            return 'Honors'
        elif 'advanced' in course_title.lower():
            return 'Advanced'
        elif 'introductory' in course_title.lower() or 'intro' in course_title.lower():
            return 'Beginner'
        elif 'intermediate' in course_title.lower():
            return 'Intermediate'
        else:
            return 'Unknown'
    df['Difficulty'] = df['Description'].apply(determine_difficulty)
    df['Difficulty'] = df.apply(lambda row: course_title(row['Course Title']) if row['Difficulty'] == 'Unknown' else row['Difficulty'], axis=1)
    return df
df = pd.read_csv("/Users/joy/Downloads/course_planner/course-plannerv2/final_cleaned_courses_v1.csv")  # Adjust path as needed
df = extract_prerequisites_and_notes(df)
df = add_diffuclty_column(df)
df.to_csv("/Users/joy/Downloads/course_planner/course-plannerv2/final_cleaned_courses_v1.csv", index=False)  # Save the updated DataFrame
