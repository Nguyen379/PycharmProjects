import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

train = pd.read_csv("analyzed_train.csv")
test = pd.read_csv("analyzed_test.csv")
# tỉ lệ clicked: not clicked = 1:4 => unbalanced.
# tạo file mới từ file cũ có tỉ lệ clicked: not clicked = 1:1. Dùng gridsearch để tìm feature quan trọng.

pre_X = train[train["click"] == 0].sample(n=len(train[train["click"] == 1]), random_state=42)
# lay 1 luong not clicked = clicked
pre_X = pd.concat([pre_X, train[train["click"] == 1]]).sample(frac=1)
pre_y = pre_X[["click"]].values.ravel()
pre_X.drop(["click"], axis=1, inplace=True)
test.drop(["click"], axis=1, inplace=True)

import lightgbm as lgb
from sklearn.model_selection import GridSearchCV, train_test_split

pre_X_train, pre_X_test, pre_y_train, pre_y_test = train_test_split(pre_X, pre_y, test_size=0.2, stratify=pre_y,
                                                                    random_state=42)

# ti le clicked unbalanced => dung un_balanced hoac chia ra r tim gridsearch trc

# TESTED_PARAMS = {"learning_rate": np.arange(0.05, 0.5, 0.05),
#                  "max_depth": [1, 6, 11, 16, 21, 26, 31]}
# clf = lgb.LGBMClassifier(boosting_type="goss",
#                          is_unbalance=True,
#                          objective="binary",
#                          n_estimators=300,
#                          max_bin=255,
#                          num_leaves=511,
#                          metric="binary_logloss")
# grid_search = GridSearchCV(clf, param_grid=TESTED_PARAMS, scoring="roc_auc", cv=50, verbose=1, n_jobs=-1)
# grid_search.fit(pre_X_train, pre_y_train)

# print(grid_search.best_params_) {'learning_rate': 0.05, 'max_depth': 6}
# print(grid_search.best_estimator_)
# LGBMClassifier(boosting_type='goss',
#                is_unbalance=True,
#                learning_rate=0.05,
#                max_bin=255,
#                max_depth=6,
#                metric='binary_logloss',
#                n_estimators=300,
#                num_leaves=511,
#                objective='binary')
# print(grid_search.best_score_) 0.7316138940393835


# clf = lgb.LGBMClassifier(boosting_type="goss",
#                          is_unbalance=True,
#                          objective="binary",
#                          n_estimators=300,
#                          max_bin=255,
#                          metric="binary_logloss",
#                          max_depth=6)
#
# clf.fit(pre_X, pre_y)
# feature_importances = pd.DataFrame(clf.feature_importances_)
# feature_importances.index = pre_X.columns
# feature_importances.sort_values(feature_importances.columns[0], axis=0, ascending=False, inplace=True)
# print(feature_importances)
#
# pre_X_train = pre_X_train[feature_importances.index[:int(len(feature_importances)/3)]]
# pre_X_test = pre_X_test[feature_importances.index[:int(len(feature_importances)/3)]]


# TESTED_PARAMS = {"learning_rate": np.arange(0.01, 0.11, 0.01),
#                  "num_leaves": [127, 255, 511, 1023]}
# grid_search = GridSearchV(clf, param_grid=TESTED_PARAMS, scoring="roc_auc", cv=100, verbose=1, n_jobs=-1)
# grid_search.fit(pre_X_train, pre_y_train)
#
# print(grid_search.best_params_)
# print(grid_search.best_estimator_)
# print(grid_search.best_score_)
# {'learning_rate': 0.02, 'num_leaves': 127}
# LGBMClassifier(boosting_type='goss', is_unbalance=True, learning_rate=0.02,
#                max_bin=255, max_depth=6, metric='binary_logloss',
#                n_estimators=300, num_leaves=127, objective='binary')
# 0.7042741730132969

clf = lgb.LGBMClassifier(boosting_type='goss',
                         learning_rate=0.1,
                         max_depth=11,
                         metric='binary_logloss',
                         n_estimators=500,
                         num_leaves=511,
                         objective='binary')

clf.fit(pre_X, pre_y)
feature_importances = pd.DataFrame(clf.feature_importances_)
feature_importances.index = pre_X.columns
feature_importances = feature_importances.sort_values(feature_importances.columns[0], ascending=False)
print(feature_importances)
cols = feature_importances[feature_importances[feature_importances.columns[0]] > 150]
print(cols)


from sklearn.metrics import roc_auc_score, confusion_matrix

feature_len = len(cols)
# un_balance=True

X_train = train[feature_importances[:feature_len].index]
y_train = train[["click"]].values.ravel()
X_test = test[feature_importances[:feature_len].index]

clf = lgb.LGBMClassifier(boosting_type='goss',
                         is_unbalance=True,
                         learning_rate=0.02,
                         max_bin=255,
                         max_depth=6,
                         metric='binary_logloss',
                         n_estimators=300,
                         num_leaves=127,
                         objective='binary')

clf.fit(X_train, y_train)
y_pred = clf.predict(X_train)
print(roc_auc_score(y_train, y_pred) * 100)

confmat = confusion_matrix(y_true=y_train, y_pred=y_pred, labels=[0, 1])
fig, ax = plt.subplots(figsize=(2.5, 2.5))
ax.matshow(confmat, cmap=plt.cm.Blues, alpha=0.3)
for i in range(confmat.shape[0]):
    for j in range(confmat.shape[1]):
        ax.text(x=j, y=i, s=confmat[i, j], va="center", ha="center")

plt.xlabel("Predicted")
plt.ylabel("True")
plt.tight_layout()

submission = pd.read_csv("sampleSubmission.csv")
submission[submission.columns[1]] = clf.predict_proba(X_test)[:, 1]
submission.to_csv("submission_lightgbm.csv", index=False)
plt.show()
# site_id_very_low        0.410412
# app_id_very_high        0.171345
# site_id_very_high       0.074036
# app_id_very_low         0.066942
# app_category_high       0.064936
# C16_250                 0.033630
# C18_1                   0.023407
# device_model_very_high  0.020505
# site_domain_very_low    0.013967
# device_model_low        0.013492
# device_model_very_low   0.011123
# site_category_high      0.010360
# banner_pos_0            0.007240
# C18_2                   0.006909
# site_id_high            0.006498
# device_conn_type_0      0.005360
# hour_17-19              0.005260
# hour_19-21              0.005151
# C15_216                 0.004563
# C18_3                   0.004517
# banner_pos_1            0.004416
# app_domain_low          0.004005
# site_category_mid       0.003578
# weekday_2               0.003395
# device_conn_type_2      0.003371
# weekday_3               0.003258
# device_ip_mid           0.003227
# hour_21-23              0.003029
# app_id_low              0.002762
# device_ip_very_high     0.002712
# C1_1012                 0.002375
# device_ip_very_low      0.002294
# app_domain_very_high    0.001928

# site_id_very_low        0.410412
# app_id_very_high        0.171345
# site_id_very_high       0.074036
# app_id_very_low         0.066942
# app_category_high       0.064936
# C16_250                 0.033630
# C18_1                   0.023407
# device_model_very_high  0.020505
# site_domain_very_low    0.013967
# device_model_low        0.013492
# device_model_very_low   0.011123
# site_category_high      0.010360
# banner_pos_0            0.007240
# C18_2                   0.006909
# site_id_high            0.006498
# device_conn_type_0      0.005360
# hour_17-19              0.005260
# hour_19-21              0.005151
