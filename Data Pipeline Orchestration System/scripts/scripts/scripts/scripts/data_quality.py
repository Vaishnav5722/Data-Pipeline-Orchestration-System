import pandas as pd


def check_quality():
df = pd.read_csv("/tmp/final_data.csv")
if df.empty:
raise ValueError("Data quality check failed: Empty dataset")