
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
file_path = './data/Sample-Superstore.csv'
df = pd.read_csv(file_path, encoding='ISO-8859-1')

# Display basic info
print("First 5 rows:")
print(df.head())

print("\nData Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nUnique Values per Column:")
print(df.nunique())

# Plot - Category count
plt.figure(figsize=(6,3))
sns.countplot(data=df, x='Category', order=df['Category'].value_counts().index)
plt.title("Category Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Total Sales by State
sales_by_state = df.groupby('State')['Sales'].sum().sort_values(ascending=False)
plt.figure(figsize=(12,6))
sales_by_state.plot(kind='bar', color='skyblue')
plt.title('Total Sales by State')
plt.xlabel('State')
plt.ylabel('Total Sales')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Top 10 Products by Sales and Profit
top_sales = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)
top_profit = df.groupby('Product Name')['Profit'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))
top_sales.plot(kind='bar', color='orange')
plt.title('Top 10 Products by Sales')
plt.xticks(rotation=75)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10,5))
top_profit.plot(kind='bar', color='purple')
plt.title('Top 10 Products by Profit')
plt.xticks(rotation=75)
plt.tight_layout()
plt.show()
