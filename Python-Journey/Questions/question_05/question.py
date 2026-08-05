
description = """
You are given a dataset containing a single column named sentence.

Your task is to reverse each word individually in every sentence while keeping the word order the same.


### 🦄 Assumptions
- Input DataFrame contains one column named sentence.

- Each sentence may contain multiple words separated by spaces.

- Output must preserve the original word order.

- Return a DataFrame with two columns:

    - sentence → original sentence

    - reversed_sentence → sentence after reversing each word.
"""
hint = """
- Use .split() to split the sentence into words.

- Reverse each word using slicing ([::-1]).

- Recombine words using ' '.join().

- Apply the logic row-wise using .apply().
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