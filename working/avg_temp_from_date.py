# Import Meteostat library and dependencies
from meteostat import Daily, Point
import pandas as pd
from datetime import datetime

location = Point(53.893009, 27.567444, 70)  # Minsk's coordinates

df = pd.read_csv("/Users/matthewpopov/Desktop/clean_database/final_dataset.csv", encoding="utf-8")


def avg_temp_from_date(row):
    date = datetime.strptime(row["date"], '%Y-%m-%d')
    start_date = datetime(date.year, date.month, date.day)
    end_date = datetime(date.year, date.month, date.day)
    data = Daily(location, start_date, end_date)
    data = data.fetch()
    return data.tavg[0]


df["tavg"] = df.apply(lambda row: avg_temp_from_date(row), axis=1)

df.to_csv("/Users/matthewpopov/Downloads/test.csv")