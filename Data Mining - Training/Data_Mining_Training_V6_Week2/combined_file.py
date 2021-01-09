from sklearn.linear_model import SGDClassifier
import re
from sklearn.datasets import load_files
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC, LinearSVC
from sklearn.model_selection import train_test_split

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

lsvc_clf = LinearSVC()
lsvc_clf.fit(files_train, categories_train)
print(lsvc_clf.score(files_test, categories_test))
with open("lsvc_clf2", "wb") as picklefile:
    pickle.dump(lsvc_clf, picklefile)

# svc_clf = SVC()
# svc_clf.fit(files_train, categories_train)
# print(svc_clf.score(files_test, categories_test))
# with open("svc_clf2", "wb") as picklefile:
#     pickle.dump(svc_clf, picklefile)
