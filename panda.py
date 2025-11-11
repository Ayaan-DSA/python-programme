import pandas as pd
import numpy as np

data = {
    'Product_ID': [101, 102, 103, 104],
    'Product_Name': ['Laptop', 'Smartphone', 'Tablet', 'Monitor'],
    'Catergory': ['Electronics', 'Electronics', 'Electronics', 'Electronics'],
    'Price': [1200, 800, 300, 400],
    'Quantity': [1, 2, 3, 1],
    'Discount' : [ 10, 5 , 5 , 20]
}
# --- create dataframe----
df = pd.DataFrame(data)
df['Revenue'] = df['Price'] * df['Quantity'] *(1- df['Discount']/100)
print(df.info)
# ---- convert into CSV and use of describe method----
df.to_csv("sales_data.csv", index=False)

sales = pd.read_csv("sales_data.csv")
sales.head()
# print(sales.describe(include='all'))

