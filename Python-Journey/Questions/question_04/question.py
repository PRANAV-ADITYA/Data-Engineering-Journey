
description = """
You are given a list of words stored in a DataFrame column named word.
Your task is to group all anagrams together — words that contain the same letters in different orders (e.g., “listen” and “silent”).

You should return a new DataFrame with two columns:

group_id → numeric ID for each anagram group (starting from 1)

words → list of words that are anagrams of each other (as a Python list or comma-separated string)


### 🦄 Assumptions
- Input DataFrame has one column: word.

- Words are lowercase alphabetic strings (no punctuation or spaces).

- Output must be ordered based on the first occurrence of any word from that group in the original DataFrame.

- Each word appears in exactly one group.

"""
hint = """
- Two words are anagrams if their sorted characters are identical.

- You can use ''.join(sorted(word)) as a key for grouping.

- Consider using groupby() or a Python dictionary to collect words.
"""

inital_sample_code = """# Data Available in this DataFrame:
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