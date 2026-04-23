import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')

print(data.head())

sns.histplot(data['Glucose'], kde=True)

plt.title('Histogram of Glucose')
plt.xlabel('Glucose')
plt.ylabel('Count')
plt.show()

sns.boxplot(x=data['BMI'])

plt.title('Boxplot of BMI')
plt.show()