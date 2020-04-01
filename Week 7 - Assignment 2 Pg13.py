#!/usr/bin/env python
# coding: utf-8

# In[28]:


import pandas as pd
import numpy as np
import glob
import os


# In[29]:


Location = r'C:\Users\rfsas\Documents\MBA\Spring 2020 Class docs\ISM 6419 - Data Visualization\week 7\datasets\weekly_call_data'


# In[30]:


all_files = glob.glob(os.path.join(Location, "*.xlsx"))


# In[31]:


df_from_each_file = (pd.read_excel(f) for f in all_files)


# In[33]:


concatenated_df   = pd.concat(df_from_each_file, ignore_index=True)


# In[34]:


concatenated_df.head()


# In[ ]:




