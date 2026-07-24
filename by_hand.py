import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#doing it by hand, without the assistence of libraries to calculate prediction

#loading dataset
df = pd.read_csv('Salary.csv')

x = df['YearsExperience']
y = df['Salary']

#calculating mean average of x and y
mean_x = sum(x)/len(x)
mean_y = sum(y)/len(y)

# print(f'{mean_x} | {mean_y}')

#calculating prediction's slope and constant
numerator   = 0
denominator = 0
for x_i, y_i in zip(x, y):
    numerator   += (x_i - mean_x) * (y_i - mean_y)
    denominator += (x_i - mean_x) ** 2
    
a = numerator/denominator
b = mean_y - (a * mean_x)

def prediction(x):
    return (a*x) + b

df['PredictedSalary'] = prediction(df['YearsExperience'])

#mounjting graph
sns.scatterplot(data=df, x=x, y=y, label='data_points')
sns.lineplot(data=df, x=x, y='PredictedSalary', label='prediction', color='red')
plt.show()