#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
Location = r'C:/Users/rfsas/Documents/MBA/Spring 2020 Class docs/ISM 6419 - Data Visualization/datasets/gradedata.csv'
df = pd.read_csv(Location)
df.tail()


# In[2]:


df.take(np.random.permutation(len(df))[:500])


# In[ ]:




