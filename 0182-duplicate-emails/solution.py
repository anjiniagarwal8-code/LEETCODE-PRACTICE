import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    dup_mask = person.duplicated(subset=['email'])
    res = person[dup_mask][['email']].drop_duplicates()
    return res.rename(columns={'email' : 'Email'})
    
