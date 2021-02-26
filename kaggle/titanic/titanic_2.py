import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import MinMaxScaler, StandardScaler

plt.style.use('fivethirtyeight')
sns.set(style='whitegrid', color_codes=True)

# for root, directory, file in os.walk("C:\\Users\\Asus\\PycharmProjects\\kaggle"):
#     for f in file:
#         print(os.path.join(root, f))

train_data = pd.read_csv("train.csv")
test_data = pd.read_csv("test.csv")

df = train_data.copy()
df2 = test_data.copy()


# df.Sex = df.Sex.apply(lambda x: 1 if x == "male" else 0)
# df2.Sex = df2.Sex.apply(lambda x: 1 if x == "male" else 0)
#
# df.Embarked = df.Embarked.apply(lambda x: 1 if x == "C" else (2 if x == "Q" else 3))
# df2.Embarked = df2.Embarked.apply(lambda x: 1 if x == "C" else (2 if x == "Q" else 3))


df.Age.fillna(df.Age.mean(), inplace=True)
df2.Age.fillna(df2.Age.mean(), inplace=True)

df2.Fare.fillna(df2.Fare.mean(), inplace=True)

X = pd.get_dummies(df.drop(columns=["Name", "Cabin", "Survived", "Ticket"]))

y = df.Survived
X_test = pd.get_dummies(df2.drop(columns=["Name", "Cabin", "Ticket"]))

model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
model.fit(X, y)
y_pred = model.predict(X_test)

output = pd.DataFrame({'PassengerId': df2.PassengerId, "Survived": y_pred})
output.to_csv('my_submission2.csv', index=False)
