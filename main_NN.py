import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error
from sklearn.metrics import accuracy_score

label_encoder = LabelEncoder()

df = pd.read_csv("/Users/matthewpopov/Desktop/clean_database/dataset_WNCF.csv", encoding="utf-8")

X = df.drop(["item_id", "number_of_sales", "Unnamed: 0", "date"], axis=1)

y = df["number_of_sales"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=228)

y_train = label_encoder.fit_transform(y_train)

X_train["is_day_off"] = X_train["is_day_off"].astype("category")
X_train["season"] = X_train["season"].astype("category")
X_train["num_type"] = X_train["num_type"].astype("category")

X_train["is_day_off"] = pd.to_numeric(X_train["is_day_off"])
X_train["season"] = pd.to_numeric(X_train["season"])
X_train["num_type"] = pd.to_numeric(X_train["num_type"])

#  test dataset
X_test["num_type"] = X_test["num_type"].astype("category")
X_test["is_day_off"] = X_test["is_day_off"].astype("category")
X_test["season"] = X_test["season"].astype("category")

X_test["is_day_off"] = pd.to_numeric(X_test["is_day_off"])
X_test["season"] = pd.to_numeric(X_test["season"])
X_test["num_type"] = pd.to_numeric(X_test["num_type"])

model = xgb.XGBRegressor(n_estimators=1000, max_depth=7)

model.fit(X_train, y_train)

prediction = model.predict(X_test)

print(X_test)

print(prediction)

mse = mean_squared_error(y_test, prediction)

print(mse)