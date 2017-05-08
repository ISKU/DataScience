
# coding: utf-8

# In[15]:

import csv
import matplotlib.image
import matplotlib.pyplot as plt
import collections
import pandas as pd
import pylab
import datetime
import numpy
from operator import itemgetter
import gmaps
gmaps.configure(api_key = 'AIzaSyDmH5pACzSkC7if9jpNEzmEoXdtbR8wFmw')

get_ipython().magic('matplotlib inline')
matplotlib.rc('font', family = 'nanumgothic')


# In[16]:

tashu = pd.read_csv('tashu.csv')
station = pd.read_csv('station.csv')


# In[19]:

tashu['rent_date'] = pd.to_datetime(tashu['rent_date'], format = '%Y%m%d%H%M%S')


# In[21]:

ts = pd.Series(1, tashu['rent_date'])


# In[22]:

daily_ts = ts.resample('D').count()


# In[28]:

plt.figure(figsize = (15, 15))
daily_ts.plot()
plt.show()


# In[ ]:



