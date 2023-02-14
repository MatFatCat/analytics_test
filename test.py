import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

df = pd.read_csv("/Users/matthewpopov/Desktop/clean_database/resampled_classification_df.csv", encoding="utf-8")

df = df.drop(["Unnamed: 0"], axis=1)

categories = ['season_1', 'season_2', 'season_3', 'season_4', 'product_type_ДРУГОЕ', 'product_type_ЙОГУРТ',
              'product_type_КЕФИР', 'product_type_МАСЛО', 'product_type_МОЛОКО', 'product_type_МОРОЖЕНОЕ',
              'product_type_СЛИВКИ', 'product_type_СМЕТАНА', 'product_type_СЫР', 'product_type_ТВОРОГ',
              'day_of_month_1', 'day_of_month_2', 'day_of_month_3', 'day_of_month_4', 'day_of_month_5',
              'day_of_month_6', 'day_of_month_7', 'day_of_month_8', 'day_of_month_9', 'day_of_month_10',
              'day_of_month_11', 'day_of_month_12', 'day_of_month_13', 'day_of_month_14', 'day_of_month_15',
              'day_of_month_16', 'day_of_month_17', 'day_of_month_18', 'day_of_month_19', 'day_of_month_20',
              'day_of_month_21', 'day_of_month_22', 'day_of_month_23', 'day_of_month_24', 'day_of_month_25',
              'day_of_month_26', 'day_of_month_27', 'day_of_month_28', 'day_of_month_29', 'day_of_month_30',
              'day_of_month_31', 'month_1', 'month_2', 'month_3', 'month_4', 'month_5', 'month_6', 'month_7',
              'month_8', 'month_9', 'month_10', 'month_11', 'month_12', 'day_of_week_1', 'day_of_week_2',
              'day_of_week_3', 'day_of_week_4', 'day_of_week_5', 'day_of_week_6', 'day_of_week_7']

season_columns = categories[0:4]

product_type_columns = categories[4:14]

day_of_month_column = categories[14:45]

month_column = categories[45:57]

day_of_week_column = categories[57:64]

groups = [season_columns, product_type_columns,
          day_of_month_column, month_column, day_of_week_column]


def check_zero_in_column(column_group_name, df):
    results = []
    for index, row in df.iterrows():
        if not sub_check_zero_in_column(row, column_group_name):
            results.append(row)

    return results


def sub_check_zero_in_column(row, column_group_name):
    result = False
    for column in column_group_name:
        if row[column] != 0:
            result = True
            break

    if result is False:
        return False
    else:
        return True


df_big_sales_resampled = df.loc[df["number_of_sales"] > 100]

df_small_sales_resampled = df.loc[df["number_of_sales"] <= 100]

# df_small_sales_resampled.to_csv("/Users/matthewpopov/Desktop/clean_database/df_small_sales_resampled.csv")

big_season_1 = df_big_sales_resampled.loc[df["season_1"] == 1]
big_season_2 = df_big_sales_resampled.loc[df["season_2"] == 1]
big_season_3 = df_big_sales_resampled.loc[df["season_3"] == 1]
big_season_4 = df_big_sales_resampled.loc[df["season_4"] == 1]

for index, row in df_big_sales_resampled.iterrows():
    if not sub_check_zero_in_column(row, day_of_month_column):
        df_big_sales_resampled.loc[index, f"day_of_month_{random.choice(range(1, 32))}"] = 1

# for index, row in df_big_sales_resampled.iterrows():
#     if not sub_check_zero_in_column(row, month_column):
#
#         if row["season_1"] == 1:
#             df_big_sales_resampled.loc[index, f"month_{random.choice(range(1, 3))}"] = 1
#         elif row["season_2"] == 1:
#             df_big_sales_resampled.loc[index, f"month_{random.choice(range(3, 6))}"] = 1
#         elif row["season_3"] == 1:
#             df_big_sales_resampled.loc[index, f"month_{random.choice(range(6, 9))}"] = 1
#         else:
#             df_big_sales_resampled.loc[index, f"month_{random.choice(range(9, 13))}"] = 1

print(len(check_zero_in_column(day_of_month_column, df_big_sales_resampled)))

data = pd.concat([df_big_sales_resampled, df_small_sales_resampled])

data = data.sample(frac=1)

data.to_csv("/Users/matthewpopov/Desktop/clean_database/resampled_classification_df.csv")


# for index, row in df_big_sales_resampled.iterrows():
#     season = 0
#     if row["season_1"] == 1:
#         season = 1
#     elif row["season_2"] == 1:
#         season = 2
#     elif row["season_3"] == 1:
#         season = 1
#     else:
#         season = 4
#
#     if not sub_check_zero_in_column(row, product_type_columns):
#         prod_types = ['product_type_ДРУГОЕ', 'product_type_ЙОГУРТ',
#                       'product_type_КЕФИР', 'product_type_МАСЛО', 'product_type_МОЛОКО', 'product_type_МОРОЖЕНОЕ',
#                       'product_type_СЛИВКИ', 'product_type_СМЕТАНА', 'product_type_СЫР', 'product_type_ТВОРОГ']
#
#         if season == 1:
#             column = random.choices(prod_types, weights=[0.0725, 0.0725, 0.0725, 0.0725, 0.3, 0.0725, 0.0725,
#                                                          0.0725, 0.12, 0.0725])
#             df_big_sales_resampled.loc[index, column] = 1
#         elif season == 2:
#             column = random.choices(prod_types, weights=[0.0725, 0.0725, 0.0725, 0.0725, 0.3, 0.0725, 0.0725,
#                                                          0.0725, 0.12, 0.0725])
#             df_big_sales_resampled.loc[index, column] = 1
#         elif season == 3:
#             column = random.choices(prod_types, weights=[0.0725, 0.0725, 0.0725, 0.0725, 0.3, 0.0725, 0.0725,
#                                                          0.0725, 0.12, 0.0725])
#             df_big_sales_resampled.loc[index, column] = 1
#         else:
#             column = random.choices(prod_types, weights=[0.0714285714, 0.0714285714, 0.0714285714, 0.0714285714, 0.2,
#                                                          0.0714285714, 0.0714285714, 0.0725, 0.1, 0.2])
#             df_big_sales_resampled.loc[index, column] = 1





# data = pd.concat([df_big_sales_resampled, df_small_sales_resampled])
#
# data = data.sample(frac=1)
#
# data.to_csv("/Users/matthewpopov/Desktop/clean_database/resampled_classification_df-AFTER.csv")

# resampled_classification_df.to_csv("/Users/matthewpopov/Desktop/clean_database/resampled_classification_df.csv")