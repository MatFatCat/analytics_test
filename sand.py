import time
import requests as req
import pandas as pd
from datetime import datetime


def row_handler(row): return datetime.strptime(row["date"], '%Y-%m-%d').weekday()


PATH = "/Users/matthewpopov/Desktop/clean_database/dataset.csv"

df = pd.read_csv(PATH, encoding="utf-8")

df = df.drop(["Unnamed: 0", "Unnamed: 0.1"], axis=1)

print(df)

df["day_of_week_number"] = df.apply(lambda row: row_handler(row), axis=1)

print(df)

df.to_csv("/Users/matthewpopov/Desktop/clean_database/dataset.csv")
