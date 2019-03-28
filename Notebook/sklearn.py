
# coding: utf-8

# In[1]:


import pandas as pd
#from sklearn.model_selection import GridSearchCV, train_test_split, KFold
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import AdaBoostClassifier, GradientBoostingClassifier, RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC, NuSVC, SVC
from sklearn.tree import DecisionTreeClassifier, ExtraTreeClassifier
from sklearn.naive_bayes import BernoulliNB, GaussianNB, MultinomialNB
from sklearn import metrics
from sklearn.utils import shuffle
from matplotlib import pyplot as plt
import numpy as np
import itertools
from sklearn.preprocessing import Normalizer
import xgboost
get_ipython().run_line_magic('matplotlib', 'inline')
import random
from sklearn.feature_extraction.text import TfidfVectorizer


# In[2]:


data = pd.read_csv("../Data/train_data.csv")
data.columns


# In[3]:


data.tweets.isnull().value_counts()


# In[4]:


data.dropna(axis=0, inplace=True)


# In[5]:


data.shape


# In[6]:


target = data['target']
data = data.drop(columns=["target", 'Unnamed: 0'], axis=1)
print("{}\n{}".format(data.shape, target.shape))


# In[7]:


vectorizer = TfidfVectorizer()
tweets = vectorizer.fit_transform(data["tweets"])
#print(vectorizer.get_feature_names())
print(tweets.shape)


# In[8]:


x_train, x_test, y_train, y_test = train_test_split(tweets, target, test_size=0.333, random_state=42)


# In[9]:


'''
Test_accuracy = []
Train_accuracy = []
for i in range(1, 10):
    neigh = KNeighborsClassifier(n_neighbors=i)
    neigh.fit(x_train, y_train)
    y_hat = neigh.predict(x_test)
    Test_accuracy.append(metrics.accuracy_score(y_train, neigh.predict(x_train)))
    Train_accuracy.append(metrics.accuracy_score(y_test, y_hat))
plt.plot(Test_accuracy, color="r")
plt.plot(Train_accuracy, color="c")
'''


# In[10]:


LR = LogisticRegression()
LR.fit(x_train,y_train)
yhat = LR.predict(x_test)
print("LogisticRegression")
print("Train set Accuracy: ", metrics.accuracy_score(y_train, LR.predict(x_train)))
print("Test set Accuracy: ", metrics.accuracy_score(y_test, yhat))


# In[11]:


BNB = BernoulliNB()
BNB.fit(x_train,y_train)
yhat = BNB.predict(x_test)
print("BernoulliNB")
print("Train set Accuracy: ", metrics.accuracy_score(y_train, BNB.predict(x_train)))
print("Test set Accuracy: ", metrics.accuracy_score(y_test, yhat))


# In[12]:


MNB = MultinomialNB()
MNB.fit(x_train,y_train)
yhat = MNB.predict(x_test)
print("MultinomialNB")
print("Train set Accuracy: ", metrics.accuracy_score(y_train, MNB.predict(x_train)))
print("Test set Accuracy: ", metrics.accuracy_score(y_test, yhat))


# In[13]:


'''
GNB = GaussianNB()
GNB.fit(x_train,y_train)
yhat = GNB.predict(x_test)
print(" GaussianNB")
print("Train set Accuracy: ", metrics.accuracy_score(y_train, GNB.predict(x_train)))
print("Test set Accuracy: ", metrics.accuracy_score(y_test, yhat))
'''


# In[14]:


"""LSVC = LinearSVC()
LSVC.fit(x_train,y_train)
yhat = LSVC.predict(x_test)
print("LinearSVC")
print("Train set Accuracy: ", metrics.accuracy_score(y_train, LSVC.predict(x_train)))
print("Test set Accuracy: ", metrics.accuracy_score(y_test, yhat))
"""


# In[15]:


"""PSVC = SVC()
PSVC.fit(x_train,y_train)
yhat = PSVC.predict(x_test)
print("SVC")
print("Train set Accuracy: ", metrics.accuracy_score(y_train, PSVC.predict(x_train)))
print("Test set Accuracy: ", metrics.accuracy_score(y_test, yhat))
"""


# In[ ]:


RForest = RandomForestClassifier()
RForest.fit(x_train, y_train)
yhat = RForest.predict(x_test)
print("RandomForestClassifier")
print("Train set Accuracy: ", metrics.accuracy_score(y_train, RForest.predict(x_train)))
print("Test set Accuracy: ", metrics.accuracy_score(y_test, yhat))


# In[ ]:


DTree = DecisionTreeClassifier(max_depth=3)
DTree.fit(x_train, y_train)
yhat = DTree.predict(x_test)
print("DecisionTreeClassifier")
print("Train set Accuracy: ", metrics.accuracy_score(y_train, DTree.predict(x_train)))
print("Test set Accuracy: ", metrics.accuracy_score(y_test, yhat))


# In[ ]:


ETree = ExtraTreeClassifier(max_depth=3)
ETree.fit(x_train, y_train)
yhat = ETree.predict(x_test)
print("ExtraTreeClassifier")
print("Train set Accuracy: ", metrics.accuracy_score(y_train, ETree.predict(x_train)))
print("Test set Accuracy: ", metrics.accuracy_score(y_test, yhat))


# In[ ]:


Ada = AdaBoostClassifier()
Ada.fit(x_train, y_train)
yhat = Ada.predict(x_test)
print("AdaBoostClassifier")
print("Train set Accuracy: ", metrics.accuracy_score(y_train, Ada.predict(x_train)))
print("Test set Accuracy: ", metrics.accuracy_score(y_test, yhat))


# In[ ]:


xgb = xgboost.XGBClassifier()
xgb.fit(x_train, y_train)
yhat = xgb.predict(x_test)
print("xgboost")
print("Train set Accuracy: ", metrics.accuracy_score(y_train, xgb.predict(x_train)))
print("Test set Accuracy: ", metrics.accuracy_score(y_test, yhat))


# In[ ]:


Gboost = GradientBoostingClassifier()
Gboost.fit(x_train, y_train)
yhat = Gboost.predict(x_test)
print("GradientBoostingClassifier")
print("Train set Accuracy: ", metrics.accuracy_score(y_train, Gboost.predict(x_train)))
print("Test set Accuracy: ", metrics.accuracy_score(y_test, yhat))

