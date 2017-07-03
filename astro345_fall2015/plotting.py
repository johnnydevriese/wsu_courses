import matplotlib.pyplot as plt 

plt.plot([0,1,1, 0.1666], [0,1, -1, 0], 'ro')
plt.axis([-3, 3, -3, 3])
plt.show()

savefig('foo.png')
