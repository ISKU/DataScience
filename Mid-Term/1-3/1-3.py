
# coding: utf-8

# In[26]:

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


# In[27]:

tashu = pd.read_csv('tashu.csv')
station = pd.read_csv('station.csv')


# In[28]:

tashu['rent_date'] = pd.to_datetime(tashu['rent_date'], format = '%Y%m%d%H%M%S')


# In[29]:

tashu['year'] = pd.DatetimeIndex(tashu['rent_date']).year
tashu['month'] = pd.DatetimeIndex(tashu['rent_date']).month
tashu['day'] = pd.DatetimeIndex(tashu['rent_date']).day
tashu['hour'] = pd.DatetimeIndex(tashu['rent_date']).hour
tashu['weekday'] = pd.DatetimeIndex(tashu['rent_date']).weekday
tashu['weekday_name'] = pd.DatetimeIndex(tashu['rent_date']).weekday_name
tashu


# In[31]:

df = tashu[(tashu['weekday'] == 2)]
df2 = df[(df['hour'] == 7) | (df['hour'] == 8) | (df['hour'] == 18) | (df['hour'] == 19)]
df_am = df[(df['hour'] == 7) | (df['hour'] == 8)]
df_fm = df[(df['hour'] == 18) | (df['hour'] == 19)]


# In[32]:

result_df = df2.groupby(['rent_station', 'return_station']).size().reset_index(name = 'count')
result_am = df_am.groupby(['rent_station']).size().reset_index(name = 'count')
result_fm = df_fm.groupby(['rent_station']).size().reset_index(name = 'count')


# In[33]:

result_df = result_df.sort_values('count', ascending = False)[:5]
result_am = result_am.sort_values('count', ascending = False)[:5]
result_fm = result_fm.sort_values('count', ascending = False)[:5]


# In[34]:

result_df


# In[35]:

fig, ax = plt.subplots()
sc = plt.scatter(result_df['rent_station'], result_df['return_station'], s=result_df['count'], c = result_df['count'], marker='o', alpha=0.5)
ax.grid()
fig.colorbar(sc)
plt.show()


# In[36]:

result_am.to_csv('top5_am.csv', sep=',')
result_fm.to_csv('top5_fm.csv', sep=',')


# In[ ]:



