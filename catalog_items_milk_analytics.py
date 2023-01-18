import pandas as pd


def detect_procentage(description: str):
    pass


items = pd.read_csv("catalogs_items.csv")

items = items.drop(labels=["image", "user_info_id", "material_id", "pack", "is_kit", "document_id"], axis=1)

milk_products = items.loc[items["group"] == "milk"]



