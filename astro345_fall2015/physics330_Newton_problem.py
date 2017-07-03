import math
import numpy 
import scipy 
import pylab
import scipy.optimize



def f(x): 
	y = ( ( 0.965 + 1.0 ) / ( 0.2588 ) ) * x + numpy.log( 1 - ( x / 0.2588 ) ) 
	return y 
	
def y(x): 
	
	y = ( ( 0.9659258263 + 1.0 ) / ( 0.2588190451 ) ) + ( 1 / ( 1 - (x / 0.2588190451)) ) * (- 1.0 / 0.2588190451 )
	
	return y 	
	

#x = numpy.linspace(0.0,0.3,100) # 100 linearly spaced numbers
#y = f(x) # computing the values of f(x) 


#pylab.plot(x,y) 
#pylab.axis([0, 0.5, -0.5, 0.5]) #axis() command in the example above takes a list of [xmin, xmax, ymin, ymax]
#pylab.show() # show the plot

x = scipy.optimize.newton(f, .2, fprime = y )
	
print(x)










