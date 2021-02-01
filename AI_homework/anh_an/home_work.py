import re
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.model_selection import KFold, StratifiedKFold, LeaveOneOut, LeavePOut
from sklearn.metrics import mean_absolute_error, mean_squared_error


df = pd.read_csv("advertising.csv", delimiter=",")

x = df[["TV", "Radio", "Newspaper"]]
y = df["Sales"]

score = []
kf = KFold(n_splits=10, shuffle=True, random_state=42)
for train_index, test_index in kf.split(x, y):
    x_train, x_test = x.iloc[train_index], x.iloc[test_index]
    y_train, y_test = y.iloc[train_index], y.iloc[test_index]
    sc = StandardScaler().fit(x_train)
    x_train_sc = sc.transform(x_train)
    x_test_sc = sc.transform(x_test)
    clf = LinearRegression().fit(x_train_sc, y_train)
    score.append(clf.score(x_test_sc, y_test))
print(np.mean(score))

score = []
skf = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)
# stratified is for binary values and multiclass only
for train_index, test_index in skf.split(x, np.zeros(y.shape[0])):
    x_train, x_test = x.iloc[train_index], x.iloc[test_index]
    y_train, y_test = y.iloc[train_index], y.iloc[test_index]

    sc = StandardScaler().fit(x_train)
    x_train_sc = sc.transform(x_train)
    x_test_sc = sc.transform(x_test)
    clf = LinearRegression().fit(x_train_sc, y_train)
    score.append(clf.score(x_test_sc, y_test))
print(np.mean(score))

score = []
loo = LeaveOneOut()
# stratified is for binary values and multiclass only
for train_index, test_index in loo.split(x):
    x_train, x_test = x.iloc[train_index], x.iloc[test_index]
    y_train, y_test = y.iloc[train_index], y.iloc[test_index]

    clf = LinearRegression().fit(x_train, y_train)
    y_pred = clf.predict(x_test)
    score.append(mean_absolute_error(y_test, y_pred))

# print(np.mean(score))
# clf = LinearRegression()
# print(cross_val_score(clf, x, y, cv=x.shape[0]))
# khi chay dong tren se bi loi ben duoi => leave one out khong hieu qua vs large data
# UndefinedMetricWarning: R ^ 2 score is not well - defined with less than two samples

score = []
lpo = LeavePOut(2)
for train_index, test_index in lpo.split(x, np.zeros(y.shape[0])):
    x_train, x_test = x.iloc[train_index], x.iloc[test_index]
    y_train, y_test = y.iloc[train_index], y.iloc[test_index]
    clf = LinearRegression().fit(x_train, y_train)
    score.append(clf.score(x_test, y_test))
print(np.mean(score))
# leave p out cung giong leaveoneout: cuc ki kem hieu qua khi lam viec voi large dataset
#  thu vs p==2 => co nhung truong hop predict tot co nhung truong hop predict rat te
#  thu vs p==20 => tinh rat lau, 200 rows ma da nhu the nay thi qua khong hieu qua

