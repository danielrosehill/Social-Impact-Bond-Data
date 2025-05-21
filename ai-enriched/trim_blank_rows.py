import pandas as pd
from pathlib import Path
import os

def trim_blank_rows(csv_path):
    try:
        df = pd.read_csv(csv_path)
        # Drop rows that are entirely blank or contain only whitespace
        df = df.dropna(how='all')
        df = df.loc[~df.apply(lambda row: row.astype(str).str.strip().eq('').all(), axis=1)]
        df.to_csv(csv_path, index=False)
        print(f"Trimmed: {csv_path}")
    except Exception as e:
        print(f"Error processing {csv_path}: {e}")

def main():
    root = Path("edited-data")
    for dirpath, _, filenames in os.walk(root):
        for filename in filenames:
            if filename.lower().endswith('.csv'):
                trim_blank_rows(Path(dirpath) / filename)

if __name__ == "__main__":
    main()
