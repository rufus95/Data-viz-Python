#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
Location = r"C:\Users\rfsas\Documents\MBA\Spring 2020 Class docs\ISM 6419 - Data Visualization\week 7\datasets\gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[2]:


import numpy as np
df['isbusy'] = np.where((df['exercise']>3)
& (df['hours'] > 17),'busy', 'not busy')
df.tail(10)


# In[ ]:




