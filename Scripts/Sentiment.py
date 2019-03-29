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