from numpy import average, who
import pandas as pd


sal = pd.read_csv('Salaries.csv')

# print(sal.head())

# print(sal.info())

# avg_pay = sal['BasePay'].mean()
# max_pay = sal['OvertimePay'].max()
# print(max_pay)


print(
        sal['JobTitle'].value_counts()
        )
