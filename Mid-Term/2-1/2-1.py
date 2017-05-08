
# coding: utf-8

# In[1]:

import csv
import matplotlib.image
import matplotlib.pyplot as plt
import pandas as pd
import numpy
get_ipython().magic('matplotlib inline')

steps = pd.read_csv('avgsteps.csv')
steps


# In[2]:

sleep = pd.read_csv('avgsleep.csv')
sleep


# In[4]:

dict_step = {}
for date in pd.date_range('2016-04-01', '2016-05-20') :
    dict_step[date] = steps[steps[str(date)] > 0][str(date)].mean()
    
mean_step = pd.Series(dict_step)
mean_step


# In[5]:

plt.figure(figsize = (30, 10))
mean_step.plot()


# In[6]:

dict_sleep = {}
for date in pd.date_range('2016-04-01', '2016-05-20') :
    dict_sleep[date] = sleep[sleep[str(date)] > 0][str(date)].mean()
    
mean_sleep = pd.Series(dict_sleep)
mean_sleep


# In[7]:

plt.figure(figsize = (30, 10))
mean_sleep.plot()


# In[20]:

plt.figure(figsize = (10, 5))
plt.plot(mean_step * 2500)
plt.plot(mean_sleep)
plt.show


# In[ ]:



