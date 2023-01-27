import time

import requests as req
import pandas as pd
from datetime import datetime


def row_handler(row):
    date = datetime.strptime(row["Date"], '%Y-%m-%d')
    result = req.get(f"https://isdayoff.ru/api/getdata?year={date.year}&month={date.month}&day={date.day}")
    time.sleep(0.1)
    return result.text


df = pd.read_csv("/Users/matthewpopov/Desktop/clean_database/date-sales_number.csv", encoding="utf-8")

df["is_day_off"] = df.apply(lambda row: row_handler(row), axis=1)

print(df)

df.to_csv("/Users/matthewpopov/Desktop/clean_database/date-sales_number_with_day_off_data.csv")





