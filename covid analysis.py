#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importing libraries
import pandas as pd
import numpy as np


# In[2]:


# loading data from the source:
confirmed_df = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv")
death_df = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv")
recovered_df = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv")
country_df = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/web-data/data/cases_country.csv")


# In[3]:


confirmed_df.head()


# In[4]:


#death_df.head()


# In[5]:


#recovered_df.head()


# In[6]:


#country_df.head()


# In[7]:


# data cleaning

# converting df column names to lowercase

country_df.columns = map(str.lower, country_df.columns)
confirmed_df.columns = map(str.lower, confirmed_df.columns)
death_df.columns = map(str.lower, death_df.columns)
recovered_df.columns = map(str.lower, recovered_df.columns)


# In[8]:


# changing province/state to state and country/region to country
confirmed_df = confirmed_df.rename(columns={'province/state': 'state', 'country/region': 'country'})
recovered_df = confirmed_df.rename(columns={'province/state': 'state', 'country/region': 'country'})
death_df = death_df.rename(columns={'province/state': 'state', 'country/region': 'country'})
country_df = country_df.rename(columns={'country_region': 'country'})


# In[12]:


## conda install -c https://conda.anaconda.org/plotly plotly  (use this if plotply is not installed in your system)
import plotly.express as px
sorted_country_df = country_df.sort_values('confirmed', ascending= False)
fig= px.bar(
    sorted_country_df.head(10),
    x = "country",
    y = "confirmed",
    title= "Top 10 worst affected countries", # the axis names
    color = "country", 
    height=500,
    width=800
)
fig.update_layout(template='plotly_dark')
fig.show()


# In[14]:


country_df.drop(['lat', 'long_', 'last_update'], axis=1).sort_values('confirmed', ascending = False).reset_index(drop=True).style.bar(align='left', width=98, color='green')


# In[ ]:




