import numpy as np
import tensorflow as tf
import re
import pickle as pkl

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, SpatialDropout1D, LSTM, Conv1D, MaxPooling1D
from tensorflow.keras import layers


MODEL_PATH = "model_pretrain/cp.ckpt"
MAX_NB_WORDS = 59000
MAX_SEQUENCE_LENGTH = 150
HIDDEN_DIM = 200
TOKENIZER = Tokenizer(num_words=MAX_NB_WORDS, lower=True)
X = np.load('offensive_hate.pkl', allow_pickle=True)


class HateOffensiveModel:
    def model_load(self):
        model = self.hate_offensive_model()
        model.load_weights(MODEL_PATH)
        return model

    @staticmethod
    def hate_offensive_model():
        model = Sequential()
        model.add(Embedding(MAX_NB_WORDS, HIDDEN_DIM, input_length=X.shape[1]))
        model.add(SpatialDropout1D(0.2))
        model.add(LSTM(100, dropout=0.2, recurrent_dropout=0.2))
        model.add(Dense(3, activation='softmax'))

        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

        return model


def get_tokens():
    with open('tokenizer.pkl', 'rb') as handle:
        tokenizer_load = pkl.load(handle)

    return tokenizer_load


def clean_text(text):
    text = re.sub('[»„‘’“”…]', ' ', text)
    text = re.sub('\w*\d\w*', 'Nummer', text)
    text = re.sub(r"https?://\S+|www\.\S+", ' ', text)
    text = re.sub('[\u0080-\uffff]w{1-3}', " ", text)
    text = re.sub(r"[^\x00-\x7F\w{1,3}]+", ' ', text)
    text = re.sub(r"(#[\d\w\.]+)", ' ', text)
    text = re.sub(r"(@[\d\w\.]+)", ' ', text)

    tokenizer = get_tokens()

    text = tokenizer.texts_to_sequences([text])

    return text


def predict_lang(text):
    text = clean_text(text)
    padded = pad_sequences(text, maxlen=MAX_SEQUENCE_LENGTH)
    array_pred = np.round(model.predict(padded)[0], 4)

    pred = {'hate': array_pred[0],
                           'neither': array_pred[1],
                           'offensive': array_pred[2]}

    return pred


if __name__ == '__main__':
    model_inst = HateOffensiveModel()
    model = model_inst.model_load()
    print(predict_lang('Hello'))
