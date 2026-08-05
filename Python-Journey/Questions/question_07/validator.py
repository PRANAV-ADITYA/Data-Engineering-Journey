import pandas as pd
import numpy as np
import os
import random

# Tolerances
REL_TOL = 0.025   # 2.5% relative tolerance
ABS_TOL = 2.0     # absolute tolerance on EOQ

def _close(a, b, rtol=REL_TOL, atol=ABS_TOL):
    return np.isclose(a, b, rtol=rtol, atol=atol)

def _load_demand():
    # Try common locations
    for path in ["demand.csv", "questions/question_07/data.csv"]:
        if os.path.exists(path):
            return pd.read_csv(path)
    raise FileNotFoundError("Could not find 'demand.csv' or 'questions/question_07/data.csv'.")

def validate(user_df: pd.DataFrame, expected_path: str) -> str:
    """
    Validates:
      - Presence of columns: sku, EOQ  (stockouts optional)
      - EOQ per-SKU close to either accepted convention:
           A) H = holding_rate * unit_cost
           B) H = holding_rate
      - 'stockouts' (if present) is a non-negative integer-like column.

    NOTE: We do NOT fail on stockouts mismatch because lead time is stochastic and
          different (but still reasonable) order/logical choices can alter counts.
    """
    # Basic columns
    if 'sku' not in user_df.columns or 'EOQ' not in user_df.columns:
        return "❌ Incorrect. Output must include columns: ['sku','EOQ'] (and optional 'stockouts')."

    # Load demand to compute targets
    try:
        demand = _load_demand()
    except Exception as e:
        return f"❌ Validator setup error: {e}"

    # Build EOQ targets under both conventions
    targets = []
    for sku, g in demand.groupby('sku'):
        daily = g['demand'].values
        if len(daily) == 0:
            continue
        D_annual = daily.sum() * (365.0 / len(daily))
        S = float(g['order_cost'].iloc[0])
        rate = float(g['holding_cost'].iloc[0])
        unit_cost = float(g['unit_cost'].iloc[0])

        # Convention A (reference): H = rate * unit_cost
        H_a = rate * unit_cost
        eoq_a = np.sqrt((2.0 * D_annual * S) / H_a)

        # Convention B (alternate): H = rate
        H_b = rate
        eoq_b = np.sqrt((2.0 * D_annual * S) / H_b)

        targets.append({'sku': sku, 'EOQ_expected': eoq_a, 'EOQ_alt': eoq_b})

    target_df = pd.DataFrame(targets)

    # Merge user output with targets
    merged = (user_df[['sku', 'EOQ']].copy()
              .merge(target_df, on='sku', how='left'))
    if merged['EOQ_expected'].isna().any():
        missing = merged.loc[merged['EOQ_expected'].isna(), 'sku'].tolist()
        return f"❌ Incorrect. Unknown SKU(s) in output (not found in demand): {missing}"

    # Check EOQ against accepted conventions
    try:
        user_eoq = pd.to_numeric(merged['EOQ'])
    except Exception:
        return "❌ Incorrect. 'EOQ' must be numeric."

    ok_exp = _close(user_eoq.values, merged['EOQ_expected'].values)
    ok_alt = _close(user_eoq.values, merged['EOQ_alt'].values)
    ok_any = ok_exp | ok_alt

    if not ok_any.all():
        bad = merged.loc[~ok_any, ['sku', 'EOQ', 'EOQ_expected', 'EOQ_alt']]
        sample = bad.head(5).to_dict(orient='records')
        return ("❌ Incorrect. EOQ does not match accepted conventions for some SKUs "
                f"(showing up to 5): {sample}")

    # Optional: stockouts sanity check
    if 'stockouts' in user_df.columns:
        try:
            stc = pd.to_numeric(user_df['stockouts'])
        except Exception:
            return "❌ Incorrect. 'stockouts' must be numeric."
        if (stc < 0).any():
            return "❌ Incorrect. 'stockouts' must be non-negative."

        # --- Strict stockouts check (DISABLED by default) ---
        # If you want strict matching, uncomment this block.
        # def simulate_stockouts(g, EOQ):
        #     daily = g['demand'].values
        #     random.seed(42); np.random.seed(42)
        #     inv = EOQ; stockouts = 0; on_order = 0; deliv = {}
        #     for day in range(1, 181):
        #         if day in deliv:
        #             inv += deliv[day]
        #             del deliv[day]
        #         d = float(daily[(day - 1) % len(daily)])
        #         if d > inv:
        #             stockouts += 1
        #             d = inv
        #         inv -= d
        #         if inv <= 0 and on_order == 0:
        #             lead = random.randint(2, 7)
        #             deliv[day + lead] = EOQ
        #             on_order = 1
        #         if on_order and all(day < k for k in deliv.keys()):
        #             on_order = 0
        #     return stockouts
        #
        # # Compare only when using convention A EOQ to keep it deterministic:
        # strict = []
        # for sku, g in demand.groupby('sku'):
        #     eoq_ref = target_df.loc[target_df['sku']==sku, 'EOQ_expected'].values[0]
        #     strict.append({'sku': sku, 'stockouts_expected': simulate_stockouts(g, eoq_ref)})
        # strict_df = pd.DataFrame(strict)
        # chk = (user_df[['sku','stockouts']].merge(strict_df, on='sku', how='left'))
        # if (chk['stockouts'] != chk['stockouts_expected']).any():
        #     diffs = chk.loc[chk['stockouts'] != chk['stockouts_expected']].head(5).to_dict(orient='records')
        #     return (f"❌ Incorrect. Stockouts differ from canonical simulation (seed=42). "
        #             f"(showing up to 5): {diffs}")

    return ("✅ Correct! EOQ matches an accepted convention "
            "(H = rate×unit_cost OR H = rate). "
            "Stockouts are treated as optional/sanity-checked only.")
