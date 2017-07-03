
#by johnny minor on 9.20.15

import matplotlib.pyplot as plot 
from pylab import * 
import math
import numpy as np 

#not sure what these do but apparently they have to be here 
#in order to show the linear regression equation. 
fig = plt.figure()
ax = fig.add_subplot(111)

#newtons gravitational constant 
G = 6.67e-11

#arange is (start, stop, step) 
x = arange(0.0, 10.0, 0.1)

#Names of Jupiters Galilean Moons 
names = ['Io', 'Europa', 'Ganymede', 'Callisto'] 

#period in Earth days. 
period = [1.769, 3.551, 7.1546, 16.849] 

#a = semi-major axis or mean orbital distance. in kilometers 
a = [421000.0, 671100.0, 1070000.0, 1882700.0 ]

log_a = log10(a)

log_period = log10(period) 

#print names 

plot(log_a, log_period, 'ro')
plt.xlabel('log(a)')
plt.ylabel('log(period)')
plt.title('Semi-major Axis vs Period of Jupiters Galilean Moons')
plt.text(60, 0.25,'$y = 3/2 x + stuff$')
#plt.axis([40, 160, 0, 0.03])
plt.grid(True)

#this will keep the plot and not clear the graph. You could also just put show() at the bottom and be equivalent.  
hold(True) 

#this is the linear regression line. 
#ax.text(0.1, 0.9,'$y = \mfrac{3}{2} * x - 8.21$', ha='center', va='center', transform=transAxes)


ax.text(2, 3, r'Linear Regression: $y = \frac{3}{2} x - 8.21$', fontsize=15)
plot(x, 1.5 * x + -8.21)


plt.show()


#how to calculate the linear regression equation. 
#first # is slope and second is y intercept 
linear_regression = np.polyfit(log_a, log_period, 1) 

print linear_regression
