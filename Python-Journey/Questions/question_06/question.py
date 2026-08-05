
description = """
You are given JSON clickstream data where each record contains:

- a timestamp (string in ISO format)

- a text field containing words (e.g., search queries, chat messages, or actions)

Your task is to:

1. Parse the JSON data.

2. Create hourly time buckets (e.g., 09:00–10:00, 10:00–11:00, etc.).

3. For each bucket, identify the most frequently occurring word.

4. Return the output in the following format: "HH:00 - HH:00 WORD COUNT"

### 🦄 Assumptions

- Consider only alphabetic words (ignore words containing numbers)

- If multiple words have the same highest frequency within an hour, select the word that comes first when sorted alphabetically.

- Input DataFrame has a single column: json_data (each row is a JSON string).

- Each JSON object has the following structure:
{"timestamp": "2025-10-28T09:34:22", "text": "learn python data"}

- Words are case-insensitive; treat "Data" and "data" as the same.

- Ignore punctuation.

- Output DataFrame should have one column: summary, containing strings in the format:
"HH:00 - HH:00 WORD COUNT".

- Output must be sorted by hour.
"""
hint = """
- Use json.loads() to parse JSON strings.

- Convert timestamps using pd.to_datetime().

- Use df['timestamp'].dt.hour to extract hour buckets.

- Use collections.Counter or explode() with groupby() to find word frequencies.
"""

inital_sample_code = """
import pandas as pd
import json
from collections import Counter
import re

# Data Available in this DataFrame:
df = data.copy()

def solve(df: pd.DataFrame) -> pd.DataFrame:
    # your code here
    
    return result


# return the DataFrame
#df

"""


def get_description():
    return description

def get_hint():
    return hint

def get_inital_sample_code():
    return inital_sample_code