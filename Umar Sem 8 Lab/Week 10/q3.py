import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')

print(data.head())

sns.scatterplot(x='Glucose', y='BMI', hue='Class', data=data)

plt.title('Glucose vs BMI')
plt.show()

sns.scatterplot(x='Age', y='Diabetes_Pedigree', hue='Class', data=data)

plt.title('Age vs Diabetes Pedigree')
plt.show()

corr = data.corr()

sns.heatmap(corr, annot=True, cmap='coolwarm')

plt.title('Correlation Heatmap')
plt.show()