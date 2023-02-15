import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score
import matplotlib.pyplot as plt


def get_classifier():
    df = pd.read_csv("/Users/matthewpopov/Desktop/clean_database/resampled_df.csv", encoding="utf-8")

    X = df.drop(["Unnamed: 0", "is_anomaly", "number_of_sales"], axis=1)

    y = df["is_anomaly"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=20)

    model = XGBClassifier(n_estimators=100, max_depth=7)

    model.fit(X_train, y_train)

    return model, X_test, y_test, X_train, y_train


model, X_test, y_test, X_train, y_train = get_classifier()


prediction = model.predict(X_test)

print(prediction)
print(X_test)

print(accuracy_score(y_test, prediction))

model.save_model("/Users/matthewpopov/Desktop/clean_database/models/anomaly_classifier.json")



