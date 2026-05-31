#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

np.random.seed(42)

print("=" * 80)
print("Pharmacy Star Schema Analysis")
print("=" * 80)
print()

dim_time = pd.read_csv('Data/dim_time.csv')
dim_customer = pd.read_csv('Data/dim_customer.csv')
dim_drug = pd.read_csv('Data/dim_drug.csv')
dim_branch = pd.read_csv('Data/dim_branch.csv')

print("✓ DIM_TIME:", len(dim_time), "records")
print("✓ DIM_CUSTOMER:", len(dim_customer), "records")
print("✓ DIM_DRUG:", len(dim_drug), "records")
print("✓ DIM_BRANCH:", len(dim_branch), "records")
print()

drug_prices = {
    'D0001': 45000, 'D0002': 85000, 'D0004': 120000, 'D0005': 250000,
    'D0006': 75000, 'D0007': 95000, 'D0008': 150000, 'D0009': 110000,
    'D0010': 180000, 'D0011': 165000, 'D0012': 125000, 'D0013': 220000,
    'D0014': 195000, 'D0015': 95000, 'D0016': 140000, 'D0017': 175000,
    'D0018': 55000, 'D0019': 75000, 'D0020': 185000,
}

transactions = []
n_transactions = 5000

for i in range(n_transactions):
    time_row = dim_time.sample(1).iloc[0]
    drug_row = dim_drug.sample(1).iloc[0]
    customer_row = dim_customer.sample(1).iloc[0]
    branch_row = dim_branch.sample(1).iloc[0]
    
    quantity = np.random.randint(1, 5)
    unit_price = drug_prices.get(drug_row['DrugCode'], 100000)
    total_amount = quantity * unit_price
    payment_method = np.random.choice(['Cash', 'Card', 'Insurance', 'Check'], p=[0.4, 0.35, 0.2, 0.05])
    
    transactions.append({
        'TransactionID': f'TRX{i+1:06d}',
        'DateKey': time_row['Date'],
        'CustomerID': customer_row['CustomerID'],
        'DrugCode': drug_row['DrugCode'],
        'BranchCode': branch_row['BranchCode'],
        'Quantity': quantity,
        'UnitPrice': unit_price,
        'TotalAmount': total_amount,
        'PaymentMethod': payment_method,
        'Month': time_row['Month'],
        'Quarter': time_row['Quarter'],
        'Year': time_row['Year'],
        'DayOfWeek': time_row['DayOfWeek'],
        'Gender': customer_row['Gender'],
        'AgeGroup': customer_row['AgeGroup'],
        'DrugCategory': drug_row['Category'],
        'BranchName': branch_row['BranchName']
    })

fact_sales = pd.DataFrame(transactions)

print("FACT TABLE CREATED")
print("=" * 80)
print(f"Total Transactions: {len(fact_sales)}")
print(f"Total Revenue: {fact_sales['TotalAmount'].sum():,.0f} Rials")
print(f"Average Transaction: {fact_sales['TotalAmount'].mean():,.0f} Rials")
print()

print("MONTHLY REVENUE ANALYSIS")
print("=" * 80)
pivot_monthly = fact_sales.groupby('Month').agg({
    'TotalAmount': ['sum', 'count', 'mean'],
    'Quantity': 'sum'
}).round(0)
pivot_monthly.columns = ['Revenue', 'Count', 'AvgAmount', 'TotalQty']
print(pivot_monthly)
print()

print("BRANCH vs DRUG CATEGORY")
print("=" * 80)
pivot_branch_drug = fact_sales.pivot_table(
    values='TotalAmount',
    index='BranchName',
    columns='DrugCategory',
    aggfunc='sum',
    fill_value=0
).round(0)
print(pivot_branch_drug)
print()

print("AGE GROUP vs GENDER")
print("=" * 80)
pivot_age_gender = fact_sales.pivot_table(
    values='TotalAmount',
    index='AgeGroup',
    columns='Gender',
    aggfunc='sum',
    fill_value=0
).round(0)
print(pivot_age_gender)
print()

print("PAYMENT METHOD by BRANCH")
print("=" * 80)
pivot_payment = fact_sales.pivot_table(
    values='TransactionID',
    index='BranchName',
    columns='PaymentMethod',
    aggfunc='count',
    fill_value=0
).astype(int)
print(pivot_payment)
print()

print("DAY OF WEEK ANALYSIS")
print("=" * 80)
pivot_dayofweek = fact_sales.groupby('DayOfWeek').agg({
    'TotalAmount': ['sum', 'count', 'mean'],
    'Quantity': 'sum'
}).round(0)
pivot_dayofweek.columns = ['Revenue', 'Count', 'AvgAmount', 'TotalQty']
print(pivot_dayofweek)
print()

print("TOP 10 DRUGS")
print("=" * 80)
pivot_top_drugs = fact_sales.groupby(['DrugCode', 'DrugCategory']).agg({
    'TotalAmount': 'sum',
    'Quantity': 'sum',
    'TransactionID': 'count'
}).round(0)
pivot_top_drugs.columns = ['Revenue', 'Units', 'Count']
pivot_top_drugs = pivot_top_drugs.sort_values('Revenue', ascending=False).head(10)
print(pivot_top_drugs)
print()

print("AGE GROUP DISTRIBUTION")
print("=" * 80)
pivot_age = fact_sales.groupby('AgeGroup').agg({
    'TotalAmount': ['sum', 'count', 'mean'],
    'Quantity': 'sum'
}).round(0)
pivot_age.columns = ['Revenue', 'Count', 'AvgAmount', 'TotalQty']
print(pivot_age)
print()

print("PAYMENT METHOD ANALYSIS")
print("=" * 80)
payment_analysis = fact_sales.groupby('PaymentMethod').agg({
    'TotalAmount': ['sum', 'count', 'mean'],
    'Quantity': 'sum'
}).round(0)
payment_analysis.columns = ['Revenue', 'Count', 'AvgAmount', 'TotalQty']
print(payment_analysis)
print()

print("BRANCH PERFORMANCE")
print("=" * 80)
branch_analysis = fact_sales.groupby('BranchName').agg({
    'TotalAmount': ['sum', 'count', 'mean'],
    'Quantity': 'sum'
}).round(0)
branch_analysis.columns = ['Revenue', 'Count', 'AvgAmount', 'TotalQty']
branch_analysis = branch_analysis.sort_values('Revenue', ascending=False)
print(branch_analysis)
print()

print("DRUG CATEGORY ANALYSIS")
print("=" * 80)
category_analysis = fact_sales.groupby('DrugCategory').agg({
    'TotalAmount': ['sum', 'count', 'mean'],
    'Quantity': 'sum'
}).round(0)
category_analysis.columns = ['Revenue', 'Count', 'AvgAmount', 'TotalQty']
category_analysis = category_analysis.sort_values('Revenue', ascending=False)
print(category_analysis)
print()

fact_sales.to_csv('fact_sales_output.csv', index=False, encoding='utf-8')
print("✓ Saved: fact_sales_output.csv")

with pd.ExcelWriter('pharmacy_pivots_analysis.xlsx', engine='openpyxl') as writer:
    pivot_monthly.to_excel(writer, sheet_name='Monthly Revenue')
    pivot_branch_drug.to_excel(writer, sheet_name='Branch vs Category')
    pivot_age_gender.to_excel(writer, sheet_name='Age vs Gender')
    pivot_payment.to_excel(writer, sheet_name='Payment vs Branch')
    pivot_dayofweek.to_excel(writer, sheet_name='Day of Week')
    pivot_top_drugs.to_excel(writer, sheet_name='Top 10 Drugs')
    pivot_age.to_excel(writer, sheet_name='Age Distribution')
    payment_analysis.to_excel(writer, sheet_name='Payment Analysis')
    branch_analysis.to_excel(writer, sheet_name='Branch Analysis')
    category_analysis.to_excel(writer, sheet_name='Category Analysis')

print("✓ Saved: pharmacy_pivots_analysis.xlsx")
print()

print("=" * 80)
print("ANALYSIS COMPLETE")
print("=" * 80)
