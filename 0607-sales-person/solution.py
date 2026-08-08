import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    red_com = company[company['name'] == 'RED']['com_id']
    red_sales_ids = orders[orders['com_id'].isin(red_com)]['sales_id']
    res = sales_person[~sales_person['sales_id'].isin(red_sales_ids)]
    return res[['name']]
