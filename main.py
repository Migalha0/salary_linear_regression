import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

import matplotlib.pyplot as plt
import seaborn as sns

#loading dataset
df = pd.read_csv('Salary.csv')

#choosing axes
x = df[['YearsExperience']]
y = df['Salary']

#separating data into training and test sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#choosing model and training
model = LinearRegression()
model.fit(x_train,y_train)

#add model prediction to dataset
df['PredictedSalary'] = model.predict(x)

#mounting graph
sns.scatterplot(data=df, x='YearsExperience', y='Salary', label="data_points")
sns.lineplot(data=df, x='YearsExperience', y='PredictedSalary', label="prediction",color='red')

plt.savefig('salary_prediction_plot.png')
print('plot saved to salary_prediction_plot.png')