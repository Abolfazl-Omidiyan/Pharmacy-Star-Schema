```markdown
# 📊 Project 2: Star Schema Model for a Chain Pharmacy

## Project Introduction

This project focuses on the design and implementation of a **multidimensional data model (Star Schema)** for a **chain pharmacy**.

### Objectives
- ✓ Design a Star Schema model for pharmacy sales
- ✓ Create dimension tables
- ✓ Create a fact table
- ✓ Create Pivot Tables for analysis
- ✓ Produce comprehensive reports

---

## 📁 Project Structure

```
Pharmacy_Project/
│
├── Data/                           # Data tables
│   ├── dim_time.csv               # Time dimension table (366 records)
│   ├── dim_customer.csv           # Customer dimension table (4,347 records)
│   ├── dim_drug.csv               # Drug dimension table (20 records)
│   ├── dim_branch.csv             # Branch dimension table (10 records)
│   └── fact_sales.csv             # Sales fact table (5,000 records)
│
├── Analysis/                       # Dynamic analyses
│   └── pharmacy_analysis_pivots.xlsx  # 7 Pivot Tables
│
└── Reports/                        # Reports
    └── Pharmacy_Star_Schema_Report_Farsi.html  # Comprehensive report (Persian)
```

---

## 📊 Star Schema Architecture

```
                    ┌─────────────────────────┐
                    │   FACT_SALES            │
                    │  ─────────────────────  │
                    │  • TransactionID        │
                    │  • DateKey (FK)         │
                    │  • CustomerID (FK)      │
                    │  • DrugCode (FK)        │
                    │  • BranchCode (FK)      │
                    │  • Quantity             │
                    │  • UnitPrice            │
                    │  • TotalAmount          │
                    │  • PaymentMethod        │
                    └─────────────────────────┘
                            ↓↓↓↓
        ┌───────────────────┼───────────────────┐
        │                   │                   │
    DIM_TIME          DIM_CUSTOMER        DIM_DRUG
   ────────────      ──────────────      ─────────
   • Date (PK)       • CustomerID (PK)   • DrugCode (PK)
   • Day             • Gender            • DrugName
   • Month           • AgeGroup          • Category
   • Quarter                             
   • Year                DIM_BRANCH
   • DayOfWeek      ──────────────────
   • WeekOfYear     • BranchCode (PK)
                    • BranchName
```

---

## 📋 Table Descriptions

### 1. Time Dimension (DIM_TIME)
- **Records:** 366 (all days of the year 2024)
- **Columns:** Date, Day, Month, Quarter, Year, DayOfWeek, WeekOfYear
- **Usage:** Sales analysis by time

### 2. Customer Dimension (DIM_CUSTOMER)
- **Records:** 4,347
- **Columns:** CustomerID, Gender, AgeGroup
- **Age groups:** <18, 18-35, 36-50, 51-65, >65
- **Usage:** Customer segmentation

### 3. Drug Dimension (DIM_DRUG)
- **Records:** 20
- **Columns:** DrugCode, DrugName, Category
- **Drug categories:** 13 different categories
- **Usage:** Sales analysis by drug

### 4. Branch Dimension (DIM_BRANCH)
- **Records:** 10
- **Columns:** BranchCode, BranchName
- **Usage:** Revenue distribution across branches

### 5. Fact Table (FACT_SALES) ⭐
- **Records:** 5,000 transactions
- **Key measures:**
  - Quantity: number of units
  - UnitPrice: price per unit
  - TotalAmount: total amount
  - PaymentMethod: payment method

---

## 📈 Overall Statistics

| Metric | Value |
|--------|-------|
| Total Transactions | 5,000 |
| Total Revenue | 1,674 billion Tomans |
| Average Transaction | 334,820 Tomans |
| Total Units Sold | 11,970 |
| Time Period | Full year 2024 |

---

## 🔄 Pivot Tables

### 7 Pivot Tables Created:

1. **Monthly Revenue Trend** - Revenue by month
2. **Branch vs. Drug Category** - Sales per branch by category
3. **Age Group vs. Gender** - Sales by age and gender
4. **Payment Method by Branch** - Breakdown of payment methods
5. **Day of Week Analysis** - Revenue by day of week
6. **Top 10 Drugs** - Best-selling drugs
7. **Customer Age Distribution** - Revenue by age group

---

## 💡 Key Findings

### 📊 Revenue Distribution by Payment Method
- **Cash:** 40% (647 billion)
- **Card:** 35% (593 billion)
- **Insurance:** 20% (349 billion)
- **Check:** 5% (83 billion)

### 🏆 Top Branches
1. Branch 5: 186 billion (26%)
2. Branch 9: 173 billion (10.3%)
3. Branch 2: 172 billion (10.3%)

### 💊 Top Drugs
1. D0005 (Antibiotic): 182 billion
2. D0013 (Anticonvulsant): 129 billion
3. D0010 (Statin): 126 billion

### 👥 Age Distribution
- 36-50 years: 344 billion (20.5%)
- 51-65 years: 339 billion (20.2%)
- >65 years: 333 billion (19.9%)
- 18-35 years: 329 billion (19.7%)
- <18 years: 327 billion (19.5%)

---

## 🎯 Business Recommendations

### 1. Branch Management
- ✓ Investigate performance of Branch 10 (lowest revenue)
- ✓ Share best practices from Branch 5 with other branches

### 2. Inventory Management
- ✓ Ensure sufficient stock for Top 10 drugs
- ✓ Implement a forecasting management system for best-selling drugs

### 3. Marketing
- ✓ Targeted campaign for the 36-50 age group
- ✓ Encourage more purchases on low-sales days

### 4. Payment System
- ✓ Promote card and digital payments
- ✓ Reduce the percentage of cash payments

---

## 📂 Project Files

### Data Files
| File | Records | Description |
|------|---------|-------------|
| dim_time.csv | 366 | All days of 2024 |
| dim_customer.csv | 4,347 | Customer information |
| dim_drug.csv | 20 | Drug catalog |
| dim_branch.csv | 10 | Branch information |
| fact_sales.csv | 5,000 | Sales transactions |

### Analysis Files
- `pharmacy_analysis_pivots.xlsx` - 7 Pivot Tables in Excel

### Report Files
- `Pharmacy_Star_Schema_Report_Farsi.html` - Comprehensive report (Persian)

---

## 🛠️ How to Use

### 1. Read CSV Files
```python
import pandas as pd

# Read dimension tables
dim_time = pd.read_csv('Data/dim_time.csv')
dim_drug = pd.read_csv('Data/dim_drug.csv')
dim_customer = pd.read_csv('Data/dim_customer.csv')
dim_branch = pd.read_csv('Data/dim_branch.csv')

# Read fact table
fact_sales = pd.read_csv('Data/fact_sales.csv')
```

### 2. Create Pivot Tables
```python
# Revenue by month
pivot_month = fact_sales.groupby('Month')['TotalAmount'].sum()

# Revenue by branch
pivot_branch = fact_sales.groupby('BranchName')['TotalAmount'].sum()
```

### 3. View the Report
- Open `Pharmacy_Star_Schema_Report_Farsi.html` in your browser

---

## ✅ Data Characteristics

- ✓ Realistic and logical data
- ✓ Complete dates for the year 2024
- ✓ Drug prices appropriate for the Iranian market
- ✓ Diverse customer distribution
- ✓ Various payment methods
- ✓ Relatively equal distribution among branches and age groups

---

## 📚 Additional Resources

### Key Concepts
- **Star Schema:** Data architecture for OLAP
- **Fact Table:** Central table containing transactions
- **Dimension Table:** Descriptive tables
- **Pivot Table:** Dynamic analysis tool

### Useful Tools
- Excel: For Pivot Tables
- Python/Pandas: For data analysis
- Tableau/Power BI: For business dashboards

---

## 📞 Important Notes

1. **All data is for the year 2024**
2. **Prices are in Iranian Tomans**
3. **Pivot Tables are editable in Excel**
4. **The report is in Persian for better understanding**

---

## 🎓 Conclusion

This project demonstrates how the Star Schema model:
- Simplifies complex data
- Provides faster queries
- Enables multidimensional analysis
- Improves managerial decision-making

---

**Creation Date:** 2026 
**Project Type:** Data model design  
**Environment:** Python + Excel + SQL
```
