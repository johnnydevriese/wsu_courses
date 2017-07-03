from pylab import * 
import sympy as sp 

#why do we care
#cite where the tnak comes from 
#and then how we attack the problem. 
#how we did the numerics, but no snippets of code. 


#In general, we want to use symbolic variables. 
sp.var('x,y') 

alpha_values = arange(0,0.02 + 0.001, 0.001) 

#print alpha_values 

volumes = zeros(len(alpha_values))

for i in arange(len(alpha_values)):
	#~ volumes[i] = alpha_values[i] 
#~ 
#~ print "these are the volumes:{}".format(volumes)

	#initialize the variables, just for fun... 
	lower_limit = 0.0 
	upper_limit = 0.0 

	#now we can define expressions in terms of symbolic variables. 
	function = 0.0002017404542*x**2 + (0.0001303290910 * y ** 2) / (0.9520444748 + alpha_values[i] * y)- 1.0

	#substitue x = 0 into the expression. 
	z = function.subs(x,0) 
	#solve for y now so we have y = stuff 
	roots = sp.solve(z, y)

	#print roots 

	#this returns a list that we can then access them in the usual indexed way. 
	lower_limit = roots[0]
	upper_limit = roots[1] 

	#~ print lower_limit
	#~ print upper_limit
	  
	#to find out what the limits are we will have to set x = 0 and find out the two values for y. These two values will be our upper and lower limit of integration. 

	#First we need to solve the equation for only one variable. I want to solve for x as a function of y (i.e. x(y) ) 
	integrand = sp.solve(function, x) 

	def evaluate(t): 
		return pi * integrand[1].subs(y,t)**2 
	
	#~ could use a lambda function to evalutate the integrand. 
	#~ something = lambda t: pi * integrand[1].subs(y,t)**2 

	#~ sp.pprint (integrand[1])

	#We could then integrate this using spherical shells. Which is like integral of pi * R^2 dR where R is the radius. 
	#In our case the R will be the value of x at some point y 
	volumes[i] = sp.mpmath.quad(evaluate, [lower_limit, upper_limit] )  * 0.000264172 #converting to gallons 
	#~ volumes[i] = volumes[i] * 0.000264172 

	#volume = sp.mpmath.quad(something, [lower_limit, upper_limit])

#this volume is in cm^3 
print "this is the volume:{0} for {1}".format(volumes,alpha_values) 

#~ calculating the number of wine bottles we would expect from the tank! 

bottle_of_wine = 1.8011927068878e6 / 750 

print 'We have {0} bottles of wine on the wall.' .format(bottle_of_wine)

a = '\\alpha' 

plt.plot(alpha_values,volumes) 
plt.title('Alpha($%s$) vs. Volume'%a) 
plt.xlabel('Value of Alpha($%s$)'%a) 
plt.ylabel('Volume Of Object') 
plt.axis([0, 0.02, 460, volumes[-1]])
plt.show()


#for alpha=0.005 we have 475.82467976 gallons or 1801192.70688783  cm^3 or 1.8011927068878*10^6 mL  (milliliters)


#************** THIS PLOT THE FUNCTION ************************** 
#little snippet of code to plot the function. 
#~ from sympy import *
#~ x, y = symbols('x y') 
#~ 
#~ 
#~ eq = Eq((0.0002017404542*(x)**2)+((0.0001303290910*(y)**2) / (0.9520444748+0.005*y)) - 1.0) 
#~ 
#~ plot_implicit(eq,(x,-75,75),(y,-80,150))








