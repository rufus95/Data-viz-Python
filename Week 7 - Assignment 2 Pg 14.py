#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from sqlalchemy import create_engine


# In[3]:


# Connect to sqlite db
db_file = r'C:\Users\rfsas\Documents\MBA\Spring 2020 Class docs\ISM 6419 - Data Visualization\week 7\datasets\salesdata.db'
engine = create_engine(r"sqlite:///{}".format(db_file))


# In[4]:


sql = "select name from sqlite_master"    
"where type = 'table';"
test = pd.read_sql(sql, engine)


# In[8]:


test


# In[ ]:




