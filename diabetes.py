#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
db_data = pd.read_csv("diabetes.csv")


# In[3]:


db_data.head()


# In[11]:




db_data["Glucose"].describe()


# In[4]:


print(db_data)


# In[12]:


db_data.iloc[0]


# In[13]:


def getIndexes(dfObj, value):
    ''' Get index positions of value in dataframe i.e. dfObj.'''
    listOfPos = list()
    # Get bool dataframe with True at positions where the given value exists
    result = dfObj.isin([value])
    # Get list of columns that contains the value
    seriesObj = result.any()
    columnNames = list(seriesObj[seriesObj == True].index)
    # Iterate over list of columns and fetch the rows indexes where value exists
    for col in columnNames:
        rows = list(result[col][result[col] == True].index)
        for row in rows:
            listOfPos.append((row, col))
    # Return a list of tuples indicating the positions of value in the dataframe
    return listOfPos


# In[29]:


db_data['Glucose'].mean()


# In[30]:


db_data[db_data['Glucose']>= 120.89453125]


# In[31]:


db_data['BloodPressure'].median()


# In[40]:


db_data['BMI'].mode()


# In[46]:


db_data[[db_data['BloodPressure']==72][db_data[db_data['BMI']>=32.0]]]


# In[44]:


db_data[db_data['BMI']>=32.0]


# In[51]:


db_data[(db_data['BloodPressure']==72) & (db_data['BMI']<32)]


# In[ ]:


print(df[(df['D']<0) & (df['A']>0)])

