#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import numpy as np
Location = r'C:/Users/rfsas/Documents/MBA/Spring 2020 Class docs/ISM 6419 - Data Visualization/datasets/gradedata.csv'
df = pd.read_csv(Location)
df['MF'] = np.where((df['gender']=='female') ,'1', '0')
df.tail(10)


# In[12]:


import statsmodels.formula.api as sm
result = sm.ols(formula='grade ~ age + exercise + hours',data=df).fit()
result.summary()


# In[13]:


import statsmodels.formula.api as sm
result = sm.ols(formula='grade ~ age + exercise + hours + MF',data=df).fit()
result.summary()


# In[ ]:




