# imports
import pandas as pd
import statistics
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import roc_auc_score
import xgboost as xgb

AI_MODEL_NAME = "model.json"


def train_ai_model():
    def data_preprocessing():
        data = pd.read_csv("train_data.csv")
        data = data.drop("", axis=1)
        min_max_scaler(data.dropna())

    def min_max_scaler(data):
        scaler = MinMaxScaler()
        for i in data.select_dtypes(include=np.number).columns.tolist():
            col = np.array(data[i]).reshape(-1, 1)
            scaler.fit(col)
            data[i] = scaler.transform(col)
        label_encoder(data)

    def label_encoder(data):
        l = LabelEncoder()
        data['WorkingCondition'] = l.fit_transform(data['WorkingCondition'])
        data['Education'] = l.fit_transform(data['Education'])
        data['MaritalStatus'] = l.fit_transform(data['MaritalStatus'])
        data['Occupation'] = l.fit_transform(data['Occupation'])
        data['Relationship'] = l.fit_transform(data['Relationship'])
        data['Ethnicity'] = l.fit_transform(data['Ethnicity'])
        data['Gender'] = l.fit_transform(data['Gender'])
        data['CountryOfOrigin'] = l.fit_transform(data['CountryOfOrigin'])
        data.head()
        split_data(data)

    def split_data(data):
        X = data.drop(["MonthlyIncome"], axis=1).values
        y = data["MonthlyIncome"].values
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        train_the_model(X_train, X_test, y_train, y_test)

    def train_the_model(X_train, X_test, y_train, y_test):
        dtrain = xgb.DMatrix(X_train, label=y_train)
        dtest = xgb.DMatrix(X_test, label=y_test)

        params = {'max_depth': 5, 'eta': 0.1, 'objective': 'binary:logistic'}
        model = xgb.train(params, dtrain, num_boost_round=100)

        y_pred = model.predict(dtest)
        auc = roc_auc_score(y_test, y_pred)
        print("AUC: ", auc)

        model.save_model(AI_MODEL_NAME)

    data_preprocessing()






# test_data = pd.read_csv("test_data.csv")
# num_cols = test_data.select_dtypes(include=np.number).columns.tolist()
#
# scaler = MinMaxScaler()
# for i in num_cols:
#   col = np.array(test_data[i]).reshape(-1, 1)
#   scaler.fit(col)
#   test_data[i] = scaler.transform(col)
#
# l = LabelEncoder()
# test_data['WorkingCondition'] = l.fit_transform(test_data['WorkingCondition'])
# test_data['Education'] = l.fit_transform(test_data['Education'])
# test_data['MaritalStatus'] = l.fit_transform(test_data['MaritalStatus'])
# test_data['Occupation'] = l.fit_transform(test_data['Occupation'])
# test_data['Relationship'] = l.fit_transform(test_data['Relationship'])
# test_data['Ethnicity'] = l.fit_transform(test_data['Ethnicity'])
# test_data['Gender'] = l.fit_transform(test_data['Gender'])
# test_data['CountryOfOrigin'] = l.fit_transform(test_data['CountryOfOrigin'])
# test_data.head()
#
# dtest = xgb.DMatrix(test_data.values)
#
# y_pred = model.predict(dtest)
#
# id = pd.read_csv('test_data.csv')['Id'].values
# df = pd.DataFrame({'id': id, 'MonthlyIncome': y_pred})
# df.to_csv('predictions.csv', index=False)
