import pandas as pd

data = [10, 20, 30, 40, 50]
series = pd.Series(data)
print(series)

data = {
    "Name": ["Ali", "Sara", "John"],
    "Age": [21, 22, 23],
    "City": ["Delhi", "Mumbai", "Bangalore"]
}
df = pd.DataFrame(data)
print(df)