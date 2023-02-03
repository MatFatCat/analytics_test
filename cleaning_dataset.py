import dask.dataframe as dd
import pandas as pd

labels = dd.read_csv("/Users/matthewpopov/Desktop/clean_database/milk_labels_50M.csv", encoding="utf-8",
                     on_bad_lines="skip")
labels_story_50 = pd.read_csv("/Users/matthewpopov/Desktop/clean_database/all_history.csv", encoding="utf-8",
                              on_bad_lines="skip")
catalogs_items = dd.read_csv("/Users/matthewpopov/Desktop/clean_database/milk_catalogs_items.csv", encoding="utf-8",
                             on_bad_lines="skip")
ok_rows_counter = 0
counter = 0

labels.reset_index(drop=True)
labels_story_50.reset_index(drop=True)
catalogs_items.reset_index(drop=True)

df_ok_rows = pd.DataFrame(columns=["id", "label_id", "message", "user_id", "created_at",
                                   "action", "action_id", "recipient", "user_info_id", "is_viewed"])
df_ok_rows = dd.from_pandas(df_ok_rows, npartitions=3)


def row_handler(row):
    global ok_rows_counter, counter
    label_row = labels.loc[labels["id"] == row["label_id"]]

    if len(label_row) != 0:
        ok_rows_counter += 1
        df_ok_rows.loc[len(df_ok_rows)] = row

        df_ok_rows.to_csv("/Users/matthewpopov/Desktop/clean_database/ok_rows_4.csv")

    counter += 1

    print(f"COUNTER = {counter}, OK ROWS = {ok_rows_counter}")

labels_story_50 = labels_story_50.iloc[2523432:3200000]

labels_story_50 = dd.from_pandas(labels_story_50, npartitions=3)

meta_df = pd.DataFrame(columns=["id", "label_id", "message", "user_id", "created_at",
                                   "action", "action_id", "recipient", "user_info_id", "is_viewed"])

labels_story_50.apply(lambda row: row_handler(row), meta=meta_df, axis=1)

print(df_ok_rows)