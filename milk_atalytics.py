import pandas as pd

items = pd.read_csv("/Users/matthewpopov/Desktop/catalogs_items.csv")

milk_products = items.loc[items["group"] == "milk"]

print(milk_products)