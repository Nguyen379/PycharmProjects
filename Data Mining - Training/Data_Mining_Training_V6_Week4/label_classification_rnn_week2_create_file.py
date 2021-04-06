import numpy as np
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout, SpatialDropout1D
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence
from sklearn.datasets import load_files
import pickle

reviews_train = load_files(r"C:\Users\Asus\PycharmProjects\Data Mining - Training"
                           r"\Data_Mining_Training_V6_Week2\new train")
reviews_test = load_files(r"C:\Users\Asus\PycharmProjects\Data Mining - Training"
                          r"\Data_Mining_Training_V6_Week2\new test")
train_files, train_categories = reviews_train.data, reviews_train.target
test_files, test_categories = reviews_test.data, reviews_test.target
combined_files = train_files.copy()
combined_files.extend(test_files)
dict_all_words = {}
new_combined_files = []
for file in combined_files:
    file = file.split(b" ")
    new_combined_files.append(file)
for file in new_combined_files[:len(train_files)]:
    for word in file:
        if word not in dict_all_words:
            dict_all_words[word] = 0
        else:
            dict_all_words[word] += 1

one_quarter = len(dict_all_words.items()) // 4 #55214
sorted_dict_words = sorted(dict_all_words.items(), key=lambda x: x[1])[-one_quarter:]
dict_best_words = {k: sorted_dict_words.index((k, v)) for (k, v) in sorted_dict_words}
edited_combined_file = []
for file in new_combined_files:
    new_file = []
    for word in file:
        if word in dict_best_words:
            new_file.append(dict_best_words[word])
    edited_combined_file.append(new_file)

X_train, X_test, y_train, y_test = edited_combined_file[:len(train_files)], edited_combined_file[len(train_files):], \
                                   train_categories, test_categories
pickle_out = open("X_train.pickle", "wb")
pickle.dump(X_train, pickle_out)
pickle_out.close()
pickle_out = open("y_train.pickle", "wb")
pickle.dump(y_train, pickle_out)
pickle_out.close()
pickle_out = open("X_test.pickle", "wb")
pickle.dump(X_test, pickle_out)
pickle_out.close()
pickle_out = open("y_test.pickle", "wb")
pickle.dump(y_test, pickle_out)
pickle_out.close()
