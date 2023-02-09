import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split

df = pd.read_csv("/Users/matthewpopov/Desktop/clean_database/dataset.csv", encoding="utf-8")

df.info()
