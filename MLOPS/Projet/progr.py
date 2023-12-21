from infrastructure.importation import load_data
from preparation.transfo import *
from preparation.feature_engineering import *
from modeling.train_test import *
from modeling.model import *
import pandas as pd

data = load_data()

data = drop_na(data)
data = borne_age(data)
data = borne_heures(data)
data = borne_capital_gain(data)
data = borne_capital_loss(data)
data = regroupement(data)
data = sal_dummies(data)

data = supp_colonne(data)

X_train, X_test, y_train, y_test = train_test(data)

model = fit_logistic_regression(X_train, y_train)
preds = predict_logistic_regression(model, X_test)

df_preds = pd.DataFrame(preds)

df_preds.to_csv("data/preds.csv")