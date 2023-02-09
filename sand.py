import pandas as pd

PRODUCT_TYPES = ["ТВОРОГ", "СЫР", "МОЛОКО", "ЙОГУРТ", "МОРОЖЕНОЕ", "МАСЛО", "СЛИВКИ",
                 "КЕФИР", "СМЕТАНА"]

df = pd.read_csv("/Users/matthewpopov/Desktop/clean_database/dataset.csv", encoding="utf-8")

milk_products = pd.read_csv("/Users/matthewpopov/Desktop/clean_database/milk_catalogs_items.csv", encoding="utf-8")

def row_handler(row):
    global PRODUCT_TYPES
    item_id = row["item_id"]
    product_row = milk_products.loc[milk_products["id"] == item_id]
    product_name = product_row["name"].tolist()[0]
    product_type = product_name.split()[0].upper()
    if product_type in PRODUCT_TYPES:
        return product_type
    else:
        return "ДРУГОЕ"


del df[df.columns[0]]

df["product_type"] = df.apply(lambda row: row_handler(row), axis=1)

del df[df.columns[2]]

df.to_csv("/Users/matthewpopov/Desktop/clean_database/dataset_types.csv")