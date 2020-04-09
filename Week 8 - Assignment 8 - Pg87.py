#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
Location = r'C:/Users/rfsas/Documents/MBA/Spring 2020 Class docs/ISM 6419 - Data Visualization/datasets/gradedata.csv'
df = pd.read_csv(Location)
plt.scatter(df['hours'], df['grade'])


# In[ ]:




