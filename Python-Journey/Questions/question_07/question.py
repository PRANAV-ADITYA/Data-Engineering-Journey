
description = r"""
You are given a dataset `data.csv` containing daily demand for multiple SKUs.
Each SKU has:

- Daily demand quantities

- Cost per unit,

- Order cost,

- Holding cost rate


Your task is to:

1. Compute the **Economic Order Quantity (EOQ)** for each SKU using the formula:

    $$
    EOQ = \sqrt{\frac{2 \times D \times S}{H}}
    $$

    where:  
    - \( D \): Annual demand (units per year)  
    - \( S \): Ordering cost per order  
    - \( H \): Holding cost per unit per year

2. Simulate a 180-day inventory system for each SKU assuming:

    - Initial inventory = EOQ

    - Reorder occurs when inventory ≤ 0

    - Lead time is stochastic (random between 2–7 days)

    - Daily demand follows the provided dataset cyclically

3. For each SKU, output a summary DataFrame containing:

    - sku

    - EOQ

    - stockouts (total number of days with stockout)

### 🦄 Assumptions
- Demand data can be reused cyclically for 180 days.

- Lead time is random each time an order is placed.

- The final output must be a DataFrame only


"""
hint = """

- Use random.seed(42) to get consistent outputs.

- Use np.sqrt() for EOQ formula.

- Use a for-loop or rolling simulation to update inventory daily.

- Use random.randint(2, 7) for stochastic lead time.

- Keep track of stockouts when demand > inventory.

"""

inital_sample_code = """
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

# Data Available in this DataFrame:
df = data.copy()

def solve(df: pd.DataFrame):
    # your code here
    
    return result

"""


def get_description():
    return description

def get_hint():
    return hint

def get_inital_sample_code():
    return inital_sample_code