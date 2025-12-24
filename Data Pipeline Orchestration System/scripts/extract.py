import pandas as pd
import requests


def extract():
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
response.raise_for_status()


df = pd.DataFrame(response.json())
df.to_csv("/tmp/raw_data.csv", index=False)