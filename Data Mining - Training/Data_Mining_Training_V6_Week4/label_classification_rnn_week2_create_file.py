import numpy as np
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout, SpatialDropout1D
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence
from sklearn.datasets import load_files
import pickle
# Doc file train, test
reviews_train = load_files(r"C:\Users\Asus\PycharmProjects\Data Mining - Training"
                           r"\Data_Mining_Training_V6_Week2\new train")
reviews_test = load_files(r"C:\Users\Asus\PycharmProjects\Data Mining - Training"
                          r"\Data_Mining_Training_V6_Week2\new test")
train_files, train_categories = reviews_train.data, reviews_train.target
test_files, test_categories = reviews_test.data, reviews_test.target

# Mục đích: lọc chỉ lấy 1/4 những từ phổ biến nhất còn lại thì bỏ không dùng
# combined_files là kết hợp file train và test. Dùng file này để đếm số từ
combined_files = train_files.copy()
combined_files.extend(test_files)
dict_all_words = {}
new_combined_files = []
for file in combined_files:
    file = file.split(b" ")
    # chia 1 câu thành 1 list chứa những từ đơn: "tôi tên là A" => ["tôi", "tên", "là", "A"]
    new_combined_files.append(file)
for file in new_combined_files:
    # đếm số từ: nếu từ nào không có trong dict thì thêm vào, có rồi thì +1
    for word in file:
        if word not in dict_all_words:
            dict_all_words[word] = 0
        else:
            dict_all_words[word] += 1

# lọc lấy 1/4 số từ phổ biến nhất trong tổng số từ làm feature_words.
one_quarter = len(dict_all_words.items()) // 4 #81306
# lọc dict lấy 1/4 số từ phổ biến nhất
sorted_dict_words = sorted(dict_all_words.items(), key=lambda x: x[1])[-one_quarter:]
# dict có cặp key:value là feature_word:index.
dict_best_words = {k: sorted_dict_words.index((k, v)) for (k, v) in sorted_dict_words}
edited_combined_file = []
for file in new_combined_files:
    # tạo câu mới: những từ trong câu cũ được thay bằng index (thể hiện mức độ phổ biến).
    # Những từ không có trong dict thì bỏ qua
    # cho câu mới này vào 1 new_file r thêm tất cả vào edited_combined_file => chứa tất cả các câu
    new_file = []
    for word in file:
        if word in dict_best_words:
            new_file.append(dict_best_words[word])
    edited_combined_file.append(new_file)

# edited_combined_file sẽ được slicing lại thành train_file và test_file do số lượng câu không thay đổi
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
