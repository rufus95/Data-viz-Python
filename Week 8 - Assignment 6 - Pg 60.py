#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
Location = r'C:/Users/rfsas/Documents/MBA/Spring 2020 Class docs/ISM 6419 - Data Visualization/datasets/gradedata.csv'
df = pd.read_csv(Location)
df = df.sort_values(by=['fname', 'age', 'grade'], ascending=[True, True,True])
df.head()


# In[ ]:




