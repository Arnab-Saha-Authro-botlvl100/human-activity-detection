# -*- coding: utf-8 -*-
"""422_group_4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jfGWu7flTRIbjekm9HhBmcda8MggXQQ1

Group 4




**Topic: Human Activity Recognition**

**Data Processing**
"""

import numpy as np
import pandas as pd
import sklearn
from sklearn.datasets import load_iris

train = pd.read_csv("/content/train.csv")
test = pd.read_csv("/content/test.csv")
train.head()

train.shape

train.isnull()

train['Activity'].unique()

train = train.sort_values(["Activity"], ascending=True)
test = test.sort_values(["Activity"], ascending=True)

test

from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

plt.figure(figsize=(12,6))
axis=sns.countplot(x="Activity",data=train)
plt.xticks(x=train['Activity'],rotation='vertical')
plt.show()

plt.figure(figsize=(12,6))
axis=sns.countplot(x="Activity",data=test)
plt.xticks(x=test['Activity'],rotation='vertical')
plt.show()

# def label_encoder(x):
# 'STANDING': return 2
#  'SITTING': return 1
#  'LAYING': return 0
# 'WALKING': return 3
# 'WALKING_DOWNSTAIRS': return 4
# 'WALKING_UPSTAIRS' retun 5
#     else: return 1

train_new = train
test_new = test
for i in list(train.columns.values):
  # print(i)
  train_new[i] = LabelEncoder().fit_transform(train[i])
  # test_new[i] = LabelEncoder().fit_transform(test[i])

train_new

test_new = test
for i in list(test.columns.values):
  test_new[i] = LabelEncoder().fit_transform(test[i])

test_new

train_new.isnull().sum()

test_new.isnull().sum()

# input train
train_x = train_new.iloc[:,0:-1]
# output train
train_y = train_new.iloc[:,-1]

# test input
test_x = test_new.iloc[:,0:-1]
# test output
test_y = test_new.iloc[:,-1]
train_y

from sklearn import preprocessing
temp_x = preprocessing.normalize(train_x)
temp_t_x = preprocessing.normalize(test_x)
temp_x

"""**SVC (SUPPORT VECTOR MACHINE)**

"""

from sklearn.svm import SVC
model = SVC()
model.fit(temp_x, train_y)

print(model.score(temp_t_x, test_y)*100,"%")

"""**Logistic Regression**"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(temp_x, train_y, test_size = 0.25, random_state = 0)

from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
xtrain = sc_x.fit_transform(X_train)
xtest = sc_x.transform(X_test)
 
print (xtrain[0:10, :])

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(xtest)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
 
print ("Confusion Matrix : \n", cm)

from sklearn.metrics import accuracy_score
print ("Accuracy : ", accuracy_score(y_test, y_pred))