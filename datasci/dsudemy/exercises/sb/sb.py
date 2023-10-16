import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np


sns.set_style('whitegrid')
titanic = sns.load_dataset('titanic')
# print(titanic.head())

# fig = sns.jointplot(x='fare',y='age',data = titanic, kind = 'hist')
# fig = sns.displot(titanic['fare'], kde = False, bins = 30)
# fig = sns.boxplot(x = 'class' , y = 'age', data = titanic, )
# fig = sns.countplot(x = 'sex', data = titanic)

# fig = sns.FacetGrid(data = titanic, col =  'sex')
# fig = fig.map(plt.hist, 'age')
print(
    sns.heatmap(titanic.corr())
        )

# plt.xlim([0,600])
# plt.ylim([0,500])


# fig.savefig('exercise7.png')
plt.show()



