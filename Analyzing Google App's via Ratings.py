#!/usr/bin/env python
# coding: utf-8

# # Analysis of Google Play Store Dataset (2010-2018)

# Importing the libraries

# In[1]:


import pandas as pd # Used to loading files
import numpy as np # Operate with mathematical operations
import matplotlib.pyplot as plt # Used for plotting
import seaborn as sns  # Used for visualizing


# In[32]:


data = pd.read_csv("google.csv") # reading csv file


# In[3]:


data.head() # reading first five rows


# Analyzing the data

# In[4]:


data.info() # missing values in rating, type, current and android ver
            # only rating attribute contains numerical data , rest of them belong to categorical data


# In[33]:


data.boxplot() # plotted data in the form of box
               # values lies between 2.5 - 5.0
               # circle represent that data is out the range (outlier)


# # [Data Cleaning: (Pre-Processing)]

# Step-01: (Removing Outlier)

# To produce the quality result, there is a need to clean the data

# In[34]:


data[data.Rating > 5]
data.drop([10472], inplace=True) # removing the outlier from original data using inplace


# In[35]:


data[10470:10475] # checking the outlier index


# In[36]:


data.boxplot() # again plotting the data 


# Step-02: (Handlying missing values)

# In[37]:


# handling missing values
# counting the missing value from data
print(data.isnull().sum())


# Attribute: (Rating)

# In[38]:


data['Rating'].unique()


# In[40]:


# Filling missing values using Aggregate Function (mean, median or mode)
# Applying Median on Rating attribute (Categorical)
def impute_median(series):
    return series.fillna(series.median)
data.Rating= data['Rating'].transform(impute_median)
print(data.isnull().sum())


# In[41]:


data.Rating= data['Rating'].transform(impute_median)


# In[11]:


data['Rating'].dtype


# In[12]:


data.describe()


# Attribute: (Type) 

# In[13]:


data['Type'].fillna(str(data['Type'].mode().values[0]),inplace=True)


# In[14]:


data['Type'].unique()


# Attribute: (Price)

# In[15]:


data['Price'].unique()


# In[16]:


# applying lambda function to convert each value [if it has a dollar sign, remove it...otherwise data will remain the same]
data['Price']=data['Price'].apply(lambda x: str(x).replace('$','') if '$' in str(x) else (x))
# converting back the values into float value
data['Price']=data['Price'].apply(lambda x: str(x))
data['Price'] =data['Price'].astype(float)
data['Price'].dtype


# In[17]:


data['Price'].unique()


# Attribute: (Review)

# In[30]:


data['Reviews'].unique()


# In[19]:


data['Reviews'].unique()
data['Reviews'] =data['Reviews'].astype(float)
data['Reviews'].dtype


# Attribute: (Install)

# In[31]:


data['Installs'].unique()


# In[20]:


# applying lambda function to convert each value [if it has a plus and comma sign, remove it...otherwise data will remain the same]
data['Installs']=data['Installs'].apply(lambda x: str(x).replace('+','') if '+' in str(x) else (x))
data['Installs']=data['Installs'].apply(lambda x: str(x).replace(',','') if ',' in str(x) else (x))
data['Installs']=data['Installs'].apply(lambda x: str(x))
data['Installs'] =data['Installs'].astype(float)
data['Installs'].dtype


# In[21]:


data['Installs'].unique()


# In[22]:


# converting back the values into float value
data['Installs']=data['Installs'].apply(lambda x: str(x))
data['Installs'] =data['Installs'].astype(float)
data['Installs'].dtype


# Data type of Reviews, Installs, and Price is object. Converting there types into float to further analyze the data.

# In[23]:


data.describe()


# Exploring the Data

# In[24]:


data.corr() #returns correlation


# In[25]:


grp = data.groupby('Category')
x = grp['Rating'].agg(np.mean)
y = grp['Reviews'].agg(np.mean)
z = grp['Price'].agg(np.mean)
print(x)
print(y)
print(z)


# Category and Rating

# In[26]:


plt.figure(figsize=(15,5))
plt.plot(x, 'r--', color='r')
plt.xticks(rotation=90)
plt.title('Category wise Rating')
plt.xlabel('Categories')
plt.ylabel('Rating')
plt.show()


# Category and Reviews

# In[27]:


plt.figure(figsize=(15,5))
plt.plot(y, 'r--', color='g')
plt.xticks(rotation=90)
plt.title('Category wise Reviews')
plt.xlabel('Categories')
plt.ylabel('Reviews')
plt.show()


# Category and Pricing

# In[28]:


plt.figure(figsize=(15,5))
plt.plot(z, 'r--', color='b')
plt.xticks(rotation=90)
plt.title('Category wise Pricing')
plt.xlabel('Categories')
plt.ylabel('Pricing')
plt.show()

