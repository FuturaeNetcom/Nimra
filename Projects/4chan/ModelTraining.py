#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 18:10:43 2018

@author: simon

Project: Futurae Netcom
"""
import model_training_func as func

FILE_NAME = 'data/scraped_material-a-1543749875.txt'
WEIGHTS = 'weights/weights-improvement-15-1.6908.hdf5'
NAME_WEIGHTS = 'new-try-a'
SEQUENCE_LENGTH = 100
TRAIN = 'Start'  # Start, Load, Continue
EPOCHS = 15


def start(file_name, weights, name, train, epochs):
    if (file_name is not None):
        global FILE_NAME
        FILE_NAME = file_name
    if (weights is not None):
        global WEIGHTS
        WEIGHTS = weights
    if (name is not None):
        global NAME_WEIGHTS
        NAME_WEIGHTS = name
    if (train is not None):
        global TRAIN
        TRAIN = train
    if (epochs is not None):
        global EPOCHS
        EPOCHS = epochs
    main()

# main part of the program
def main():
    clean_text, chars, int_to_char = text_setup()
    print_info(clean_text, chars)
    X, y, dataX = set_data(clean_text, chars)
    model = model_setup(X, y)
    predict(model, dataX, len(chars), int_to_char)


def get_text(FILE_NAME):
    raw_text = func.getRawText(FILE_NAME)
    clean_text = func.cleanText(raw_text)
    return clean_text


def text_setup():
    clean_text = get_text(FILE_NAME)
    chars = sorted(list(set(clean_text)))
    int_to_char = dict((i, c) for i, c in enumerate(chars))
    return clean_text, chars, int_to_char


def print_info(clean_text, chars):
    n_chars = len(clean_text)
    n_vocab = len(chars)
    print("Total Characters: ", n_chars)
    print("Total Vocab: ", n_vocab)


def set_data(clean_text, chars):
    char_to_int = dict((c, i) for i, c in enumerate(chars))
    dataX, dataY = func.createPatterns(clean_text, len(clean_text), SEQUENCE_LENGTH, char_to_int)
    X = func.getX(dataX, SEQUENCE_LENGTH, len(chars))
    y = func.getY(dataY)
    return X, y, dataX


def model_setup(X, y):
    model = func.createModel(X, y)
    callbacks_list = func.createCallbacks(NAME_WEIGHTS)
    if(TRAIN == 'Start'):
        model.fit(X, y, epochs=EPOCHS, batch_size=128,
                  verbose=1, callbacks=callbacks_list)
    elif(TRAIN == 'Load'):
        model.load_weights(WEIGHTS)
    elif(TRAIN == 'Continue'):
        model.load_weights(WEIGHTS)
        model.fit(X, y, epochs=EPOCHS, batch_size=128,
                  verbose=1, callbacks=callbacks_list)
    model.compile(loss='categorical_crossentropy', optimizer='adam')
    return model


def predict(model, dataX, n_vocab, int_to_char):
    import numpy
    import sys
    start = numpy.random.randint(0, len(dataX)-1)
    pattern = dataX[start]
    print("Seed:")
    print("\"", ''.join([int_to_char[value] for value in pattern]), "\"")
    # generate characters
    for i in range(1000):
        x = numpy.reshape(pattern, (1, len(pattern), 1))
        x = x / float(n_vocab)
        prediction = model.predict(x, verbose=0)
        index = numpy.argmax(prediction)
        result = int_to_char[index]
        sys.stdout.write(result)
        pattern.append(index)
        pattern = pattern[1:len(pattern)]
    print("\nDone.")
   
start(None,None,None,None,None)

