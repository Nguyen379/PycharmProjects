import numpy as np
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout, SpatialDropout1D, Conv1D, MaxPooling1D
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence
from keras.utils import np_utils
import pickle
from tensorflow.keras.callbacks import TensorBoard
import time
# NAME = time.time()
# tensorboard = TensorBoard(log_dir=f'logsRNN/{NAME}')
X_train = pickle.load(open("X_train.pickle", "rb"))
X_test = pickle.load(open("X_test.pickle", "rb"))
y_train = pickle.load(open("y_train.pickle", "rb"))
y_test = pickle.load(open("y_test.pickle", "rb"))

max_len = 0
for n in X_train:
    if len(n) > max_len:
        max_len = len(n)
max_review_len = max_len//2

dense_output = len(np.unique(y_train))

X_train = sequence.pad_sequences(X_train, maxlen=max_review_len)
X_test = sequence.pad_sequences(X_test, maxlen=max_review_len)
X_train = np.array(X_train)
X_test = np.array(X_test)
y_train = np.reshape(y_train, (-1, 1))
y_test = np.reshape(y_test, (-1, 1))
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

model = Sequential()

model.add(Embedding(55214, 512, input_length=max_review_len))
# one_auarter == 55214 => look at create_file
# model.add(SpatialDropout1D(0.2)
model.add(Conv1D(filters=512, kernel_size=3, padding='same', activation='relu'))
model.add(MaxPooling1D(pool_size=2))

model.add(Conv1D(filters=512, kernel_size=3, padding='same', activation='relu'))
model.add(MaxPooling1D(pool_size=2))

model.add(Conv1D(filters=512, kernel_size=3, padding='same', activation='relu'))
model.add(MaxPooling1D(pool_size=2))

model.add(LSTM(100, dropout=0.2, recurrent_dropout=0.2))

model.add(Dense(128, activation="relu"))
model.add(Dense(dense_output, activation="softmax"))

model.compile(loss="sparse_categorical_crossentropy", metrics=["accuracy"], optimizer="adam")
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10, batch_size=16)
model.save("lstm_100_dense_1_embedding_5000_32")
