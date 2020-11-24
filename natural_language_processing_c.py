# Natural Language Processing

# Importing the libraries
import numpy as np
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk import WordNetLemmatizer
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import precision_score, recall_score, confusion_matrix,accuracy_score
import nltk
import emoji
import itertools
from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer
from datetime import datetime
from nltk.tokenize import RegexpTokenizer
import string


def create_metrics(y_test, y_pred, decimal=3):
  """
  @param y_test: the real values of the target variable
  @param y_pred: the predicted values of the target variable
  @param decimal: the rounded decimal value of accuracy, precision and recall
  @return: confusion matrix, first type error, second type error, accuracy, precision, recall
  """

  cm = confusion_matrix(y_test, y_pred)
  error_first_type = cm[0, 1]
  error_second_type = cm[1, 0]
  accuracy = np.round(accuracy_score(y_test, y_pred), decimal)
  precision = np.round(precision_score(y_test, y_pred), decimal)
  recall = np.round(recall_score(y_test, y_pred), decimal)
  return cm, error_first_type, error_second_type, accuracy, precision, recall

# Importing the dataset
dataset = pd.read_csv('train.csv', sep=",", quoting = 0,encoding = "ISO-8859-1")
datest = pd.read_csv('test.csv', sep=",", quoting = 0,encoding = "ISO-8859-1")

dataset = dataset.drop("ItemID",axis=1)

# Cleaning the texts
#nltk.download('stopwords')
#
#nltk.download('wordnet')
corpus = []
ps = PorterStemmer()
lm = WordNetLemmatizer()
tokenizer = RegexpTokenizer(r'\w+')

all_stopwords = stopwords.words('english')
all_stopwords.remove('not')
all_stopwords.remove('no')
all_stopwords.remove('nor')

# preprocessing phase
for i in range(0, dataset.shape[0]):
    # remove mentions and hashtags
    tweet = re.sub('(@[A-Za-z0-9]+)|(#[A-Za-z0-9]+)', ' ', str(dataset['SentimentText'][i]))
    # remove url that start with http:// or https://
    tweet = re.sub('(\w+:\/\/\S+)', ' ', tweet)
    # remove punctuations
    tweet = tweet.translate(str.maketrans('', '', string.punctuation))
    # remove digits
    tweet = re.sub(" \d+", " ", tweet)
    # lower case all words
    tweet = tweet.lower()
    # correct spelling of words
    #tweet = str(TextBlob(tweet).correct())
    # create list of words from string
    tweet = tweet.split()
    # take only words whose length is greater than 1
    tweet = [i for i in tweet if len(i)>1]
    # stemming of words
    tweet = [ps.stem(word) for word in tweet if not word in set(all_stopwords)]
    # lemmatization of words
    tweet = [lm.lemmatize(word) for word in tweet]
    # create string from list of words
    tweet = ' '.join(tweet)
    # append to corpus
    corpus.append(tweet)
    print(i)

# Creating the Bag of Words model with single words, bigrams and trigrams. there are 955949 ngrams
cv = TfidfVectorizer(ngram_range=(1,2),max_features=5000)
X = cv.fit_transform(corpus).toarray()
count_vect_df = pd.DataFrame(X, columns=cv.get_feature_names())

# target variable
y = dataset.iloc[:, 0].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(count_vect_df, y, test_size = 0.20, random_state = 42)


# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0,max_iter=200,C=0.5)
classifier.fit(X_train, y_train)
#TODO: cross validation, could be a little slow but should be worth points

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Probabilities of test set tweet being negative or positive
proba = classifier.predict_proba(X_test)

cm, error_first_type, error_second_type, accuracy, precision, recall = create_metrics(y_test=y_test, y_pred=y_pred)
print("accuracy = {}".format(accuracy))
print("precision = {}".format(precision))
print("recall = {}".format(recall))
