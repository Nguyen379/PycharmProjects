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

# print(df.isnull().any())
# print(df["Cabin"].value_counts(dropna=False))
# print(df["Cabin"].count() / len(df["Cabin"]))
# nen xem xet bo cabin vi qua it du lieu
# print(df["Embarked"].count() / len(df["Embarked"]))
# print(df["Age"].count() / len(df["Age"]))

df.Sex = df.Sex.apply(lambda x: 1 if x == "male" else 0)
df2.Sex = df2.Sex.apply(lambda x: 1 if x == "male" else 0)

df.Embarked = df.Embarked.apply(lambda x: 1 if x == "C" else (2 if x == "Q" else 3))
df2.Embarked = df2.Embarked.apply(lambda x: 1 if x == "C" else (2 if x == "Q" else 3))


df.Age.fillna(df.Age.mean(), inplace=True)
df2.Age.fillna(df2.Age.mean(), inplace=True)

df2.Fare.fillna(df2.Fare.mean(), inplace=True)


# df_cor = df.drop(columns=["Name", "Ticket", "Cabin", "Embarked"]).corr()
# df.drop(columns=["Name", "Ticket", "Cabin", "Embarked"], inplace=True).corr()
# mask = np.array(df_cor)
# mask[np.tril_indices_from(mask)] = False
# sns.heatmap(data=df_cor, mask=mask, square=True, annot=True)
# plt.legend()
# plt.show()

# print(df.iloc[:, 1:5])
# ":": all rows, "1:5": column 1 to 5

def calc_limit(feature):
    down, up = df[feature].quantile([0.25, 0.75])
    iqr = up - down
    return down - 1.5 * iqr, up + 1.5 * iqr


def plot(feature):
    sns.boxplot(data=df, x=feature)
    down, up = calc_limit(feature)
    print(len(df[(df[feature] > down) & (df[feature] < up)]))
    plt.legend()
    plt.show()


X = df.drop(columns=["Name", "Cabin", "Survived", "Ticket"])
y = df.Survived
X_test = df2.drop(columns=["Name", "Cabin", "Ticket"])

model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
model.fit(X, y)
y_pred = model.predict(X_test)

output = pd.DataFrame({'PassengerId': df2.PassengerId, "Survived": y_pred})
output.to_csv('my_submission.csv', index=False)
