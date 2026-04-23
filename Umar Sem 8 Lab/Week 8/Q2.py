import pandas as pd

print("="*10+"data handling using mean"+"="*10)
data1 = pd.read_csv("data.csv")
data1.fillna(data1.mean(), inplace=True)
print(data1)

print("="*10+"data handling using median"+"="*10)
data2 = pd.read_csv("data.csv")
data2.fillna(data2.median(), inplace=True)
print(data2)

print("="*10+"data mode using mean"+"="*10)
data3 = pd.read_csv("data.csv")
data3.fillna(data3.mode().iloc[0], inplace=True)
print(data3)

# data = pd.read_csv("data.csv")
# data = data.dropna()
# data = data.dropna(axis=1)