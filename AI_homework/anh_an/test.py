import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
import pylab as pl
from sklearn.model_selection import LeaveOneOut
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn import linear_model
data = pd.read_csv('advertising.csv')
x = data[['TV', 'Radio', 'Newspaper']]
y = data['Sales']
loo = LeaveOneOut()
for train_index, test_index in loo.split(x):
    x_train, x_test = x.iloc[train_index], x.iloc[test_index]
    y_train, y_test = y.iloc[train_index], y.iloc[test_index]
    regr = linear_model.LinearRegression()
    regr.fit(x_train, y_train)
    ypred = regr.predict(x_test)
    print(mean_absolute_error(y_test, ypred))
