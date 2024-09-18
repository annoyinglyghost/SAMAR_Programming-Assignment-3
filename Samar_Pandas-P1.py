#!/usr/bin/env python
# coding: utf-8

# ## Problem 1
# 

# #### Using knowledge obtained from the experiment and demonstrations:

# a. Load the corresponding .csv file into a data frame named cars using pandas

# In[2]:


import pandas as pd


# In[14]:


#Read the csv file into the data fram
file = pd.read_csv('C:/Users/Iszz/Documents/Python Codes/PA3/cars.csv')
#Print file
file


# b. Display the first five and last five rows of the resulting cars.

# In[250]:


#Displaying the first five rows of the resulting cars
file.head(5)


# In[252]:


#Displaying the last five rows of the resulting cars
file.tail(5)


# In[254]:


file


# In[ ]:




