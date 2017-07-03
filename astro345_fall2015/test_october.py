import math
import numpy 
import scipy 
import pylab
import scipy.optimize



def f(x): 
	
	f = numpy.power(x,3) 
	
	return f 
	
def g(x): 
	
	y = x - 0.2 * numpy.sin(x) - 0.2
	
	return y 		
	
	
	
	
	
x = scipy.optimize.newton(f, 0.0 )
	
print(x)	



	
x = scipy.optimize.newton(g, 0.0 )
	
print(x)	
