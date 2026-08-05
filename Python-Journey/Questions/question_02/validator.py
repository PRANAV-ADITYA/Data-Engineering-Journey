import pandas as pd
import ast

def validate(user_df: pd.DataFrame, expected_path: str) -> str:
    """
    Validates the user's output DataFrame against the expected CSV.
    Handles dictionary comparison robustly, avoiding unhashable-type errors.
    """
    try:
        expected_df = pd.read_csv(expected_path)

        # Step 1 — Structural validation
        if list(user_df.columns) != list(expected_df.columns):
            return f"❌ Column mismatch.\nExpected: {list(expected_df.columns)}\nGot: {list(user_df.columns)}"

        # Step 2 — Make defensive copies
        user_df = user_df.copy().reset_index(drop=True)
        expected_df = expected_df.copy().reset_index(drop=True)

        # Step 3 — Convert dict-like strings safely to string (prevent hash error)
        # Only for sorting purposes
        def _stringify_dicts(df):
            for col in df.columns:
                df[col] = df[col].apply(lambda x: str(x) if isinstance(x, (dict, list)) else x)
            return df

        u_sortable = _stringify_dicts(user_df.copy())
        e_sortable = _stringify_dicts(expected_df.copy())

        # Step 4 — Sort only by non-output columns (if any)
        comparable_cols = [c for c in user_df.columns if c != "output"]
        if comparable_cols:
            u_sortable = u_sortable.sort_values(by=comparable_cols, kind="mergesort").reset_index(drop=True)
            e_sortable = e_sortable.sort_values(by=comparable_cols, kind="mergesort").reset_index(drop=True)

        # Step 5 — Row-by-row comparison
        for i, (u_row, e_row) in enumerate(zip(u_sortable.itertuples(index=False),
                                               e_sortable.itertuples(index=False))):
            for col, u_val, e_val in zip(u_sortable.columns, u_row, e_row):
                if col == "output":
                    try:
                        u_dict = ast.literal_eval(str(u_val))
                        e_dict = ast.literal_eval(str(e_val))
                    except Exception:
                        return f"❌ Row {i+1}: Invalid dictionary format in column 'output'."

                    if u_dict != e_dict:
                        return f"❌ Row {i+1}: Mismatch in 'output'.\nExpected: {e_dict}\nGot: {u_dict}"

                else:
                    if str(u_val).strip() != str(e_val).strip():
                        return f"❌ Row {i+1}: Mismatch in column '{col}'.\nExpected: '{e_val}'\nGot: '{u_val}'"

        return "✅ Correct! Well done."

    except Exception as e:
        return f"❌ Validation failed: {e}"
