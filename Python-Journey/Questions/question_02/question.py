import re

description = """
You are given two sentences. Your task is to identify all the common words between the two sentences and count how many times each common word appears in the second sentence.

The final output should be a Python dictionary where:

The keys are the common words.

The values represent how many times those words occur in the second sentence.


### 🦄 Assumptions
- Words are separated by spaces.

- The comparison should be case-sensitive (i.e., 'Here' and 'here' are treated as different words).

- Ignore punctuation marks (like ., ,, !, ?) when comparing words.

- The output dictionary should be sorted alphabetically by word (optional but recommended for cleaner output).
"""
hint = """
- Use Python's split() to break sentences into words.

- Use set() to find common words.

- Use count() or a Counter from the collections module to count word occurrences.
"""

inital_sample_code = """# Data Available in this DataFrame:
df = data.copy()
## 
# Each row has two sentences: sentence_1 and sentence_2
# Write your solution code here

def find_common_words(row):
    s1 = row['sentence_1']
    s2 = row['sentence_2']
    # Your logic here
   


# return the DataFrame
#df

"""


def get_description():
    return description

def get_hint():
    return hint

def get_inital_sample_code():
    return inital_sample_code