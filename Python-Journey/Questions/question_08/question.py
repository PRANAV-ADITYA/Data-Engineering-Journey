
description = r"""
You are given a dataset `data.csv` containing daily **GMV (Gross Merchandise Value)** for an ecommerce platform.  

Your task is to identify **anomalous days** — days where GMV deviates significantly from the norm using the **Z-score** method.

---

The Z-score for each day’s GMV is calculated as:

$$
Z = \frac{x - \mu}{\sigma}
$$

Where:  
- \( x \): GMV of the day  
- \( \mu \): Mean GMV across all days  
- \( \sigma \): Standard deviation of GMV  

---

#### 🚩 Anomaly Condition

Flag a day as **anomalous** if:

$$
|Z| > 2.5
$$

---

### 🦄 Assumptions
- Input file: `data.csv` with columns `['day', 'gmv']`  

- Days can be integers or date strings  

- If no anomalies exist, output an empty df 


"""
hint = """
- Use `df['gmv'].mean()` and `.std()` to compute the mean and standard deviation  

- Compute a new column `zscore = (gmv - mean) / std`  

- Apply a filter: `df[abs(df['zscore']) > 2.5]`  

"""

inital_sample_code = """
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

# Data Available in this DataFrame:
df = data.copy()

def solve(df: pd.DataFrame) -> pd.DataFrame:
    # your code here
    return result

"""


def get_description():
    return description

def get_hint():
    return hint

def get_inital_sample_code():
    return inital_sample_code