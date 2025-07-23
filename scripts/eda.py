import matplotlib.pyplot as plt
import seaborn as sns

def plot_fraud_distribution(df):
    sns.countplot(x='is_fraud', data=df)
    plt.title("Fraud Distribution")
    plt.savefig("outputs/fraud_distribution.png")

def plot_time_since_signup(df):
    sns.histplot(df['time_since_signup'], bins=50)
    plt.title("Time Since Signup")
    plt.savefig("outputs/time_since_signup.png")

def plot_hour_of_day(df):
    sns.countplot(x='hour_of_day', data=df)
    plt.title("Purchases by Hour")
    plt.savefig("outputs/hour_of_day.png")
