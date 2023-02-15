import pandas as pd
from imblearn.over_sampling import SMOTENC
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


from imblearn.over_sampling import SMOTENC, SMOTE


def col_ins(df, features):
    # column names to indices
    return [df.columns.get_loc(col) for col in features]


classification_dataset = pd.read_csv("/Users/matthewpopov/Desktop/clean_database/classification_dataset.csv",
                                     encoding="utf-8")

classification_dataset = classification_dataset.drop(["Unnamed: 0"], axis=1)

#  ['date', 'item_id', 'procentage', 'number_of_sales', 'tavg', 'season', 'day_of_week_cos',
#  'product_type', 'day_of_month', 'month', 'day_of_week', 'is_day_off', 'is_anomaly']

numerical_features = ["procentage", "tavg", "number_of_sales"]
categorical_features = ["season", "product_type", "day_of_month", "month", "day_of_week",
                      "is_anomaly"]

needed_features = numerical_features + categorical_features

# scaler = StandardScaler()
#
# scaled_num_features = pd.DataFrame(scaler.fit_transform(classification_dataset[numerical_features]),
#                                    columns=numerical_features)
#
# classification_dataset[numerical_features] = scaled_num_features

X = classification_dataset[needed_features]

y = X["is_anomaly"]

X = pd.get_dummies(X, columns=categorical_features)

categorical_features = ['season_1', 'season_2', 'season_3', 'season_4', 'product_type_ДРУГОЕ',
                        'product_type_ЙОГУРТ', 'product_type_КЕФИР', 'product_type_МАСЛО', 'product_type_МОЛОКО',
                        'product_type_МОРОЖЕНОЕ', 'product_type_СЛИВКИ', 'product_type_СЫР', 'product_type_ТВОРОГ',
                        'day_of_month_1', 'day_of_month_2', 'day_of_month_3', 'day_of_month_4', 'day_of_month_6',
                        'day_of_month_7', 'day_of_month_8', 'day_of_month_9', 'day_of_month_10', 'day_of_month_11',
                        'day_of_month_12', 'day_of_month_13', 'day_of_month_14', 'day_of_month_15', 'day_of_month_16',
                        'day_of_month_17', 'day_of_month_18', 'day_of_month_19', 'day_of_month_26', 'day_of_month_28',
                        'day_of_month_29', 'day_of_month_30', 'day_of_month_31', 'month_2', 'month_3', 'month_4',
                        'month_5', 'month_6', 'month_7', 'month_8', 'month_10', 'month_11', 'month_12', 'day_of_week_1',
                        'day_of_week_2', 'day_of_week_3', 'day_of_week_4', 'day_of_week_5', 'day_of_week_6',
                        'day_of_week_7', 'is_anomaly_1']


smoteNC = SMOTENC(categorical_features=col_ins(X, categorical_features), random_state=42)

X_resampled, y_resempled = smoteNC.fit_resample(X, y)


X_resampled = X_resampled.sample(frac=1)


df = pd.read_csv("/Users/matthewpopov/Desktop/clean_database/resampled_df.csv", encoding="utf-8")

df = df.drop(["Unnamed: 0"], axis=1)

print(df)

big_sales = df.loc[df["number_of_sales"] > 100]

print(big_sales)

big_sales.to_csv("/Users/matthewpopov/Desktop/clean_database/resampled_big_sales_df.csv")
