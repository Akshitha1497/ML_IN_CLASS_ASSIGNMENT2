#!/usr/bin/env python
# coding: utf-8

# Question 1

# In[21]:


import numpy as np
arr = np.random.randint(1,20,15)
print("Array:")
print(arr)
newarr = arr.reshape(3, 5)
print(newarr)
print("Array shape:")
print(reshape_arr.shape)
maxrows=np.amax(newarr, axis = 1)
for i in range(0,3):
 for j in range(0,5):
    if(newarr[i, j]==maxrows[i]):
       newarr[i, j]=0
print("Max value replaced by 0: ")
print(newarr)


# In[ ]:


Question 2


# In[30]:


import pandas as pd

data = pd.read_csv("C:\Akshitha_ML@\data.csv")
data


# In[5]:


data.describe()


# In[6]:


data.isnull().any()


# In[7]:


data.fillna(data.mean(), inplace=True)
data.isnull().any()


# In[26]:


data.agg({'Pulse':['min','max','count','mean'],'Maxpulse':['min','max','count','mean']})


# In[9]:


data.loc[(data['Calories']>500)&(data['Calories']<1000)]


# In[10]:


data.loc[(data['Calories']>500)&(data['Pulse']<100)]


# In[11]:


df_modified = data[['Duration','Pulse','Calories']]
df_modified.head()


# In[28]:


del data['Maxpulse']


# In[29]:


data.head()


# In[14]:


data.dtypes


# In[15]:


data['Calories'] = data['Calories'].astype(np.int64)
data.dtypes


# In[16]:


data.plot.scatter(x='Duration',y='Calories',c='DarkBlue')


# Question 3

# In[31]:


import matplotlib.pyplot as plt
# Data to plot
languages = 'Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]
# explode 1st slice
explode = (0.1, 0, 0, 0,0,0)  
# Plot
plt.pie(popuratity, explode=explode, labels=languages, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()


# In[ ]:





# In[ ]:




