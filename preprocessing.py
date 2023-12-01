#!/usr/bin/env python
# coding: utf-8

# In[1]:


import spacy
import pandas as pd
import numpy
from text_processing import Text_Pre_Processor


# In[ ]:


'''
Module dedicated to treating text data from the Bittext dataset.

Relies on text_processing.py

Treats text data and adds SpaCy semantic vector data to data frame for export and use in model training.

'''


# In[2]:


nlp = spacy.load('en_core_web_md')


# In[3]:


filename = 'dataset\8000_utterances.csv'


# In[10]:


df = pd.read_csv(filename)


# In[11]:


#preprocess text into lemmas, add semantic vector data into dataframe per entry, export into new dataframe

text_processor = Text_Pre_Processor(nlp)

#add new column to dataframe:
df.insert(len(df.columns), 'semantic_value', pd.Series([[1, 2, 3], 'a'], dtype=object))

df['semantic_value_vec_norm'] = 0

for i, text in enumerate(df.loc[:, 'utterance']):
    doc = text_processor.process(text)
    new_utterance = []
    for token in doc:
        new_utterance.append(token.text)
    df.at[i, 'utterance'] = ' '.join(new_utterance)
    df.at[i, 'semantic_value'] = doc.vector
    df.at[i, 'semantic_value_vec_norm'] = doc.vector_norm
    
#export treated DF for use in next steps
df.to_json('treated_data.json')
print("data exported sucessfully")

