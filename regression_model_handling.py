import pandas as pd
import xgboost
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error


def get_model(path, n_estimators, max_depth, test_size, random_state):

    df = pd.read_csv(path, encoding="utf-8")

    X = df.drop(["Unnamed: 0"], axis=1)

    y = df["number_of_sales"]

    # X = pd.get_dummies(X, columns=["product_type", "day_of_week"])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    model = xgboost.XGBRegressor(n_estimators=n_estimators, max_depth=max_depth)

    model.fit(X_train, y_train)

    return model, X_test, y_test


def describe_model(path, name_of_model, n_estimators, max_depth, test_size, random_state):
    model, X_test, y_test = get_model(path, n_estimators, max_depth, test_size, random_state)
    pred = model.predict(X_test)

    pred_data = pd.DataFrame(X_test)

    pred_data["y_true"] = y_test
    pred_data["y_pred"] = np.abs(pred)

    print(f"{name_of_model}'s MAE = {mean_absolute_error(y_test, np.abs(pred))}")

    # if name_of_model == "Big Sales Model":
    #     pred_data.to_csv("/Users/matthewpopov/Desktop/clean_database/pred_BIG_sales_data.csv")
    # elif name_of_model == "Small Sales Model":
    #     pred_data.to_csv("/Users/matthewpopov/Desktop/clean_database/pred_SMALL_sales_data.csv")


describe_model("/Users/matthewpopov/Desktop/clean_database/resampled_small_sales_df.csv", "Small Sales Model", 500, 6, 0.1,
               12)

describe_model("/Users/matthewpopov/Desktop/clean_database/resampled_big_sales_df.csv", "Big Sales Model", 500, 8, 0.2, 11)


# df = pd.read_csv("/Users/matthewpopov/Desktop/clean_database/resampled_classification_df.csv", encoding="utf-8")
# df = df.drop(["Unnamed: 0"], axis=1)



