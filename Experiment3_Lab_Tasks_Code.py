"""
Experiment 3 — Lab Tasks: NumPy & Pandas
==========================================
"""

import numpy as np
import pandas as pd


# ==========================================================
# Task 1: Create a NumPy array of 10 numbers and compute its
#         sum, mean, max and standard deviation.
# ==========================================================
arr = np.array([12, 45, 7, 23, 56, 89, 34, 18, 90, 3])

print("Array:", arr)
print("Sum:", arr.sum())
print("Mean:", arr.mean())
print("Max:", arr.max())
print("Standard Deviation:", arr.std())

print("\n" + "="*50 + "\n")


# ==========================================================
# Task 2: Load any CSV file with Pandas and print its shape,
#         column names and first five rows.
# ==========================================================
df = pd.read_csv("data.csv")   # <-- replace with your actual CSV file path

print("Shape (rows, columns):", df.shape)
print("Column Names:", list(df.columns))
print("First 5 Rows:\n", df.head())

print("\n" + "="*50 + "\n")


# ==========================================================
# Task 3: Filter the dataset to show only rows meeting a
#         condition of your choice.
# ==========================================================
# Example: show only rows where the "Salary" column is greater than 50000
# (change "Salary" and the value to match a real column in your CSV)
filtered_df = df[df["Salary"] > 50000]
print("Filtered rows (Salary > 50000):\n", filtered_df)

print("\n" + "="*50 + "\n")


# ==========================================================
# Task 4: Replace all missing values in a numeric column with
#         the column mean.
# ==========================================================
# Example: fill missing values in the "Bonus" column with its mean
print("Missing values before:", df["Bonus"].isnull().sum())
df["Bonus"] = df["Bonus"].fillna(df["Bonus"].mean())
print("Missing values after:", df["Bonus"].isnull().sum())

print("\n" + "="*50 + "\n")


# ==========================================================
# Task 5: Group the data by a categorical column and report
#         the mean of a numeric column.
# ==========================================================
# Example: average Salary per City
grouped = df.groupby("City")["Salary"].mean()
print("Average Salary by City:\n", grouped)
