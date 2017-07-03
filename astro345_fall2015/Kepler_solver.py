import math
import numpy 
import scipy 
import pylab
import scipy.optimize

#this file defines three functions. The original Kepler equation that takes arguments of eccentricity and mean anomaly. 
#it defines the derivative function
#defines a function that should solve for the root with the given eccentricity and mean anomaly. 

 

#definition of the kepler equation. I moved the mean anomaly to the RHS so I could solve for when it is zero 
def f(x, eccentricity, mean_anomaly): 
	
	y = x - (eccentricity * numpy.sin(x)) - mean_anomaly
	
	return y 	
	

#we don't actually use mean_anomaly but otherwise python/numpy will complain! 
def f_prime(x, eccentricity, mean_anomaly): 
	
	y = 1.0 - (eccentricity * numpy.cos(x)) 
	
	return y	

def Kepler_solve(eccentricity, mean_anomaly): 
	
	#tol is tolerance allowed for the root. 
	#for further documentation go to: 
	#http://docs.scipy.org/doc/scipy-0.16.0/reference/generated/scipy.optimize.newton.html
	root = scipy.optimize.newton(f, .2, fprime = f_prime, args = (eccentricity, mean_anomaly), tol=1.48e-08 )
	
	return root
	
#just some testing below... 	
	
#eccentricity = 0.2 
#mean_anomaly = 0.8 

#x = numpy.linspace(-10.0,10.0,100)	
	
#root = Kepler_solve(eccentricity, mean_anomaly) 

#print root 

#root = scipy.optimize.newton(f, .2, fprime = f_prime, args = (eccentricity, mean_anomaly) )		

#print root 
