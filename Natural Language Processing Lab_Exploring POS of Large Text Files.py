#!/usr/bin/env python
# coding: utf-8

# # `BERCHMANS KEVIN S`
# 

# ## Natural Language Processing Lab
# ##  `Exploring POS of Large Text Files`

# In[1]:


txt1 = open("12 Angry Men.txt", "r")
txt1 = txt1.read()
print(txt1) 


# In[ ]:


import glob
import nltk
import pandas as pd
from nltk import *
from zipfile import ZipFile
from nltk.corpus import stopwords


import nltk
nltk.download('stopwords')
nltk.download('punkt')
stop_words = set(stopwords.words('english'))


# #### a. How many sentences in the files??

# In[3]:


from nltk.tokenize import sent_tokenize
sentences=sent_tokenize(txt1)
len(sentences)


# #### b. How many words in the file??

# In[4]:


from nltk.tokenize import word_tokenize
words_in = nltk.tokenize.WhitespaceTokenizer()
words = words_in.tokenize(txt1)
len(words)


# #### c. What are the top 10 words and their counts??

# In[5]:


top_10 = FreqDist(words)
top_10.most_common(10)


# #### d. How many different POS tags are represented in this file??

# In[6]:


nltk.download('averaged_perceptron_tagger')

tag = []
d_tags = []
words = [w for w in words if not w in stop_words] 
tagged = nltk.pos_tag(words)

for i in tagged:
    (word,pos)=i
    tag.append(pos)
    
for j in tag:
    if j not in d_tags:
        d_tags.append(j)
        
len(d_tags)


# #### e. What are the top 10 POS tags and their counts??

# In[7]:


top_pos = FreqDist(tagged)
top_pos.most_common(10)


# #### f. How many nouns in the file??

# In[8]:


noun=0
for i in top_pos.keys():
    (word,pos)=i
    if pos == 'NN' or pos == 'NNS' or pos == 'NNP' or pos == 'NNPS':
        noun+=1
        
print(noun)


# #### g. How many verbs in the file??

# In[9]:


verbs=0
for i in top_pos.keys():
    (word,pos)=i
    if pos == 'VB' or pos == 'VBD' or pos == 'VBN' or pos == 'VBP' or pos == 'VBZ':
        verbs+=1
        
print(verbs)


# #### h. How many adjectives in the file??

# In[10]:


adj = []

for i in top_pos.keys():
    (word,pos)=i
    if pos == 'JJ' or pos == 'JJR' or pos == 'JJS':
        adj.append(i)
        
len(adj) 


# #### i. How many adverbs in the file??

# In[11]:


adv=[]

for i in top_pos.keys():
    (word,pos)=i
    if pos == 'RB' or pos == 'RBR' or pos == 'RBS' or pos == 'BP':
        adv.append(i)
        
len(adv)


# #### j. What is the most frequent adverb??

# In[12]:


adv = FreqDist(adv)
adv.most_common(1)


# #### k. What is the most frequent adjective??

# In[13]:


adj = FreqDist(adj)
adj.most_common(1)

