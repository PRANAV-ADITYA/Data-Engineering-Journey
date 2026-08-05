description = """
You are provided with a dataset containing Netflix user watch session logs. Each log entry contains the user_id, title of the movie/show, seconds watched, and a timestamp (ts). Your task is to compute the total number of seconds watched per hour for October 21st, 2025, and then return the top 5 hours with the highest total seconds watched.

The goal is to aggregate the total watch time per hour across all users for the specified date and return the **top 5** hours with the highest total seconds watched.


### 🦄 Assumptions
- The ts timestamp in the dataset is in the format YYYY-MM-DD HH:MM:SS.

- You are specifically asked to compute the total seconds watched for October 21st, 2025.

- The time should be grouped by the hour, meaning you will ignore the minute and second components of the timestamp.

- The seconds value represents the total watch time for a session and should be summed up per hour.
"""
hint = """
- Ensure that you handle the timestamp correctly by converting it to a datetime object and then extracting the date and hour.

- Group the data by the date and hour columns and aggregate the seconds using the sum() function.
"""

inital_sample_code = """# Data Available in this Dataframe:
df = data.copy()

# Write your solution code here
# result = 

# return the Dataframe
result

"""


def get_description():
    return description

def get_hint():
    return hint

def get_inital_sample_code():
    return inital_sample_code