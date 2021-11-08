from typing import SupportsFloat
from nltk import featstruct
from nltk.grammar import _read_dependency_production
from nltk.probability import HeldoutProbDist
import numpy as np #pip install numpy
import nltk #pip install nltk
from nltk.stem.porter import PorterStemmer
from numpy.core.shape_base import _block_dispatcher

Stemmer = PorterStemmer()

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return Stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence,words):
    sentence_word = [stem(word) for word in tokenized_sentence]
    bag = np.zeros(len(words),dtype=np.float32)

    for idx , w in enumerate(words):
        if w in sentence_word:
            bag[idx] = 1

    return bag

