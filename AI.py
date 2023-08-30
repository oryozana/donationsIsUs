# imports
from os.path import exists
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import roc_auc_score
import xgboost as xgb

import Consts

AI_MODEL_NAME = "model.json"


def train_ai_model_if_needed() -> None:
    """
    Train an AI model if needed.
    :return: None
    """

    def is_ai_trained() -> bool:
        return exists(AI_MODEL_NAME)

    if not is_ai_trained():
        train_ai_model()


def train_ai_model():
    def data_preprocessing():
        data = pd.read_csv("train_data.csv")
        data = data.drop("Ethnicity", axis=1)
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


def does_earn_more_than_7000_dollars():
    def data_preprocessing():
        test_data = pd.concat([pd.read_csv(Consts.TEST_FILE_NAME), pd.read_csv("test_data.csv")])
        test_data = test_data.drop("Ethnicity", axis=1)
        return min_max_scaler(test_data)

    def min_max_scaler(test_data):
        scaler = MinMaxScaler()
        for i in test_data.select_dtypes(include=np.number).columns.tolist():
            col = np.array(test_data[i]).reshape(-1, 1)
            scaler.fit(col)
            test_data[i] = scaler.transform(col)
        return label_encoder(test_data)

    def label_encoder(test_data):
        l = LabelEncoder()
        test_data['WorkingCondition'] = l.fit_transform(test_data['WorkingCondition'])
        test_data['Education'] = l.fit_transform(test_data['Education'])
        test_data['MaritalStatus'] = l.fit_transform(test_data['MaritalStatus'])
        test_data['Occupation'] = l.fit_transform(test_data['Occupation'])
        test_data['Relationship'] = l.fit_transform(test_data['Relationship'])
        test_data['Gender'] = l.fit_transform(test_data['Gender'])
        test_data['CountryOfOrigin'] = l.fit_transform(test_data['CountryOfOrigin'])
        test_data.head()
        return test_the_model(test_data)

    def test_the_model(test_data):
        dtest = xgb.DMatrix(test_data.values)

        model = xgb.Booster()
        model.load_model(AI_MODEL_NAME)

        y_pred = model.predict(dtest)

        return round(y_pred[0]) == 1

    return data_preprocessing()


train_ai_model_if_needed()
