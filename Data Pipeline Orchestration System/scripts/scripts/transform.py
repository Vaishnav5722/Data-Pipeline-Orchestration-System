import pandas as pd


def transform():
df = pd.read_csv("/tmp/raw_data.csv")
df['title_length'] = df['title'].apply(len)
df.to_csv("/tmp/transformed_data.csv", index=False)