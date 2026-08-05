import pandas as pd
import ast

def normalize_list(val):
    """
    Safely convert the 'words' column string representation to a Python list,
    sort it for comparison, and handle duplicates correctly.
    """
    if isinstance(val, str):
        try:
            lst = ast.literal_eval(val)
        except Exception:
            # handle comma-separated fallback
            lst = [x.strip() for x in val.split(',')]
    elif isinstance(val, list):
        lst = val
    else:
        lst = [val]
    return sorted(lst)

def validate(user_df: pd.DataFrame, expected_path: str) -> str:
    expected_df = pd.read_csv(expected_path)

    # Normalize both dataframes
    user_df = user_df.copy()
    expected_df = expected_df.copy()
    user_df['words'] = user_df['words'].apply(normalize_list)
    expected_df['words'] = expected_df['words'].apply(normalize_list)

    # Sort for consistent comparison
    user_df = user_df.sort_values('group_id').reset_index(drop=True)
    expected_df = expected_df.sort_values('group_id').reset_index(drop=True)

    try:
        pd.testing.assert_frame_equal(
            user_df[['group_id', 'words']],
            expected_df[['group_id', 'words']],
            check_dtype=False
        )
        return "✅ Correct! Your grouping matches expected results."
    except AssertionError as e:
        return f"❌ Not quite yet. Mismatch in grouped values. Details: {str(e)}"
