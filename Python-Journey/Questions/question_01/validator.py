import pandas as pd

def validate(user_df: pd.DataFrame, expected_path: str) -> str:
    try:
        expected_df = pd.read_csv(expected_path)

        # Ensure both DataFrames have consistent column names and order
        expected_cols = ['hour', 'seconds']
        user_df = user_df[expected_cols].copy()
        expected_df = expected_df[expected_cols].copy()

        # Sort both for consistent comparison
        user_sorted = user_df.sort_values(by=expected_cols).reset_index(drop=True)
        expected_sorted = expected_df.sort_values(by=expected_cols).reset_index(drop=True)

        # Compare with tolerance on dtype
        pd.testing.assert_frame_equal(user_sorted, expected_sorted, check_dtype=False)

        return "✅ Correct! Well done."

    except AssertionError as e:
        return f"❌ Incorrect. {str(e)}"
    except Exception as e:
        return f"⚠️ Validation error: {str(e)}"
