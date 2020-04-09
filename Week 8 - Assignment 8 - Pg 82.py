#!/usr/bin/env python
# coding: utf-8

# In[4]:


import matplotlib.pyplot as plt
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
Location = r'C:/Users/rfsas/Documents/MBA/Spring 2020 Class docs/ISM 6419 - Data Visualization/datasets/gradedata.csv'
df = pd.read_csv(Location)
df.hist(column="age", by="gender")


# In[ ]:




