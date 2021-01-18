from sklearn.linear_model import SGDClassifier
import re
from sklearn.datasets import load_files
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
import pickle
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC, LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score

reviews = load_files(r"C:\Users\Asus\PycharmProjects\Data Mining - Training"
                     r"\Data_Mining_Training_V6_Week2\combined_for_cross_validation")
files, categories = reviews.data, reviews.target
max_features = []
files_edited = []
# training list
for n in range(0, len(files)):
    file = str(files[n])
    # data stored as bytes => convert to string
    file = re.sub(r'\W', ' ', file)
    # Remove all the special characters
    # file = re.sub(r'\s+[a-zA-Z]\s+', ' ', file)
    # # remove all single characters
    # file = re.sub(r'\s+', '', file, flags=re.I)
    # Substituting multiple spaces with single space
    # file = re.sub(r'^b\s+', '', file)
    # # Removing prefixed 'b'
    # file = file.lower()
    # # Converting to Lowercase
    max_features.extend(file.split(" "))
    files_edited.append(file)

vectorizer = TfidfVectorizer(max_features=80000, min_df=10)
files_vectorized = vectorizer.fit_transform(files_edited)
files_train, files_test, categories_train, categories_test = train_test_split(files_vectorized, categories)

sgdc_clf = SGDClassifier()
sgdc_clf.fit(files_train, categories_train)
print(sgdc_clf.score(files_test, categories_test))
with open("sgdc_clf2", "wb") as picklefile:
    pickle.dump(sgdc_clf, picklefile)


vectorizer2 = CountVectorizer(max_features=80000, min_df=10)
files_vectorized2 = vectorizer2.fit_transform(files_edited)
files_train2, files_test2, categories_train2, categories_test2 = train_test_split(files_vectorized2, categories)

sgdc_clf2 = SGDClassifier()
sgdc_clf2.fit(files_train2, categories_train2)
print(sgdc_clf2 .score(files_test2, categories_test2))
with open("sgdc_clf3", "wb") as picklefile:
    pickle.dump(sgdc_clf2, picklefile)

lsvc_clf = LinearSVC()
lsvc_clf.fit(files_train, categories_train)
categories_pred = lsvc_clf.predict(files_test)
# print(lsvc_clf.score(files_test, categories_test))
# f1_score la diem ket hop giua precision vs recall
# MICRO: weights each sample equally => no favouring any class
# WEIGHTED: The F1 Scores are calculated for each label and then their average is weighted by support - which is the
# number of true instances for each label => favoring majority
# MACRO: weights each class equally => favoring minority
print(f1_score(categories_test, categories_pred, average='macro'))
print(f1_score(categories_test, categories_pred, average='micro'))
print(f1_score(categories_test, categories_pred, average='weighted'))

with open("lsvc_clf2", "wb") as picklefile:
    pickle.dump(lsvc_clf, picklefile)

# svc_clf = SVC()
# svc_clf.fit(files_train, categories_train)
# print(svc_clf.score(files_test, categories_test))
# with open("svc_clf2", "wb") as picklefile:
#     pickle.dump(svc_clf, picklefile)
