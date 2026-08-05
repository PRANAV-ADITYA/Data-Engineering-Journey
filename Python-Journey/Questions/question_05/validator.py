import pandas as pd

def validate(user_df: pd.DataFrame, expected_path: str) -> str:
    expected_df = pd.read_csv(expected_path)

    try:
        pd.testing.assert_frame_equal(
            user_df.sort_values('sentence').reset_index(drop=True),
            expected_df.sort_values('sentence').reset_index(drop=True),
            check_dtype=False
        )
        return "✅ Correct! Nicely done."
    except AssertionError as e:
        return f"❌ Not quite yet. {str(e)}"
