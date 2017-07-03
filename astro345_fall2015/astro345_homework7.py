#by johnny minor on 10.4.15

import matplotlib.pyplot as plot 
from pylab import * 
import math
import numpy as np 

#*********************problem #2 is right here... *******************

rub_stront = [0.0, 10.0 , 20.0] 

sr_sr_0 = [1.0, 1.0, 1.0] 
sr_sr_10 = [1.0, 1.736, 2.53]
sr_sr_20 = [1.0, 2.472, 4.06 ] 

plot(rub_stront, sr_sr_0, '^')
plot(rub_stront, sr_sr_10, "o")
plot(rub_stront, sr_sr_20, "v")
plt.xlabel('87 Rubidium / 86 Strontium')
plt.ylabel('87 Strontium / 86 Strontium ')
plt.title('Dating Igneous Rocks with Rubidium-Strontium')
#plt.text(60, 0.25,'$y = 3/2 x + stuff$')
plt.axis([-1., 25, 0.0, 5.0])
plt.grid(True)

#arange is (start, stop, step) 
x = arange(0.0, 25, 0.1)

plot(x, 0.0 * x + 1.00)

plot(x, 0.0765 * x + 1.00) 

plot(x, 0.153 * x + 1.00) 

plt.show()

#how to calculate the linear regression equation. 
#first number is slope and second is y intercept 
linear_regression_0 = np.polyfit(rub_stront, sr_sr_0, 1)

linear_regression_10 = np.polyfit(rub_stront, sr_sr_10, 1)

linear_regression_20 = np.polyfit(rub_stront, sr_sr_20, 1) 

#print "This is the first linear regression line:", linear_regression_0
#print "This is the second linear regression line.", linear_regression_10
#print "This is the third linear regression line.", linear_regression_20




#********************* Problem #3 is right here ***************************** 
meteorite = ['Moore County', 'Juvinias', 'Pasamonte', 'Sioux County', 'Nuevo Laredo', 'Jonzac', 'Stannern', 'Babi']

#87-Rb / 86-Sr 
#These values should be on the X-axis
rubidium_strontium = [0.00234, 0.00644, 0.00769, 0.00775, 0.01228, 0.01671, 0.02396, 0.0]

#87-Sr / 86-Sr
#These values should be on the Y-axis
strontium_strontium = [0.699140, 0.699378, 0.699481, 0.699491, 0.699840, 0.70062, 0.700475, 0.698990]


plot(rubidium_strontium, strontium_strontium, 'ro')
plt.xlabel('87 Rubidium / 86 Strontium')
plt.ylabel('87 Strontium / 86 Strontium ')
plt.title('Rubidium & Strontium Compotion of Meteorites')
#plt.text(60, 0.25,'$y = 3/2 x + stuff$')
#plt.axis([0, 0.03, 0.6988, 0.7010])
plt.grid(True)

#arange is (start, stop, step) 
x = arange(0.0, 0.03, 0.001)

plot(x, 0.0722 * x + 0.6989)

plt.show()

#how to calculate the linear regression equation. 
#first number is slope and second is y intercept 
linear_regression = np.polyfit(rubidium_strontium, strontium_strontium, 1) 

print linear_regression


#************************** problem #4 is right here  *** ********************


portion_of_rock = ['Whole rock', 'Plagioclase', 'Pyroxene A', 'Pyroxene B', 'Ilmenite', 'Cristobalite A', 'Cristobalite B']

#87-Rb / 86-Sr 
#These values should be on the X-axis 
Rubidium_Strontium = [0.00982, 0.00159, 0.0252, 0.0197, 0.0501, 0.0629, 0.0844]


#87-Sr / 86-Sr 
#These values should be on the Y-axis 
Strontium_Strontium = [0.69962, 0.69919, 0.70060, 0.70011, 0.70173, 0.70236, 0.70362]

#a bunch of settings for the plot. 
plot(Rubidium_Strontium, Strontium_Strontium, 'ro')
plt.xlabel('87 Rubidium / 86 Strontium')
plt.ylabel('87 Strontium / 86 Strontium ')
plt.title('Rubidium and Strontium in Apollo 11 rock 44 from the Sea of Tranquility')
plt.text(60, 0.25,'$y = 0.0527282 x + 0.699$')
plt.axis([0.0, 0.1, 0.6988, 0.7040])
plt.grid(True)

#arange is (start, stop, step)
#we need to calculate values for the function if we want to plot it.  
x = arange(0.0, 0.1, 0.001)

plot(x, 0.0527282 * x + 0.699)

plt.show() 



#how to calculate the linear regression equation. 
#first number is slope and second is y intercept 
linear_regression = np.polyfit(Rubidium_Strontium, Strontium_Strontium, 1) 

print linear_regression
