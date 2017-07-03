#************** THIS PLOT THE FUNCTION ************************** 
#~ import numpy as np
#~ import matplotlib.pyplot as plt
#~ 
#~ alpha = 0.005 
#~ 
#~ #a = 0.0002017404542*x**2 + (0.0001303290910 * y ** 2) / (0.9520444748 + alpha * y)- 1.0
#~ 
#~ #dom hoofd you cannot write shit like this with two equal signs! 
#~ #a = 0.0002017404542*x**2 +(0.0001303290910 * y ** 2) / (0.9520444748 + alpha * y) = 1
#~ 
#~ # Note the order of y,x.
#~ y,x=np.ogrid[-70:110:100j,-75:75:100j]
#~ plt.contour(x.ravel(),y.ravel(),0.0002017404542*x**2 + ((0.0001303290910 *y **2) / (0.9520444748 + alpha * y) )- 1.0,[1])
#~ plt.xlabel('horizontal section(cm)')
#~ plt.ylabel('vertical section(cm)')  
#~ plt.title('Cross Section of Wine Barrel') 
#~ plt.grid()
#~ 
#~ plt.show()
#~ 

from sympy import *
x, y = symbols('x y') 

alpha = 0.001

eq = Eq(( 0.0002017404542*(x)**2)+((0.0001303290910*(y)**2) / (0.9520444748+alpha*y)) - 1.0) 

plot_implicit(eq, (x,-75,75), (y,-80,150) )
