#!/usr/bin/env python
# coding: utf-8

# In[57]:


import pandas as pd
import matplotlib.pyplot as plt
Location = r'C:/Users/rfsas/Desktop/Top 10 corona - Florida.xlsx'
df_cases = pd.read_excel(Location)
d1 = df_cases.groupby(['County']).sum()
d1.plot.bar(title='Top 10 counties of Corona cases in Florida')


# In[ ]:




