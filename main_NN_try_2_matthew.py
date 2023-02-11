import pandas as pd
import xgboost
import numpy as np
from xgboost import plot_importance
from matplotlib import pyplot
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error

numeric_features = ["procentage"]

PATH = "/Users/matthewpopov/Desktop/clean_database/dataset.csv"

df = pd.read_csv(PATH, encoding="utf-8")

X = df.drop(["item_id", "number_of_sales", "date", "Unnamed: 0", "is_day_off", "season", "day_of_week_sin",
             "day_of_week_cos"], axis=1)

y = df["number_of_sales"]

X = pd.get_dummies(X, columns=["product_type", "day_of_week_number"])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=40)

X_train[numeric_features] = np.log1p(X_train[numeric_features])

X_test[numeric_features] = np.log1p(X_test[numeric_features])

model = xgboost.XGBRegressor(n_estimators=10000, max_depth=15)

model.fit(X_train, y_train)

pred = model.predict(X_test)

pred_data = pd.DataFrame(X_test)

pred_data["y_true"] = y_test
pred_data["y_pred"] = np.abs(pred)

print(mean_absolute_error(y_test, np.abs(pred)))

print(pred_data["tavg"])

pred_data.to_csv("/Users/matthewpopov/Desktop/clean_database/pred.csv")
