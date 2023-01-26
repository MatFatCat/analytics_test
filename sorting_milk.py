import pandas as pd

counter = 0
milk_counter = 0

labels = pd.read_csv("/Users/matthewpopov/Desktop/tables/all_labels.csv", encoding="cp1252",
                     on_bad_lines="skip")
catalogs_items = pd.read_csv("/Users/matthewpopov/Desktop/tables/catalogs_items.csv", encoding="utf-8",
                             on_bad_lines="skip")
catalogs_items = catalogs_items.loc[catalogs_items["group"] == "milk"]

milk_story_db = pd.DataFrame(columns=["id", "label_id", "message", "user_id", "created_at",
                                   "action", "action_id", "recipient", "user_info_id", "is_viewed"])
all_db = pd.read_csv("/Users/matthewpopov/Desktop/clean_database/all_db.csv", encoding="utf-8",
                             on_bad_lines="skip")

all_db = all_db[all_db.columns[1:]]

all_db.to_csv("/Users/matthewpopov/Desktop/clean_database/all_db.csv")


def check_if_milk(row):
    global counter, milk_counter
    label_id = row["label_id"]
    label_row = labels.loc[labels["id"] == label_id]
    item_id = label_row["item_id"]
    item_row = catalogs_items.loc[catalogs_items["id"] == item_id.iloc[0]]

    if len(item_row) != 0:
        milk_story_db.loc[len(milk_story_db)] = row

        print("milk")
        milk_counter += 1

    counter += 1

    print(f"Counter = [{counter} <= 233066], milk counter = {milk_counter}")


all_db.apply(lambda row: check_if_milk(row), axis=1)

print(milk_story_db)

milk_story_db.to_csv("/Users/matthewpopov/Desktop/clean_database/milk_story_db.csv")



