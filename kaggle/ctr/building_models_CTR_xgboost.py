import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

train = pd.read_csv("analyzed_train.csv")
test = pd.read_csv("analyzed_test.csv")
# tỉ lệ clicked: not clicked = 1:4 => unbalanced.
# tạo file mới từ file cũ có tỉ lệ clicked: not clicked = 1:1. Dùng gridsearch để tìm feature quan trọng.

pre_X = train[train["click"] == 0].sample(n=len(train[train["click"] == 1]), random_state=42)
# lay 1 luong not clicked = clicked
pre_X = pd.concat([pre_X, train[train["click"] == 1]]).sample(frac=1)
pre_y = pre_X[["click"]]
pre_X.drop(["click"], axis=1, inplace=True)
test.drop(["click"], axis=1, inplace=True)

from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import roc_auc_score
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

pre_X_train, pre_X_test, pre_y_train, pre_y_test = train_test_split(pre_X, pre_y, test_size=0.2, stratify=pre_y,
                                                                    random_state=42)

# params = {"criterion": ["gini", "entropy"], "max_depth": range(1, 20)}
# grid_search=GridSearchCV(DecisionTreeClassifier(), param_grid=params, scoring="roc_auc", cv=100, verbose=1, n_jobs=-1)
# grid_search.fit(pre_X_train, pre_y_train)
# print(grid_search.best_score_)
# print(grid_search.best_estimator_) DecisionTreeClassifier(criterion='entropy', max_depth=11)
# print(grid_search.best_params_)

tree = DecisionTreeClassifier(criterion="entropy", max_depth=11)
tree.fit(pre_X, pre_y)
feature_importances = pd.DataFrame(tree.feature_importances_)
feature_importances.index = pre_X_train.columns
feature_importances.sort_values(0, ascending=False, inplace=True)
print(feature_importances)

pre_X_train = pre_X_train[feature_importances.index[:int(len(feature_importances) / 3)]]
pre_X_test = pre_X_test[feature_importances.index[:int(len(feature_importances) / 3)]]

# params = {"criterion": ["gini", "entropy"], "max_depth": range(1, 12)}
# grid_search=GridSearchCV(DecisionTreeClassifier(), param_grid=params, scoring="roc_auc", cv=100, verbose=1, n_jobs=-1)
# grid_search.fit(pre_X_train, pre_y_train)
# print(grid_search.best_score_)
# print(grid_search.best_estimator_)
# print(grid_search.best_params_)

pre_X = pre_X[feature_importances.index[:int(len(feature_importances) / 3)]]
tree = DecisionTreeClassifier(criterion='entropy', max_depth=11)
tree.fit(pre_X, pre_y)
feature_importances = pd.DataFrame(tree.feature_importances_)
feature_importances.index = pre_X_train.columns
feature_importances = feature_importances.sort_values(0, ascending=False)
print(feature_importances)

feature_len = len(feature_importances[feature_importances[feature_importances.columns[0]] > 0.005])
print(feature_len)
print(feature_importances[:feature_len])
y = train[["click"]]
X = train[feature_importances[:feature_len].index]
test = test[feature_importances[:feature_len].index]

from xgboost import XGBClassifier

model = XGBClassifier(tree_method="gpu_hist", n_jobs=-1, n_estimators=500, max_depth=11)
model.fit(X, y.values.ravel())
y_pred = model.predict(X)
print(roc_auc_score(y, y_pred) * 100)

confmat = confusion_matrix(y_true=y, y_pred=y_pred, labels=[0, 1])
fig, ax = plt.subplots(figsize=(2.5, 2.5))
ax.matshow(confmat, cmap=plt.cm.Blues, alpha=0.3)
for i in range(confmat.shape[0]):
    for j in range(confmat.shape[1]):
        ax.text(x=j, y=i, s=confmat[i, j], va="center", ha="center")
# sns.heatmap(confmat, annot=True)

plt.xlabel("Predicted")
plt.ylabel("True")
plt.tight_layout()

submission = pd.read_csv("sampleSubmission.csv")
submission[submission.columns[1]] = model.predict_proba(test)[:, 1]
submission.to_csv("submission.csv", index=False)
plt.show()
