import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    df = employee["salary"].drop_duplicates().sort_values(ascending=False)
    if N <= 0 or len(df) < N:
        res = None
    else:
        res = df.iloc[N - 1]
    return pd.DataFrame({f"getNthHighestSalary({N})": [res]})
