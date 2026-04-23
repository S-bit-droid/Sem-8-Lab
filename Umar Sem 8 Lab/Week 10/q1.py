import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")

data[['Pregnant','Glucose','Diastolic_BP','Skin_Fold','Serum_Insulin','BMI','Diabetes_Pedigree','Age']].plot(figsize=(10,5), marker='o')
plt.title('Line Plot of Numeric Features')
plt.show()

data[['Pregnant','Glucose','Diastolic_BP','Skin_Fold','Serum_Insulin','BMI','Diabetes_Pedigree','Age']].mean().plot(kind='bar', figsize=(10,5), color='skyblue')
plt.title('Average Value of Each Feature')
plt.show()