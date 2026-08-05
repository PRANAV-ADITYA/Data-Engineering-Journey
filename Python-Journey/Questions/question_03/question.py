
description = """
You are given a string. Your task is to determine whether it is a palindrome — meaning it reads the same forwards and backwards — while ignoring spaces and letter case.

For example:

"Race car" → Palindrome

"Data Analytics" → Not a palindrome

Your function should return a DataFrame with a single column named is_palindrome containing a boolean value (True or False).


### 🦄 Assumptions
- Input DataFrame contains one column: text.

- Palindrome check must be case-insensitive and ignore spaces.

- Return a DataFrame with one row and one column: is_palindrome.

- Only alphabetic characters and spaces are considered (ignore punctuation).
"""
hint = """
- Convert the string to lowercase and remove spaces before checking.

- You can reverse a string using slicing ([::-1]).

- Compare the cleaned string with its reversed version.
"""

inital_sample_code = """# Data Available in this DataFrame:
df = data.copy()
# your code here


# return the DataFrame
#df

"""


def get_description():
    return description

def get_hint():
    return hint

def get_inital_sample_code():
    return inital_sample_code