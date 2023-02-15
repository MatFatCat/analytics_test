import pandas as pd
import xgboost


def make_prediction(X, big_sales_regression_model, small_sales_regression_model, anomaly_classifier_model):
    is_anomaly = anomaly_classifier_model.predict(X)

    if is_anomaly[0] == 1:
        prediction = big_sales_regression_model.predict(X)
    else:
        prediction = small_sales_regression_model.predict(X)

    return prediction


if __name__ == "__main__":
    df = pd.read_csv("/Users/matthewpopov/Desktop/clean_database/resampled_df.csv", encoding="utf-8")
    df = df.drop(["Unnamed: 0", "is_anomaly", "number_of_sales"], axis=1)

    BIG_PATH = "/Users/matthewpopov/Desktop/clean_database/models/big_sales_regression_model.txt"
    SMALL_PATH = "/Users/matthewpopov/Desktop/clean_database/models/small_sales_regression_model.txt"
    ANOMALY_PATH = "/Users/matthewpopov/Desktop/clean_database/models/anomaly_classifier.txt"

    big_sales_regression_model = xgboost.XGBRegressor()
    small_sales_regression_model = xgboost.XGBRegressor()
    anomaly_classifier_model = xgboost.XGBClassifier()

    big_sales_regression_model.load_model(BIG_PATH)
    small_sales_regression_model.load_model(SMALL_PATH)
    anomaly_classifier_model.load_model(ANOMALY_PATH)

    # print(big_sales_regression_model)
    # print(small_sales_regression_model)
    # print(anomaly_classifier_model)
    #
    # print(df.columns.tolist())
    print(df)
    example = df.iloc[[63]]
    print(make_prediction(example, big_sales_regression_model, small_sales_regression_model, anomaly_classifier_model))


