	
import math
import numpy 
import scipy 
import pylab
import scipy.optimize



#function definitions. 
def f(x, mean_anomaly): 
	
	y = x - 0.2 * numpy.sin(x) - mean_anomaly
	
	return y 
	
def f_prime(x): 
	
	y = 1.0 - 0.2 * numpy.cos(x) 
	
	return y 	
	
def newt(x,n):
	for i in range(n):
		if f_prime(x) == 0:
			return x
		x = x - f(x, mean_anomaly)/f_prime(x)
	return x	
	

x = numpy.linspace(-10.0,10.0,100) # 100 linearly spaced numbers
#y = f(x) # computing the values of f(x) 


#pylab.plot(x,y) 
#pylab.axis([0, 0.5, -0.5, 0.5]) #axis() command in the example above takes a list of [xmin, xmax, ymin, ymax]
#pylab.show() # show the plot




#our function f, the initial guess, and the derivative of the function. 

#getting input for the mean anomaly and checking to make sure it's positive

flag = 0 


while ( flag == 0) :
	
	mean_anomaly = float(raw_input("Enter the mean anomaly (i.e. t - T):" ))
	
	if(mean_anomaly > 0.0): 
	
		print'you entered:', mean_anomaly
	
		flag = 1
		
	
#f = f(x,mean_anomaly)

#root = scipy.optimize.newton(f, .2, fprime = f_prime)
	
#print(root)

root = 0 

#inital guess of 0.2 and setting 10 iterations. 
root = newt(0.2, 10)

print(root)


#converting from radians to degrees. 
root = root * ( 180.0 / numpy.pi ) 

print'this is the answer in degrees:' , root 

# we find that r this( from https://www.csun.edu/~hcmth017/master/node15.html) 
#r = a( 1 - eccentricity * cos(E) ) 



