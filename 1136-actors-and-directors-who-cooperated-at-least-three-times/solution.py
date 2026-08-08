import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    grouped = actor_director.groupby(['actor_id','director_id']).size().reset_index(name='count')
    res = grouped[grouped['count'] >= 3]
    return res [['actor_id','director_id']]
