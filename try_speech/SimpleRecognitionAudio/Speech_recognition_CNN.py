from pyAudioAnalysis import audioBasicIO as aIO
from pyAudioAnalysis import audioAnalysis as aAnaly
import os

# %load_ext autoreload
# %autoreload 2
# from preprocess import *
# import keras
# from keras.models import Sequential
# from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
# from keras.utils import to_categorical
# import numpy as np

# def get_model():
#     model = Sequential()
#     model.add(Conv2D(32, kernel_size=(2, 2), activation='relu', input_shape=(feature_dim_1, feature_dim_2, channel)))
#     model.add(Conv2D(48, kernel_size=(2, 2), activation='relu'))
#     model.add(Conv2D(120, kernel_size=(2, 2), activation='relu'))
#     model.add(MaxPooling2D(pool_size=(2, 2)))
#     model.add(Dropout(0.25))
#     model.add(Flatten())
#     model.add(Dense(128, activation='relu'))
#     model.add(Dropout(0.25))
#     model.add(Dense(64, activation='relu'))
#     model.add(Dropout(0.4))
#     model.add(Dense(num_classes, activation='softmax'))
#     model.compile(loss=keras.losses.categorical_crossentropy,
#                   optimizer=keras.optimizers.Adadelta(),
#                   metrics=['accuracy'])
#     return model

# # Predicts one sample
# def predict(filepath, model):
#     sample = wav2mfcc(filepath)
#     sample_reshaped = sample.reshape(1, feature_dim_1, feature_dim_2, channel)
#     return get_labels()[0][
#             np.argmax(model.predict(sample_reshaped))
#     ]
# #     print(model.predict(sample_reshaped))
# #     return np.argmax(model.predict(sample_reshaped))



# # Second dimension of the feature is dim2
# feature_dim_2 = 11
# dataset_size_model = -1

# # Save data to array file first
# save_data_to_array(max_len=feature_dim_2, size_dataset=dataset_size_model)

# # Loading train set and test set
# X_train, X_test, y_train, y_test = get_train_test()

# # # Feature dimension
# feature_dim_1 = 20
# channel = 1
# epochs = 200
# batch_size = 100
# verbose = 1
# num_classes = 8

# # Reshaping to perform 2D convolution
# X_train = X_train.reshape(X_train.shape[0], feature_dim_1, feature_dim_2, channel)
# X_test = X_test.reshape(X_test.shape[0], feature_dim_1, feature_dim_2, channel)

# y_train_hot = to_categorical(y_train)
# y_test_hot = to_categorical(y_test)

# model = get_model()
# model.fit(X_train, y_train_hot, batch_size=batch_size, epochs=epochs, verbose=verbose, validation_data=(X_test, y_test_hot))

# prediction = predict('./teste_audio/maconha-treino0d3a1dfab0de439ba80162ef1fa46816.wav', model=model)

# print(prediction)

# aAnaly.silenceRemovalWrapper("utils/teste.mp3", smoothingWindow=1.0, weight=0.3)
os.system("cp utils/teste.mp3 teste.mp3")
aAnaly.silenceRemovalWrapper("teste.mp3", smoothingWindow=1.0, weight=0.3)
os.system("rm teste.mp3")

