"""
The idea is to find unique products (id products) on certain dates and count the number of sales.
Make a new dataframe.

required fields:
sale date - created_at field in milk_data table
day of the week - I take myself out of the date
product id - labels table, link to milk_data table by id field (labels table) and label_id field (milk_data table)
is the date a holiday - ???
what is the phase of the moon on the date - ???
"""

from datetime import date
import pandas as pd
import requests as req

milk_data = pd.read_csv("/Users/nikolamuravev/Desktop/milk_data.csv", encoding="utf-8",
                        on_bad_lines="skip")
milk_data.reset_index(drop=True)

labels = pd.read_csv("/Users/nikolamuravev/Desktop/all.csv", encoding="cp1252",
                        on_bad_lines="skip")
labels.reset_index(drop=True)

procentage = pd.read_csv("/Users/nikolamuravev/Desktop/milk_catalogs_items_with_procentage.csv", encoding="utf-8",
                        on_bad_lines="skip")
procentage.reset_index(drop=True)

new_df = pd.DataFrame(columns=["date", "item_id", "day_of_week", "is_day_off", "procentage", "number_of_sales"])
is_exist_new_df = 0
counter = 0


def row_handler(row):
    global is_exist_new_df, counter
    new_id = row["label_id"]
    new_date = row["created_at"].split(" ")[0]
    year = int(new_date.split("-")[0])
    month = int(new_date.split("-")[1])
    day = int(new_date.split("-")[2])
    day_of_week = date(year, month, day).isoweekday()
    is_day_of = (req.get(f"https://isdayoff.ru/api/getdata?year={year}&month={month}&day={day}")).text

    labels_row_check = labels.loc[labels["id"] == new_id]   #begin to conection labels and milk_items tables
    new_id_of_item = labels_row_check["item_id"].item()

    procentage_row_check = procentage.loc[procentage["id"] == new_id_of_item]   #then find the percentage of fat
    new_procentage_of_item = procentage_row_check["procentage"].item()

    if is_exist_new_df == 0:
        new_df.loc[len(new_df)] = [new_date, new_id_of_item, day_of_week, is_day_of, new_procentage_of_item, 1]
        is_exist_new_df = 1
    else:
        uniq_check = new_df.loc[(new_df["date"] == new_date) & (new_df["item_id"] == new_id_of_item)]
        uniq_check_len = len(uniq_check)
        if uniq_check_len != 0:
            uniq_index = int(str(uniq_check["date"]).split("    ")[0])
            new_df.loc[uniq_index, "number_of_sales"] += 1
        else:
            new_df.loc[len(new_df)] = [new_date, new_id_of_item, day_of_week, is_day_of, new_procentage_of_item, 1]
    counter += 1
    print("checked rows: ", counter)

milk_data.apply(lambda row: row_handler(row), axis=1)
new_df.to_csv("/Users/nikolamuravev/Desktop/result/new_df.csv")

print(new_df)