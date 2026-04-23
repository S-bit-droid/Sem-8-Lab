import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('data.csv')
df.fillna(df.mean(), inplace=True)
print(df)

print(df.head())

X = df.drop('Class', axis=1) 
y = df['Class']            

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training features shape:", X_train.shape)
print("Testing features shape:", X_test.shape)
print("Training labels shape:", y_train.shape)
print("Testing labels shape:", y_test.shape)