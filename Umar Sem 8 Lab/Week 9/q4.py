import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data.csv")

print("First 5 rows of dataset:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nSummary Statistics:")
print(df.describe())

corr = df.corr(numeric_only=True)
print("\nCorrelation Matrix:")
print(corr)

plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

num_cols = df.select_dtypes(include=['int64','float64']).columns
for col in num_cols:
    plt.figure()
    sns.boxplot(x=df[col])
    plt.title(f"Boxplot of {col}")
    plt.show()

df.hist(figsize=(10,8))
plt.show()

cat_cols = df.select_dtypes(include=['object']).columns
for col in cat_cols:
    print(f"\nValue counts for {col}:")
    print(df[col].value_counts())

df.to_csv("eda_processed_dataset.csv", index=False)