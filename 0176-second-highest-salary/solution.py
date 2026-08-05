import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    unisal= employee['salary'].drop_duplicates().sort_values(ascending=False)
    if len(unisal) < 2:
        second_sal = None
    else:
        second_sal= unisal.iloc[1]
    return pd.DataFrame({'SecondHighestSalary' : [second_sal]})
