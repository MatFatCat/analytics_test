import pandas as pd

labels = pd.read_csv("/Users/matthewpopov/Desktop/tables/all_labels.csv", encoding="cp1252",
                     on_bad_lines="skip")
labels_story_50 = pd.read_csv("/Users/matthewpopov/Desktop/tables/all_history.csv", encoding="utf-8",
                              on_bad_lines="skip")
catalogs_items = pd.read_csv("/Users/matthewpopov/Desktop/tables/catalogs_items.csv", encoding="utf-8",
                             on_bad_lines="skip")
ok_rows_counter = 0
counter = 0

labels.reset_index(drop=True)
labels_story_50.reset_index(drop=True)
catalogs_items.reset_index(drop=True)

df_ok_rows = pd.DataFrame(columns=["id", "label_id", "message", "user_id", "created_at",
                                   "action", "action_id", "recipient", "user_info_id", "is_viewed"])


def row_handler(row):

    global ok_rows_counter, counter
    label_id = row["label_id"]
    label_row = labels.loc[labels["id"] == label_id]

    if len(label_row) != 0:
        item_id = label_row["item_id"]
        item_row = catalogs_items.loc[catalogs_items["id"] == item_id.iloc[0]]
        name, description = item_row["name"], item_row["description"]
        ok_rows_counter += 1
        print(f"NAME = [{name}] | DESCRIPTION = [{ok_rows_counter}]")

        df_ok_rows.loc[len(df_ok_rows)] = row
        df_ok_rows.to_csv("/Users/matthewpopov/Desktop/ok_rows.csv")

    counter += 1

    print(f"COUNTER = {counter}, OK ROWS = {ok_rows_counter}")


labels_story_50 = labels_story_50.iloc[131310:]

labels_story_50.apply(lambda row: row_handler(row), axis=1)

print(df_ok_rows)