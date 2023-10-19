# Pandas Exercises 



## Create a histogram of the 'a' column

````python
df3 = pd.read_csv('df3')

df3['a'].plot.hist(color = 'red', bins = 30)
plt.xlim([0,1])
plt.ylim([0,70])
````


![exercise2](exercise2.png)


