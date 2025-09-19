# csv_cleaner_pandas.py
import pandas as pd

def clean_csv(input_path, output_path,
              encoding='utf-8',
              strip_whitespace=True,
              drop_duplicates=True,
              date_cols=None,
              na_values=None):
    # Read (try utf-8, fall back to latin-1)
    try:
        df = pd.read_csv(input_path, encoding=encoding, na_values=na_values)
    except UnicodeDecodeError:
        df = pd.read_csv(input_path, encoding='latin-1', na_values=na_values)

    # Trim column names and strip whitespace in string columns
    df.columns = [str(c).strip() for c in df.columns]
    if strip_whitespace:
        str_cols = df.select_dtypes(include=['object']).columns
        df[str_cols] = df[str_cols].apply(lambda s: s.str.strip())

    # Parse dates if provided
    if date_cols:
        for col in date_cols:
            df[col] = pd.to_datetime(df[col], errors='coerce', dayfirst=False)

    # Drop fully empty rows
    df.dropna(how='all', inplace=True)

    # Drop duplicates if asked
    if drop_duplicates:
        df.drop_duplicates(inplace=True)

    # Example: fill simple missing values for numeric columns
    num_cols = df.select_dtypes(include=['number']).columns
    df[num_cols] = df[num_cols].fillna(0)

    # Save cleaned CSV
    df.to_csv(output_path, index=False, encoding='utf-8')
    return df

if __name__ == "__main__":
    import sys
    input_path = sys.argv[1] if len(sys.argv) > 1 else "input.csv"
    output_path = sys.argv[2] if len(sys.argv) > 2 else "cleaned.csv"
    # Example: if your date column is named 'date' use date_cols=['date']
    df = clean_csv(input_path, output_path, date_cols=['date'])
    print("Saved cleaned file:", output_path)
