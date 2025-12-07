# Data Analysis Basics - Working with numerical data
# Note: Install required libraries: pip install pandas numpy matplotlib

# NUMPY - Numerical computing

import numpy as np

# Creating arrays
arr1 = np.array([1, 2, 3, 4, 5])
print(f"1D array: {arr1}")

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(f"2D array:\n{arr2}")

# Array properties
print(f"Shape: {arr2.shape}")      # (2, 3)
print(f"Dimensions: {arr2.ndim}")  # 2
print(f"Size: {arr2.size}")        # 6
print(f"Data type: {arr2.dtype}")  # int64

# Creating special arrays
zeros = np.zeros((3, 3))
ones = np.ones((2, 4))
identity = np.eye(3)  # Identity matrix
range_arr = np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]
linspace = np.linspace(0, 1, 5)  # 5 evenly spaced values

# Random arrays
random_arr = np.random.rand(3, 3)  # Uniform [0, 1)
normal_arr = np.random.randn(3, 3)  # Normal distribution
randint_arr = np.random.randint(1, 100, (3, 3))

# Array operations
arr = np.array([1, 2, 3, 4, 5])

# Element-wise operations
print(arr + 10)    # [11, 12, 13, 14, 15]
print(arr * 2)     # [2, 4, 6, 8, 10]
print(arr ** 2)    # [1, 4, 9, 16, 25]

# Mathematical functions
print(np.sqrt(arr))
print(np.exp(arr))
print(np.log(arr))

# Statistical operations
print(f"Mean: {arr.mean()}")
print(f"Median: {np.median(arr)}")
print(f"Std: {arr.std()}")
print(f"Min: {arr.min()}")
print(f"Max: {arr.max()}")
print(f"Sum: {arr.sum()}")

# Array indexing and slicing
arr = np.array([10, 20, 30, 40, 50])
print(arr[0])      # 10
print(arr[-1])     # 50
print(arr[1:4])    # [20, 30, 40]

# Boolean indexing
arr = np.array([1, 2, 3, 4, 5])
mask = arr > 2
print(arr[mask])   # [3, 4, 5]

# 2D array indexing
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[0, 1])     # 2 (row 0, col 1)
print(arr2d[:, 1])     # [2, 5, 8] (all rows, col 1)
print(arr2d[0, :])     # [1, 2, 3] (row 0, all cols)

# Reshaping
arr = np.arange(12)
reshaped = arr.reshape(3, 4)
print(reshaped)

flattened = reshaped.flatten()
print(flattened)


# PANDAS - Data manipulation and analysis

import pandas as pd

# Creating Series (1D labeled data)
s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print(s)
print(s['b'])  # 20

# Creating DataFrame (2D labeled data)
data = {
    'name': ['Peter', 'Sarah', 'Mike', 'Lisa'],
    'age': [25, 30, 35, 28],
    'salary': [50000, 60000, 75000, 55000]
}
df = pd.DataFrame(data)
print(df)

# Basic DataFrame operations
print(f"\nFirst 2 rows:\n{df.head(2)}")
print(f"\nLast 2 rows:\n{df.tail(2)}")
print(f"\nInfo:\n{df.info()}")
print(f"\nDescribe:\n{df.describe()}")

# Selecting columns
print(df['name'])
print(df[['name', 'age']])

# Selecting rows
print(df.loc[0])        # By label
print(df.iloc[0])       # By position
print(df.loc[0:2])      # Multiple rows

# Filtering
high_salary = df[df['salary'] > 55000]
print(f"\nHigh salary employees:\n{high_salary}")

# Multiple conditions
young_high_salary = df[(df['age'] < 30) & (df['salary'] > 50000)]
print(f"\nYoung with high salary:\n{young_high_salary}")

# Adding columns
df['bonus'] = df['salary'] * 0.1
print(df)

# Modifying values
df.loc[0, 'age'] = 26
df['salary'] = df['salary'] * 1.05  # 5% raise

# Deleting columns
df_copy = df.copy()
df_copy.drop('bonus', axis=1, inplace=True)

# Sorting
sorted_by_age = df.sort_values('age')
sorted_desc = df.sort_values('salary', ascending=False)

# Grouping
dept_data = {
    'name': ['Peter', 'Sarah', 'Mike', 'Lisa', 'Tom'],
    'department': ['IT', 'HR', 'IT', 'HR', 'IT'],
    'salary': [50000, 60000, 75000, 55000, 65000]
}
df_dept = pd.DataFrame(dept_data)

# Group by department
by_dept = df_dept.groupby('department').agg({
    'salary': ['mean', 'sum', 'count']
})
print(f"\nSalary by department:\n{by_dept}")

# Reading/Writing files
# df.to_csv('data.csv', index=False)
# df = pd.read_csv('data.csv')

# df.to_excel('data.xlsx', index=False)
# df = pd.read_excel('data.xlsx')

# Handling missing data
data_with_nan = {
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, 7, 8],
    'C': [9, 10, 11, 12]
}
df_nan = pd.DataFrame(data_with_nan)

# Check for missing values
print(df_nan.isnull().sum())

# Drop rows with missing values
df_dropped = df_nan.dropna()

# Fill missing values
df_filled = df_nan.fillna(0)
df_mean_filled = df_nan.fillna(df_nan.mean())

# Merging DataFrames
df1 = pd.DataFrame({'id': [1, 2, 3], 'value': [10, 20, 30]})
df2 = pd.DataFrame({'id': [1, 2, 4], 'score': [100, 200, 400]})

# Inner join
merged = pd.merge(df1, df2, on='id', how='inner')
print(f"\nMerged:\n{merged}")

# Concatenating
df_concat = pd.concat([df1, df2], axis=0, ignore_index=True)


# PRACTICAL DATA ANALYSIS EXAMPLES

# Example 1: Sales analysis
sales_data = {
    'date': pd.date_range('2024-01-01', periods=10),
    'product': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B', 'A', 'C'],
    'quantity': [5, 3, 7, 2, 6, 4, 3, 5, 6, 4],
    'price': [10, 15, 10, 20, 15, 10, 20, 15, 10, 20]
}
df_sales = pd.DataFrame(sales_data)
df_sales['total'] = df_sales['quantity'] * df_sales['price']

# Total sales by product
sales_by_product = df_sales.groupby('product')['total'].sum()
print(f"\nSales by product:\n{sales_by_product}")

# Daily total sales
df_sales['date_only'] = df_sales['date'].dt.date
daily_sales = df_sales.groupby('date_only')['total'].sum()

# Example 2: Customer data analysis
customer_data = {
    'customer_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'age': [25, 35, 45, 30, 50, 28, 40, 33, 55, 29],
    'purchases': [5, 12, 8, 15, 3, 20, 7, 18, 4, 22],
    'total_spent': [500, 1200, 800, 1500, 300, 2000, 700, 1800, 400, 2200]
}
df_customers = pd.DataFrame(customer_data)

# Age groups
df_customers['age_group'] = pd.cut(
    df_customers['age'],
    bins=[0, 30, 40, 50, 100],
    labels=['<30', '30-40', '40-50', '50+']
)

# Average spending by age group
avg_by_age = df_customers.groupby('age_group')['total_spent'].mean()
print(f"\nAverage spending by age:\n{avg_by_age}")

# Find top customers
top_customers = df_customers.nlargest(3, 'total_spent')
print(f"\nTop 3 customers:\n{top_customers}")


# BASIC VISUALIZATION (Optional)
# Uncomment if matplotlib is installed

"""
import matplotlib.pyplot as plt

# Line plot
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.title('Sine Wave')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()

# Bar chart
products = ['Product A', 'Product B', 'Product C']
sales = [100, 150, 120]

plt.bar(products, sales)
plt.title('Sales by Product')
plt.ylabel('Sales')
plt.show()

# Histogram
data = np.random.randn(1000)
plt.hist(data, bins=30)
plt.title('Distribution')
plt.show()

# Scatter plot
x = np.random.rand(50)
y = np.random.rand(50)
plt.scatter(x, y)
plt.title('Scatter Plot')
plt.show()
"""


# TIME SERIES ANALYSIS

dates = pd.date_range('2024-01-01', periods=365)
values = np.random.randn(365).cumsum()
ts = pd.Series(values, index=dates)

# Resampling
monthly = ts.resample('M').mean()  # Monthly average
weekly = ts.resample('W').sum()    # Weekly sum

# Rolling window
rolling_mean = ts.rolling(window=7).mean()  # 7-day moving average


# PIVOT TABLES

data = {
    'date': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02'],
    'product': ['A', 'B', 'A', 'B'],
    'sales': [100, 150, 120, 180]
}
df = pd.DataFrame(data)

pivot = df.pivot_table(
    values='sales',
    index='date',
    columns='product',
    aggfunc='sum'
)
print(f"\nPivot table:\n{pivot}")


# STRING OPERATIONS IN PANDAS

df_text = pd.DataFrame({
    'name': ['Peter Sawm', 'JANE SMITH', 'Bob Wilson'],
    'email': ['peter@email.com', 'jane@email.com', 'bob@email.com']
})

# String methods
df_text['name_upper'] = df_text['name'].str.upper()
df_text['name_title'] = df_text['name'].str.title()
df_text['first_name'] = df_text['name'].str.split().str[0]

# Check if contains
df_text['has_doe'] = df_text['name'].str.contains('doe')


# PERFORMANCE TIPS

"""
1. Use vectorized operations (avoid loops)
   - df['col'] * 2  (fast)
   - for i in df: df.loc[i, 'col'] * 2  (slow)

2. Use appropriate data types
   - df['col'].astype('int32')  (saves memory)

3. Read only needed columns
   - pd.read_csv('file.csv', usecols=['col1', 'col2'])

4. Use chunks for large files
   - for chunk in pd.read_csv('large.csv', chunksize=1000):
       process(chunk)

5. Use category dtype for repeated strings
   - df['category'] = df['category'].astype('category')
"""


# COMMON DATA ANALYSIS WORKFLOW

"""
1. Load data
   - df = pd.read_csv('data.csv')

2. Explore data
   - df.head()
   - df.info()
   - df.describe()

3. Clean data
   - Handle missing values
   - Remove duplicates
   - Fix data types

4. Transform data
   - Create new columns
   - Group and aggregate
   - Merge datasets

5. Analyze
   - Calculate statistics
   - Find patterns
   - Generate insights

6. Visualize
   - Create plots
   - Make dashboards

7. Export results
   - df.to_csv('results.csv')
"""