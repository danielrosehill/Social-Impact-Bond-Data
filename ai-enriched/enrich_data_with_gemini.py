import os
import pandas as pd
import time
from pathlib import Path
from tqdm import tqdm
import requests

# Ensure the AI data enrichment directory exists
output_dir = Path("AI data enrichment")
output_dir.mkdir(exist_ok=True)

# Gemini API setup
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1/models/gemini-2.5-pro:generateContent"

HEADERS = {
    "Content-Type": "application/json"
}

# Helper to query Gemini for enrichment
def query_gemini(project_name, project_description):
    prompt = f"""
Given the following project information, provide:
1. The official website URL of the project/intervention (if available; otherwise say 'Not found').
2. A short, one-paragraph description of the project/intervention suitable for a general audience.

Project Name: {project_name}
Description: {project_description}

Respond in this JSON format:
{{"url": "<official_url>", "description": "<one-paragraph-description>"}}
"""
    data = {
        "contents": [
            {
                "role": "user",
                "parts": [{"text": prompt}]
            }
        ],
        "generationConfig": {"temperature": 0.7, "maxOutputTokens": 512}
    }
    url = f"{GEMINI_API_URL}?key={GEMINI_API_KEY}"
    try:
        response = requests.post(url, headers=HEADERS, json=data, timeout=30)
        response.raise_for_status()
        result = response.json()
        if "candidates" in result and len(result["candidates"]) > 0:
            text = result["candidates"][0]["content"]["parts"][0]["text"]
            import json as pyjson
            try:
                response_json = pyjson.loads(text)
                return response_json.get('url', 'Not found'), response_json.get('description', '')
            except Exception as parse_e:
                print(f"Error parsing Gemini response JSON: {parse_e}. Raw text: {text}")
                return 'Not found', ''
        else:
            print("No candidates in Gemini response.")
            return 'Not found', ''
    except Exception as e:
        print(f"Error with Gemini API: {e}")
        return 'Not found', ''

def enrich_file(input_path, output_path):
    df = pd.read_csv(input_path)
    # Drop rows that are entirely blank or contain only whitespace
    df = df.dropna(how='all')
    df = df.loc[~df.apply(lambda row: row.astype(str).str.strip().eq('').all(), axis=1)]

    # Try to find suitable columns for project name and description
    string_cols = [col for col in df.columns if df[col].dtype == object]
    name_col, desc_col = None, None
    for col in string_cols:
        # Use the first string column with at least one non-empty value as name
        if name_col is None and df[col].astype(str).str.strip().replace('','NaN').ne('NaN').any():
            name_col = col
        # Use the next string column as description
        elif name_col is not None and desc_col is None and df[col].astype(str).str.strip().replace('','NaN').ne('NaN').any():
            desc_col = col
            break
    if name_col is None or desc_col is None:
        print(f"ERROR: Could not detect suitable name/description columns in {input_path.name}. Columns: {df.columns.tolist()}")
        return
    print(f"Using columns: name_col='{name_col}', desc_col='{desc_col}' for {input_path.name}")

    # Only keep rows with meaningful project name or description
    df = df.loc[df[[name_col, desc_col]].apply(lambda x: any(val.strip() for val in x.astype(str)), axis=1)]
    # Add new columns
    df['AI project URL'] = ''
    df['AI project description'] = ''
    for idx, row in tqdm(df.iterrows(), total=len(df), desc=f"Enriching {input_path.name}"):
        project_name = str(row[name_col]) if name_col in row else ''
        project_desc = str(row[desc_col]) if desc_col in row else ''
        if not project_name.strip() and not project_desc.strip():
            continue  # Skip rows with no info
        url, description = query_gemini(project_name, project_desc)
        df.at[idx, 'AI project URL'] = url
        df.at[idx, 'AI project description'] = description
        time.sleep(1.5)  # Respectful delay to avoid hitting rate limits
    df.to_csv(output_path, index=False)
    print(f"Enriched file saved to {output_path}")

if __name__ == "__main__":
    # File paths to enrich
    files_info = [
        {
            "input": Path("edited-data/pay-for-outcomes/deployed-and-historic/current-and-historic-projects.csv"),
            "output": output_dir / "current-and-historic-projects_enriched.csv"
        },
        {
            "input": Path("edited-data/pay-for-outcomes/deployed-and-historic/outcomefunds.csv"),
            "output": output_dir / "outcomefunds_enriched.csv"
        },
        {
            "input": Path("edited-data/pay-for-outcomes/pipeline/pipeline.csv"),
            "output": output_dir / "pipeline_enriched.csv"
        }
    ]
    for info in files_info:
        if info["input"].exists():
            enrich_file(info["input"], info["output"])
        else:
            print(f"Input file {info['input']} not found.")
