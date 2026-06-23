import pandas as pd 

df=pd.read_csv("dataset.csv",encoding="latin1")
print(df.head())
print(df.info())

print(df.isnull().sum())
df=df.drop_duplicates()
df['Order Date']=pd.to_datetime(df['Order Date'])
df['Ship Date']=pd.to_datetime(df['Ship Date'])

print("Total Sales:",df['Sales'].sum())
print("Total Profit:",df['Profit'].sum())

top_states=df.groupby('State')['Sales'].sum().sort_values(ascending=False).head(10)
top_states

import matplotlib.pyplot as plt 
import seaborn as sns
plt.figure(figsize=(8,5))
sns.barplot(
    x=df.groupby('Category')['Sales'].sum().index,
    y=df.groupby('Category')['Sales'].sum().values
)
plt.title("Sales by Category")
plt.show()

category_profit=df.groupby("Category")['Profit'].sum()
plt.figure(figsize=(8,5))
category_profit.plot(kind='bar',color='green')
plt.title("Profit by Category")
plt.ylabel("Profit")
plt.show()

plt.figure(figsize=(6,4))
sns.heatmap(
    df[['Sales','Quantity','Discount','Profit']].corr(),
    annot=True,
    cmap='coolwarm'
)
plt.title("Correlation Heatmap")
plt.show()

df['Month']=df['Order Date'].dt.to_period('M')
monthly_sales=df.groupby('Month')['Sales'].sum()

monthly_sales.plot(figsize=(12,5))
plt.title("Monthly Sales Trend")
plt.ylabel("Slaes")
plt.show()