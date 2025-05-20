import pandas as pd

def load_courses(path):
    df = pd.read_csv(path)
    df.fillna('', inplace=True)
    return df

def preprocess_text(df, column):
    df[column] = df[column].str.lower().str.replace(r'[^a-zA-Z0-9 ]', '', regex=True)
    return df
