import pandas as pd

# Load personal expenses CSV
df = pd.read_csv("expenses.csv")

# View data
print(df.head())

# Total and average expenses
print("Total Expenses:", df["Amount"].sum())
print("Average Expense:", df["Amount"].mean())

# Group by category
category_expense = df.groupby("Category")["Amount"].sum()
print(category_expense)
