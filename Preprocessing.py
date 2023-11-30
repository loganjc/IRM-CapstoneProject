#!/usr/bin/env python
# coding: utf-8

# In[27]:


import spacy
import pandas as pd
import numpy
import string
import text_processing


# In[28]:


nlp = spacy.load('en_core_web_md')


# In[29]:


filename = 'dataset\8000_utterances.csv'


# In[30]:


df = pd.read_csv(filename)


# In[31]:


#preprocess text into lemmas, add semantic vector data into dataframe per entry, export into new dataframe

text_processor = text_processing.Text_Pre_Processor(nlp)
#add new column to dataframe:
#df['semantic_value'] = 0.0
df.insert(len(df.columns), 'semantic_value', pd.Series([[1, 2, 3], 'a'], dtype=object))

df['semantic_value_vec_norm'] = 0

#for i, text in enumerate(df.loc[:, 'utterance']):
for i, text in enumerate(df.loc[0:5, 'utterance']):
    doc = text_processor.process(text)
    new_utterance = []
    for token in doc:
        new_utterance.append(token.text)
    df.at[i, 'utterance'] = ' '.join(new_utterance)
    
    #Cannot put array into df cell. Could convert to str and then back to list for sklearn?
    df.at[i, 'semantic_value'] = doc.vector
    
    df.at[i, 'semantic_value_vec_norm'] = doc.vector_norm
    
#export treated DF for use in next steps
df.to_json('treated_data.json')

