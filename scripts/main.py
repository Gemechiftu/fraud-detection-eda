import os
import pandas as pd
from preprocessing import preprocess_data
from ip_merge import merge_ip_country
from eda import plot_fraud_distribution, plot_time_since_signup, plot_hour_of_day

# Define paths
fraud_data_path = "../data/fraud_train.csv"
ip_data_path = "../data/ip_data.csv"
output_cleaned_path = "../outputs/cleaned_fraud_data.csv"

# Make sure outputs folder exists
os.makedirs("../outputs", exist_ok=True)

# Step 1: Preprocess data
df, ip_df = preprocess_data(fraud_data_path, ip_data_path)

# Step 2: Merge IP to country
df = merge_ip_country(df, ip_df)

# Step 3: Save cleaned data
df.to_csv(output_cleaned_path, index=False)
print(f"Cleaned data saved to {output_cleaned_path}")

# Step 4: Run EDA
plot_fraud_distribution(df)
plot_time_since_signup(df)
plot_hour_of_day(df)

print("EDA plots saved to outputs/")
