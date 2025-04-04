# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 12:48:32 2025

@author: Ghost
"""

import pandas as pd

# Load the dataset
file_path = "D:/Projects/Datasets/archive (18)/DataCoSupplyChainDataset.csv"
df = pd.read_csv(file_path, encoding="ISO-8859-1")

# View first few    rows
df.head()
df.shape  # returns (rows, columns)
df.columns  # shows all column names
df.info()  # summary of column types and null values

df = df.rename(columns={
    'order date (DateOrders)': 'Order Date',
    'shipping date (DateOrders)': 'Shipping Date',
    'Order Item Quantity': 'Quantity',
    'Order Item Product Price': 'Unit Price',
    'Order Item Total': 'Total Price',
    'Order Profit Per Order': 'Profit',
    'Days for shipping (real)': 'Actual Shipping Days',
    'Days for shipment (scheduled)': 'Scheduled Shipping Days'
})
columns_to_drop = ['Customer Email', 'Customer Password', 'Product Description', 'Product Image']
df.drop(columns=columns_to_drop, inplace=True)

df.isnull().sum()  # check how many missing values in each column

# Drop rows with missing important info
df = df.dropna(subset=["Customer Lname", "Customer Zipcode"])

df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Shipping Date"] = pd.to_datetime(df["Shipping Date"])

df["Shipping Delay (Days)"] = (df["Shipping Date"] - df["Order Date"]).dt.days

df.to_csv("D:/Projects/Datasets/archive (18)/cleaned_supply_chain_data.csv", index=False)


