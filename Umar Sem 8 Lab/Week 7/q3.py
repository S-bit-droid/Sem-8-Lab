import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A':[10,20,30,40,50],
    'B':[5,10,15,20,25],
    'C':[2,4,6,8,10],
    'D':[1,3,5,7,9]
})
print (df)
print(df.iloc[:,1].mean())
print(df.iloc[:5,2:4].mean())
print(df.sum(axis=1))
print(df.mean(axis=1).max())
