
import math
import numpy 
import scipy 
import pylab
import scipy.optimize


def f(x, eccentricity, mean_anomaly): 
	
	y = x - eccentricity * numpy.sin(x) - mean_anomaly
	
	return y 	
	
	
#we don't actually use mean_anomaly but otherwise python will complain! 
def f_prime(x, eccentricity, mean_anomaly): 
	
	y = 1.0 - eccentricity * numpy.cos(x) 
	
	return y	
	
eccentricity = 0.2 
mean_anomaly = 0.8 

#x = numpy.linspace(-10.0,10.0,100)

def Kepler_solve(eccentricity, mean_anomaly): 
	
	root = scipy.optimize.newton(f, .2, fprime = f_prime, args = (eccentricity, mean_anomaly) )
	
	return root
	
root = Kepler_solve(eccentricity, mean_anomaly) 

print root 

root = scipy.optimize.newton(f, .2, fprime = f_prime, args = (eccentricity, mean_anomaly) )		

print root 
