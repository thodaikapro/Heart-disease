#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd

import warnings
warnings.filterwarnings('ignore')

import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv(r'dataset_heart.csv')
df.head()


# In[3]:


df.shape


# In[4]:


df.info()


# In[5]:


df.describe()


# In[27]:


df.columns


# In[32]:


cols = ['age', 'sex ', 'chest pain type', 'resting blood pressure',
       'serum cholestoral', 'fasting blood sugar',
       'resting electrocardiographic results', 'max heart rate',
       'exercise induced angina', 'oldpeak', 'ST segment', 'major vessels',
       'thal', 'heart disease']

n_rows = 2
n_cols = 7
o = 0

fig, ax = plt.subplots(n_rows, n_cols, figsize = (25, 17))

for r in range(n_rows):
    for c in range(n_cols):
        i = r*n_cols + r
        o +=1
        if i<len(cols):
            ax_i = ax[r,c]
            sns.countplot(data = df, x = cols[o-1], palette = 'colorblind', ax = ax_i)
#         print (o)


# In[38]:


cat_cols = ['sex ', 'chest pain type', 'fasting blood sugar',
       'resting electrocardiographic results', 'exercise induced angina', 'ST segment', 'major vessels',
       'thal', 'heart disease']
for col in cat_cols:
    df[col] = df[col].astype(str)


# In[39]:


df.info()


# In[40]:


num_cols = [col for col in cols if df[col].dtype != 'object']

print (num_cols)


# In[47]:


cat1 = ['sex ', 'chest pain type', 'fasting blood sugar',
       'resting electrocardiographic results', 'exercise induced angina', 'ST segment', 'major vessels',
       'thal']
n_rows = 2
n_cols = 3
o = 0

fig, ax = plt.subplots(n_rows, n_cols, figsize = (25, 17))

for r in range(n_rows):
    for c in range(n_cols):
        i = r*n_cols + r
        o +=1
        if i<len(cat1):
            ax_i = ax[r,c]
            sns.countplot(data = df, x = cat1[o-1], palette = 'colorblind', ax = ax_i, hue = 'heart disease')
#         print (o)


# In[53]:


plt.figure(figsize = (15, 20))
plotnumber = 1

for col in num_cols:
    if plotnumber <= len(num_cols):
        ax = plt.subplot(1, 5, plotnumber)
        sns.distplot(df[col])
        plt.xlabel(col)
        
    plotnumber +=1


# In[56]:


sns.pairplot(data = df[['age', 'resting blood pressure', 'serum cholestoral', 'max heart rate', 'oldpeak', 'heart disease']], hue = 'heart disease', corner = True)


#   -- 1. age       
#   -- 2. sex       
#   -- 3. chest pain type  (4 values)       
#   -- 4. resting blood pressure  
#   -- 5. serum cholestoral in mg/dl      
#   -- 6. fasting blood sugar > 120 mg/dl       
#   -- 7. resting electrocardiographic results  (values 0,1,2) 
#   -- 8. maximum heart rate achieved  
#   -- 9. exercise induced angina    
#   -- 10. oldpeak = ST depression induced by exercise relative to rest   
#   -- 11. the slope of the peak exercise ST segment     
#   -- 12. number of major vessels (0-3) colored by flourosopy        
#   -- 13. thal: 3 = normal; 6 = fixed defect; 7 = reversable defect
#   -- 14. Target(Absence (1) or presence (2) of heart disease) 

# In[ ]:




