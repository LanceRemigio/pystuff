import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,100)


y = x * 2
z = x ** 2 



fig  = plt.figure()

ax1 = fig.add_subplot(1,1,1)
ax1.plot(x,z)
ax1.set_xlabel('x')
ax1.set_ylabel('z')
ax1.set_title('Bigger Plot')


ax2 = fig.add_axes([0.2, 0.5, 0.2, 0.2 ])

ax2.plot(x,y)
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('zoom')



plt.show()

fig.savefig('exer3.png')



# Exercise 1

# fig = plt.figure()
# fig.add_axes([0,0,1,1])

# plt.plot(x,y)



## Exercise 2


# fig = plt.figure()

# ax1 = fig.add_axes([0,0,1,1])
# ax2 = fig.add_axes([0.2, 0.5, 0.2, 0.2 ])

# ax1.plot(x,y)
# ax2.plot(x,y)
# ax2.set_xlabel('x')
# ax2.set_ylabel('y')
# plt.show()



######




## Exercise 3


# fig  = plt.figure()
# axes1 = fig.add_axes([0,0,1,1])
# # plt.subplots_adjust(left=0.2,bottom=0.2, top = 0.9, right = 0.9)
# # fig.add_subplot()
# # axes.plot(x,z)

# # axes.set_xlim([0,100])
# # axes.set_ylim([2000,10000])


# axes1.plot(x,z) # larger plot
# axes1.set_xlabel("x")
# axes1.set_ylabel("y")
# axes1.set_xlim([0,100])
# axes1.set_ylim([2000,10000])


# axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.4])

# axes2.plot(x,y) # smaller plot
# axes2.set_xlabel("x")
# axes2.set_ylabel("y")
# axes2.set_title("zoom")
# axes2.set_ylim([30, 50])
# axes2.set_xlim([20,22])

# plt.show()

# fig.savefig("exer3.png")


################################

# Exercise 4
# fig, axes = plt.subplots(1,2, figsize = (12,5)) # nrows = 1, ncols = 2

# axes[0].plot(x,y, color = "blue", linewidth = 5.00, ls = '--')

# axes[1].plot(x,z, color = "red", linewidth = 5.00)



# plt.show()

# fig.savefig("exer4.png")


