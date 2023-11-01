import pandas as pd
import matplotlib.pyplot as plt

df3 = pd.read_csv('df3')
# print(
#         )
plt.style.use('ggplot')

# Exercise 1 =======

df3.plot(kind = 'scatter', x = 'a', y = 'b', figsize = (12,3), color = 'red')
plt.xlim([-0.2, 1.2])
plt.ylim([-0.2, 1.2])
plt.savefig('exercise1.png')

#===================

# Exercise 2 =============

# df3.plot.hist(x = 'a', y = 'b', figsize = (12,3), color = 'red')

# plt.savefig('exercise2.png')
# ====================

# Exercise 3 =========

# df3.plot.scatter(x = 'a', y = 'b', figsize = (12,3))
# plt.xlim([-0.2, 1.2])
# plt.ylim([-0.2, 1.2])
# plt.savefig('exercise3.png')




# Exercise 4 ====

# df3[ ['a', 'b'] ].plot(kind = 'box')


# Exercise 5 ====

# df3['d'].plot(kind = 'kde')
# plt.savefig('exercise4.png')

# df3['d'].plot(kind = 'kde', linestyle = '--', linewidth = 5.0, color = 'red')



#Exercise 5======#

# df3.head(30).plot.area(alpha = 0.3)
# plt.legend(bbox_to_anchor=(1.0, 0.75))
# plt.xlim([0,30])
# plt.ylim([0,3])

# =============#






plt.show()
