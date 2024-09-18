#!/usr/bin/env python
# coding: utf-8

# ## Problem 2

# #### Using the dataframe cars in problem 1, extract the following information using subsetting, <br> slicing and indexing operations..

# In[13]:


import pandas as pd


# In[15]:


#Read the csv file into the data fram
file = pd.read_csv('C:/Users/Iszz/Documents/Python Codes/PA3/cars.csv')


# a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.ted
# 

# In[48]:


#Showing only the first five rows with odd-numbered columns
file[1::2].head(5)


# b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.

# In[31]:


#Displaying the row that contains the 'Model' of 'Mazda RX4'
file.loc[file['Model'] == 'Mazda RX4']


# c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?

# In[45]:


#Filter for finding how many cylinders the 'Camaro Z28' have
camaro = file[file['Model'] == 'Camaro Z28']['cyl'].values[0]

#Printing the result
print(f"The Camaro Z28 has {camaro} cylinders.")


# d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

# In[41]:


#List of the car models to be filtered
str = ['Mazda RX4', 'Ford Pantera L', 'Honda Civic']
#Filter the data frame with the specific car models and select only the cyl and gear columns
file[file['Model'].isin(str)][['Model', 'cyl', 'gear']] 

