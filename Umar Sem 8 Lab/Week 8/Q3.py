import pandas as pd

data = pd.read_csv("data.csv")

data.rename(columns={
    'Glucose':' Glucose_Level',
    'Age':'Patient_Age'
}, inplace=True)

print(data)

data['Student_Age'] = data['Student_Age'].astype(int)
data['Student_Marks'] = data['Student_Marks'].astype(float)

print(data.dtypes)