import pandas as pd

data = pd.read_csv("data.csv")

print("Dataset:\n", data)

print("\nMissing Values in each column:")
print(data.isnull().sum())

print("\nTotal Missing Values:", data.isnull().sum().sum())