# Import packages
import sys
import pickle
import nltk
nltk.data.path=['./tmp']
from nltk.corpus import stopwords
from nltk import download
from nltk.tokenize import word_tokenize
from string import punctuation

print(nltk.data.path)
# Download datasets
download('punkt', download_dir='./tmp')
download('stopwords', download_dir='./tmp')
# Set stopwords
stopwords_eng = stopwords.words('english')
# Import model
if 'google.colab' not in sys.modules:
    model_file = open('sa_classifier.pickle', 'rb')
    model = pickle.load(model_file)
    model_file.close()
# Define functions


def extract_features(words):
    """
    Remove stopwords from words
    Input:
    - words (list of string)
    Output
    - list of string
    """
    return [
        w for w in words
        if w not in stopwords_eng
        and w not in punctuation
        ]


def bag_of_words(words):
    """
    Tally word occurences into a dict
    Input:
    - words (list of strings)
    Output:
    - bad (dict of (string: int) pairs)
    """
    bag = {}
    for w in words:
        bag[w] = bag.get(w, 0)+1
    return bag


def get_sentiment(review):
    """
    Return 'pos' or 'neg' sentiment for the review
    Input:
    - review (str)
    Output:
    - str: 'pos' for positive and 'neg' for negative
    """
    words = word_tokenize(review)
    words = extract_features(words)
    words = bag_of_words(words)
    return model.classify(words)
