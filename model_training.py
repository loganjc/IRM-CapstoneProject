#!/usr/bin/env python
# coding: utf-8

# In[124]:


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn import metrics
from sklearn import datasets
from joblib import dump


# In[ ]:


'''
This module takes in the processed data frame created by the Preprocessing module and uses the data to train machine learning
models for category classification.

The module is not intended for use except for the purposes of modifying the machine learning models and classification
pipeline.

This module outputs a serialized classification model for use in the Main module.
'''


# In[69]:


#import data frame created in preprocessing.py
df = pd.read_json('treated_data.json')


# In[79]:


#Lemmas train/ test data split
X = df['utterance']
y = df['category']
X_lemma_train, X_lemma_test, y_lemma_train, y_lemma_test = train_test_split(X,y, stratify= df[['category']], test_size=0.33, random_state=42)


# In[80]:


#Vector norms train/ test data split
X = df['semantic_value_vec_norm']
y = df['category']
X_norm_train, X_norm_test, y_norm_train, y_norm_test = train_test_split(X.values.reshape(-1,1),                                                                        y.values.reshape(-1,1),                                                                        stratify= df[['category']], test_size=0.33, random_state=42)


# In[81]:


#Vector arrays train/test data split
X = df['semantic_value']
y = df['category']
X_vect_train, X_vect_test, y_vect_train, y_vects_test = train_test_split(X,y, stratify= df[['category']], test_size=0.33, random_state=42)


# In[82]:


#TFIDF vectorizer pipeline object
tfidf_lsvc = Pipeline([('tfidf', TfidfVectorizer()),('clf', LinearSVC())])


# In[90]:


#vector arrays svc 
vects_lsvc = Pipeline([('standardScaler',StandardScaler()), ('linearSVC', LinearSVC())])
#vects_lvsc = LinearSVC()


# In[84]:


#Vector norm svc
norm_lsvc = LinearSVC()


# In[85]:


#Fit models
tfidf_lsvc.fit(X_lemma_train, y_lemma_train)


# In[107]:


#vects_lsvc.fit(X_vect_train, y_vect_train)


# In[108]:


#norm_lsvc.fit(X_norm_train, y_norm_train.ravel())


# In[36]:


#Predictions for test data
predictions_lemm = tfidf_lsvc.predict(X_lemma_test)
predictions_norm = norm_lsvc.predict(X_norm_test)


# In[37]:


print(metrics.confusion_matrix(y_lemma_test,predictions_lemm))


# In[38]:


print(metrics.classification_report(y_lemma_test,predictions_lemm))


# In[126]:


#Model persitience
#save the tfidf lsvc to be loaded into interface module
with open('fitted_model.txt' , 'wb') as f:
    dump(tfidf_lsvc, f)

