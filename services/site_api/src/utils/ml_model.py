from sklearn.base import BaseEstimator, TransformerMixin
from catboost import CatBoostClassifier, Pool
import numpy as np
import pymorphy2
from navec import Navec
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

class PreProcessing(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.morph = pymorphy2.MorphAnalyzer()
        self.tokenize = lambda word: word_tokenize(word)
        self.navec = Navec.load('navec_hudlit_v1_12B_500K_300d_100q.tar')
        self.model = CatBoostClassifier()

    def transform(self, df, mode='train'):
        lemmatize_word = lambda word: self.morph.parse(word)[0].normal_form

        columns = ['chair_name', 'name', 'faculty_name', 'groups']
        labels = None
        if mode == 'train':
            labels = df['profession']

        df = df[columns].replace('', 'No information available')

        df['groups'] = df.apply(lambda row: ' '.join(row), axis=1)
        df['groups'] = df['groups'].apply(lambda x: ' '.join([lemmatize_word(word) for word in x.split()]))
        df['groups'] = df['groups'].apply(lambda x: ' '.join(self.tokenize(x)))

        data = []

        for text in df['groups'].tolist():
            text = [self.navec[word] if word in self.navec else self.navec['<unk>'] for word in text.split()]
            text = np.mean(text, axis=0)
            data.append(text)

        for i in range(300):
            col_name = f'word2vec_feature_{i}'
            df[col_name] = [vector[i] for vector in data]
        df = df.drop(['groups'], axis=1)
        return df, labels

    def predict(self, df):
        self.model = self.model.load_model('path')
        return self.model.predict_proba(df)