from __future__ import print_function

import pickle
import sys

import numpy as np
from keras.models import load_model


def sample(preds, temperature=1.0):
    # helper function to sample an index from a probability array
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)


def gen_sentence(read):
    response = ''

    text = open("moby_dick.txt").read().lower()
    print('corpus length:', len(text))

    chars = sorted(list(set(text)))
    print('total chars:', len(chars))
    char_indices = dict((c, i) for i, c in enumerate(chars))
    indices_char = dict((i, c) for i, c in enumerate(chars))

    model = load_model("model.h5")

    maxlen = 40

    generated = ''
    read = read.lower() + " "
    sentence = read[:maxlen]
    if len(sentence) < maxlen:
        sentence = (' ' * (maxlen - len(sentence))) + sentence
    generated += sentence
    print('----- Generating with seed: "' + sentence + '"')
    sys.stdout.write(generated)

    for i in range(200):
        x_pred = np.zeros((1, maxlen, len(chars)))
        for t, char in enumerate(sentence):
            x_pred[0, t, char_indices[char]] = 1.

        preds = model.predict(x_pred, verbose=0)[0]
        next_index = sample(preds, 1.0)
        next_char = indices_char[next_index]

        sentence = sentence[1:] + next_char
        response += next_char
    print(read + response)
    return read, response


if __name__ == "__main__":
    print(gen_sentence(input()))
