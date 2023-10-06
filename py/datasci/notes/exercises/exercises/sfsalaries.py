import pandas as pd


sal = pd.read_csv('Salaries.csv')

def findchief (x):
    if 'chief' in x.lower().split():
        return True
    else:
        return False


# JobTitle
# TotalPayBenefits

sal['title_len'] = sal['JobTitle'].apply(len)






print(
        sal[['title_len', 'TotalPayBenefits']].corr()
        )
