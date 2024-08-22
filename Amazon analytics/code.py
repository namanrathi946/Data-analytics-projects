import pandas as pd
# Load the dataset
file_path = '/Users/namanrathi946/Downloads/Amazon Sales data.csv'
df = pd.read_csv(file_path)

# Display basic information
print(df.info())
print(df.describe())
print(df.head())

# Convert 'Order Date' column to datetime type
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Extract useful information from the 'Order Date' column
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month
df['Day'] = df['Order Date'].dt.day

import matplotlib.pyplot as plt
import seaborn as sns

# Monthly Sales Trend using 'Total Revenue' as the sales data
monthly_sales = df.groupby(['Year', 'Month'])['Total Revenue'].sum().reset_index()

plt.figure(figsize=(12,6))
sns.lineplot(data=monthly_sales, x='Month', y='Total Revenue', hue='Year')
plt.title('Monthly Sales Trend')
plt.show()

# Yearly Sales Trend
yearly_sales = df.groupby('Year')['Total Revenue'].sum()

plt.figure(figsize=(8,5))
yearly_sales.plot(kind='bar', color='skyblue')
plt.title('Yearly Sales')
plt.show()

import plotly.express as px

# Animated Sales Trend using 'Total Revenue'
fig = px.line(monthly_sales, x='Month', y='Total Revenue', color='Year', title='Monthly Sales Trend (Animated)',
              labels={'Total Revenue':'Sales in $', 'Month':'Month'}, 
              animation_frame='Year', animation_group='Month')

fig.show()

import numpy as np
import seaborn as sns

# Correlation matrix for numeric columns only
numeric_df = df.select_dtypes(include=[np.number])
corr_matrix = numeric_df.corr()

plt.figure(figsize=(10,6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# Summary of descriptive statistics for numeric columns
descriptive_stats = df.describe()
print(descriptive_stats)

# Histogram for visualizing the distribution of 'Total Revenue'
plt.figure(figsize=(10, 6))
sns.histplot(df['Total Revenue'], kde=True)
plt.title('Distribution of Total Revenue')
plt.show()

# Box plot for 'Total Revenue'
plt.figure(figsize=(10, 6))
sns.boxplot(x=df['Total Revenue'])
plt.title('Box Plot of Total Revenue')
plt.show()

# Scatter plot of 'Total Revenue' vs 'Total Profit'
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Total Revenue', y='Total Profit', data=df)
plt.title('Total Revenue vs Total Profit')
plt.show()


