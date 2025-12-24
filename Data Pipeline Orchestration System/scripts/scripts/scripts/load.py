import pandas as pd


def load():
df = pd.read_csv("/tmp/transformed_data.csv")
df.to_csv("/tmp/final_data.csv", index=False)