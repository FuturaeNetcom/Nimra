# -*- coding: utf-8 -*-
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint

import numpy
import re


def main():
    raw_text = getRawText('data/scraped_material-a-1543749875.txt')
    cleanText(raw_text)


def getRawText(filename):
    raw_text = open(filename, encoding="utf8").read()
    raw_text = raw_text.lower()
    return raw_text


def cleanText(raw_text):
    '''
    # remove all special characters
    match = re.findall(r"\W", raw_text)
    match = list(dict.fromkeys(match))
    match.remove(' ')
    match.remove('?')
    match.remove('\n')
    match.remove('.')
    match.remove(',')
    match.append('_')
    for char in match:
        raw_text = raw_text.replace(char, ' ')
    # remove all numbers
    match = re.findall(r"[0-9]", raw_text)
    match = list(dict.fromkeys(match))
    for char in match:
        raw_text = raw_text.replace(char, ' ')
    '''
    char_list = sorted(list(set(raw_text)))
    match_list = ['\n', ' ', ',', '.', '?', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for match in match_list:
        char_list.remove(match)
    for char in char_list:
        raw_text = raw_text.replace(char, '')
    return raw_text


# prepare the dataset of input to output pairs encoded as integers
def createPatterns(raw_text, n_vokab, SEQUENCE_LENGTH, char_to_int):
    dataX = []
    dataY = []
    for i in range(0, n_vokab - SEQUENCE_LENGTH, 1):
        seq_in = raw_text[i:i + SEQUENCE_LENGTH]
        seq_out = raw_text[i + SEQUENCE_LENGTH]
        dataX.append([char_to_int[char] for char in seq_in])
        dataY.append(char_to_int[seq_out])
    print("Total Patterns: ", len(dataX))
    return dataX, dataY


def getX(dataX, SEQUENCE_LENGTH, n_vocab):
    # reshape X to be [samples, time steps, features]
    X = numpy.reshape(dataX, (len(dataX), SEQUENCE_LENGTH, 1))
    # normalize
    X = X / float(n_vocab)
    return X


def getY(dataY):
    # one hot encode the output variable
    y = np_utils.to_categorical(dataY)
    return y


def createModel(X, y):
    # define the LSTM model
    model = Sequential()
    model.add(LSTM(256, input_shape=(X.shape[1], X.shape[2])))
    model.add(Dropout(0.2))
    model.add(Dense(y.shape[1], activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam')
    return model


def createCallbacks(NAME_WEIGHTS):
    filepath = "weights-" + NAME_WEIGHTS + "-{epoch:02d}-{loss:.4f}.hdf5"
    checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1,
                                 save_best_only=True, mode='min')
    return [checkpoint]

main()
print('model_training_func finished')
