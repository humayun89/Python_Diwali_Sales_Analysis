
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
# visualizing data %matplotlib inline
import seaborn as sns

# import csv file
df = pd.read_csv('Diwali Sales Data.csv', encoding= 'unicode_escape')

df.shape
print(df.shape)
df.head()
print(df.head())
df.info()
print(df.info())

#drop unrelated/blank columns
df.drop(['Status', 'unnamed1'], axis=1, inplace=True)
#check for null values
pd.isnull(df).sum()
print(pd.isnull(df).sum())
# drop null values
df.dropna(inplace=True)
print(df.dropna(inplace=True))


# change data type
df['Amount'] = df['Amount'].astype('int')