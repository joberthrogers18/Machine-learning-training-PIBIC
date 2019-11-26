from pyAudioAnalysis import audioBasicIO as aIO
from pyAudioAnalysis import audioAnalysis as aAnaly
import os
import glob

# %load_ext autoreload
# %autoreload 2
from preprocess import *
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from keras.utils import to_categorical
import numpy as np

# Feature dimension
FEATURE_DIM_1 = 20
CHANNEL = 1
EPOCHS = 200
BATCH_SIZE = 100
VERBOSE = 1
NUM_CLASSES = 8

# Second dimension of the feature is dim2
FEATURE_DIM_2 = 11
DATASET_SIZE_MODEL = -1

def get_model():
    model = Sequential()
    model.add(Conv2D(32, kernel_size=(2, 2), activation='relu', input_shape=(FEATURE_DIM_1, FEATURE_DIM_2, CHANNEL)))
    model.add(Conv2D(48, kernel_size=(2, 2), activation='relu'))
    model.add(Conv2D(120, kernel_size=(2, 2), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.25))
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.4))
    model.add(Dense(NUM_CLASSES, activation='softmax'))
    model.compile(loss=keras.losses.categorical_crossentropy,
                  optimizer=keras.optimizers.Adadelta(),
                  metrics=['accuracy'])
    return model

# Predicts one sample
def predict(filepath, model):
    sample = wav2mfcc(filepath)
    sample_reshaped = sample.reshape(1, FEATURE_DIM_1, FEATURE_DIM_2, CHANNEL)
    return get_labels()[0][
            np.argmax(model.predict(sample_reshaped))
    ]
#     print(model.predict(sample_reshaped))
#     return np.argmax(model.predict(sample_reshaped))


def training_model():

    # Save data to array file first
    # save_data_to_array(max_len=FEATURE_DIM_2, size_dataset=DATASET_SIZE_MODEL)

    # Loading train set and test set
    X_train, X_test, y_train, y_test = get_train_test()

    # Reshaping to perform 2D convolution
    X_train = X_train.reshape(X_train.shape[0], FEATURE_DIM_1, FEATURE_DIM_2, CHANNEL)
    X_test = X_test.reshape(X_test.shape[0], FEATURE_DIM_1, FEATURE_DIM_2, CHANNEL)

    y_train_hot = to_categorical(y_train)
    y_test_hot = to_categorical(y_test)

    model = get_model()
    model.fit(X_train, y_train_hot, batch_size=BATCH_SIZE, epochs=EPOCHS, verbose=VERBOSE, validation_data=(X_test, y_test_hot))

    # prediction = predict('./teste_audio/maconha-treino0d3a1dfab0de439ba80162ef1fa46816.wav', model=model)
    # print(prediction)

    return model

if __name__ == '__main__':

    predictions = []
    pediction_audios = []

    # return the model trained
    model = training_model()

    for file_audio in os.listdir('./teste_audio/'):
        # Verify through the split audio if audio is suspect or not
    
        os.system("cp teste_audio/" + file_audio + " " + file_audio)
        aAnaly.silenceRemovalWrapper(file_audio , smoothingWindow=1.0, weight=0.3)

        prediction = []
        os.system("rm " + file_audio)

        for filename in glob.glob(os.path.join(os.getcwd(), "*.wav")):
            print(filename)
            predictions.append( predict(filename, model=model) )
            os.system("rm " + str(filename))

        pediction_audios.append('Audio suspeito') if 'maconha' in predictions else pediction_audios.append('Não suspeito')

    print('Audios não suspeitos: ' + str( pediction_audios.count('Não suspeito') ) )
    print('Audios suspeitos: ' + str( pediction_audios.count('Audio suspeito') ) )