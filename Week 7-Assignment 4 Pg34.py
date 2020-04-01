#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
Location = r"C:\Users\rfsas\Documents\MBA\Spring 2020 Class docs\ISM 6419 - Data Visualization\week 7\datasets\gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[2]:


bins = [0, 60, 70, 80, 90, 100]
group_names = ['F', 'D', 'C', 'B', 'A']
df['lettergrade'] = pd.cut(df['grade'], bins,
labels=group_names)
df


# In[3]:


pd.value_counts(df['lettergrade'])


# In[4]:


bins = [0,80,100]
group_names = ['fail', 'pass']
df['Pass/Fail'] = pd.cut(df['grade'], bins,
labels=group_names)
df


# In[ ]:




