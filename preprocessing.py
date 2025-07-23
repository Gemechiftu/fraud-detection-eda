import pandas as pd
import numpy as np

def load_data(fraud_path, ip_path):
    fraud_df = pd.read_csv(fraud_path)
    ip_df = pd.read_csv(ip_path)
    return fraud_df, ip_df

def preprocess_data(df):
    # Drop duplicates
    df = df.drop_duplicates()

    # Convert to datetime
    df['signup_time'] = pd.to_datetime(df['signup_time'])
    df['purchase_time'] = pd.to_datetime(df['purchase_time'])

    # Feature engineering
    df['time_since_signup'] = (df['purchase_time'] - df['signup_time']).dt.total_seconds()
    df['hour_of_day'] = df['purchase_time'].dt.hour
    df['day_of_week'] = df['purchase_time'].dt.dayofweek

    return df

def merge_ip_data(fraud_df, ip_df):
    # Convert IP to integer for merging
    fraud_df['ip_int'] = fraud_df['ip_address'].apply(ip_to_int)
    ip_df['lower_bound_ip_address'] = ip_df['lower_bound_ip_address'].apply(ip_to_int)
    ip_df['upper_bound_ip_address'] = ip_df['upper_bound_ip_address'].apply(ip_to_int)

    # Merge using conditions
    merged_df = fraud_df.merge(ip_df, how='left', left_on='ip_int', right_on='lower_bound_ip_address')
    return merged_df

def ip_to_int(ip):
    try:
        return int(''.join(['{:03}'.format(int(x)) for x in ip.split('.')]))
    except:
        return np.nan
