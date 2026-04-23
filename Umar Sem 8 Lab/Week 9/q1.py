import pandas as pd

df = pd.read_csv("data.csv")

print("Data Preview:")
print(df.head())

summary_stats = df.describe()

print("\nSummary Statistics of Numerical Columns:")
print(summary_stats)