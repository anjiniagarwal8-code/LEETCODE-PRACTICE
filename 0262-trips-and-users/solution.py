import pandas as pd

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    unbanned_users = users[users['banned'] == 'No']['users_id']
    valid_trips = trips[(trips['client_id'].isin(unbanned_users)) & (trips['driver_id'].isin(unbanned_users)) & (trips['request_at'].between('2013-10-01','2013-10-03'))].copy()
    if valid_trips.empty:
        return pd.DataFrame(columns=['Day','Cancellation Rate'])
    valid_trips['is_cancelled']= valid_trips['status'] != 'completed'
    res = valid_trips.groupby('request_at')['is_cancelled'].mean().round(2).reset_index()
    return res.rename(columns={'request_at' : 'Day','is_cancelled': 'Cancellation Rate'})
