import pandas as pd

final_milk_data_1 = pd.read_csv("/Users/nikolamuravev/Desktop/result/test.csv", encoding="utf-8",
                        on_bad_lines="skip")
final_milk_data_2 = pd.read_csv("/Users/nikolamuravev/Desktop/result/final_data_updated.csv", encoding="utf-8",
                        on_bad_lines="skip")

df = pd.DataFrame(final_milk_data_1)

def check_for_uniq_lines(row):
    new_date = row["date"]
    new_id_of_item = row["item_id"]
    new_number_of_sales = row["number_of_sales"]
    uniq_check = df.loc[(df["date"] == new_date) & (df["item_id"] == new_id_of_item)]
    uniq_check_len = len(uniq_check)
    if uniq_check_len != 0:
        uniq_index = int(str(uniq_check["date"]).split("    ")[0])
        df.loc[uniq_index, "number_of_sales"] += new_number_of_sales
    else:
        df.loc[len(df)] = row

final_milk_data_2.apply(lambda row: check_for_uniq_lines(row), axis=1)
#удаляю первую строку, которая нумерует строки
del df[df.columns[0]]
del df[df.columns[0]]
print(df)
df.to_csv("/Users/nikolamuravev/Desktop/result/best_dataframe.csv")