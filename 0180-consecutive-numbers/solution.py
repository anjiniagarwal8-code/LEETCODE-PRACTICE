import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    is_consecutive = ((logs['num'] == logs['num'].shift(1)) &  
    (logs['num'] == logs['num'].shift(2)))
    res = logs[is_consecutive]['num'].drop_duplicates()
    return pd.DataFrame({'ConsecutiveNums': res})
