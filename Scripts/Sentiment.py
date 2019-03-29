import pickle, nltk
from nltk.corpus import stopwords
from sklearn.linear_model import LogisticRegression as LR
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
import re
allowed_word_types = ["JJ", "JJR", "JJS", "NN", "NNS", "RB", "RBR", "RBS", "VB", "VBD", "VBG", "VBN", "VBP"]
stop_words = set(stopwords.words("English"))

#vectorizer = TfidfVectorizer()

open_file = open("../Pickle/Vectorizer.pickle", "rb")
vectorizer = pickle.load(open_file)
open_file.close()

open_file = open("../Pickle/LogisticRegression.pickle", "rb")
LR = pickle.load(open_file)
open_file.close()

class VoteClassifier(ClassifierI):
    """docstring for VoteClassifier"""
    def __init__(self, *classifiers):
        self._classifiers = classifiers
    
    def classify(self, features):
        votes =[]
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        return str(mode(votes)[0])

    def confidence(self, features):
        votes =[]
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        choice_votes = int(mode(votes)[1])
        conf = choice_votes / len(votes)
        return conf


def processing(tweet):
    tweet.lower()
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))',' ',tweet)
    tweet = re.sub('@[^\s]+',' ', tweet)
    tweet = re.sub('[\s]+', ' ', tweet)
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    sentence = nltk.pos_tag(word_tokenize(str(tweet)))
    full = []
    for s in sentence:
        if s[1] in allowed_word_types and s[0] not in stop_words:
            full.append(s[0])
    fulls = " ".join(full)
    return fulls

def sentiment(text):
    processed_text = processing(text);
    tfidf_vect = vectorizer.transform([processed_text]);
    yhat = LR.predict(tfidf_vect)
    return yhat