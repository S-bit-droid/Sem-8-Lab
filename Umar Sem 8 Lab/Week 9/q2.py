import pandas as pd
import numpy as np

df = pd.read_csv("data.csv")

num_df = df.select_dtypes(include=[np.number])

corr_matrix = num_df.corr()

print("Correlation Matrix:")
print(corr_matrix)

threshold = 0.9

high_corr_cols = set()
for i in range(len(corr_matrix.columns)):
    for j in range(i):
        if abs(corr_matrix.iloc[i, j]) > threshold:
            colname = corr_matrix.columns[i]
            high_corr_cols.add(colname)

print("\nHighly Correlated Columns to Remove:")
print(high_corr_cols)

df_cleaned = df.drop(columns=high_corr_cols)

print("\nDataset shape after removing correlated columns:")
print(df_cleaned.shape)