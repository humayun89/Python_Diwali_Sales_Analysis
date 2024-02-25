import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
# visualizing data matplotlib inline
import seaborn as sns

# Import CSV file
df = pd.read_csv('Diwali Sales Data.csv', encoding='unicode_escape')

# Display basic information about the dataset
print(df.shape)
print(df.head())
print(df.info())

# Drop unrelated/blank columns
df.drop(['Status', 'unnamed1'], axis=1, inplace=True)

# Check for null values
print(pd.isnull(df).sum())

# Drop null values
df.dropna(inplace=True)

# Change data type
df['Amount'] = df['Amount'].astype('int')

# Rename the 'Marital_Status' column
df.rename(columns={'Marital_Status': 'Shaadi'}, inplace=True)

# Descriptive statistics of the dataset
print(df.describe())

# Exploratory Data Analysis
# Plotting a bar chart for Gender and its count
ax = sns.countplot(x='Gender', data=df)
for bars in ax.containers:
    ax.bar_label(bars)

# Plotting a bar chart for gender vs total amount
sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(x='Gender', y='Amount', data=sales_gen)

# Age
ax = sns.countplot(data=df, x='Age Group', hue='Gender')
for bars in ax.containers:
    ax.bar_label(bars)

# Total Amount vs Age Group
sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(x='Age Group', y='Amount', data=sales_age)

# State
# Total number of orders from top 10 states
sales_state_orders = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
sns.barplot(data=sales_state_orders, x='State', y='Orders')

# Total amount/sales from top 10 states
sales_state_amount = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
sns.barplot(data=sales_state_amount, x='State', y='Amount')

# Marital Status
ax = sns.countplot(data=df, x='Marital_Status')
for bars in ax.containers:
    ax.bar_label(bars)

# Sales by Marital Status and Gender
sales_marital_gender = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(data=sales_marital_gender, x='Marital_Status', y='Amount', hue='Gender')

# Occupation
ax = sns.countplot(data=df, x='Occupation')
for bars in ax.containers:
    ax.bar_label(bars)

# Sales by Occupation
sales_occupation = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(data=sales_occupation, x='Occupation', y='Amount')

# Product Category
ax = sns.countplot(data=df, x='Product_Category')
for bars in ax.containers:
    ax.bar_label(bars)

# Sales by Product Category
sales_category = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
sns.barplot(data=sales_category, x='Product_Category', y='Amount')

# Top 10 most sold products
fig1, ax1 = plt.subplots(figsize=(12, 7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')

# Conclusion
print("Married women aged 26-35 from Uttar Pradesh, Maharashtra, and Karnataka working in IT, Healthcare, and Aviation are more likely to buy products from Food, Clothing, and Electronics categories.")
