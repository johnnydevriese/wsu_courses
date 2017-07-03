from pylab import * 
import string 
import numpy as np 
from numpy.polynomial.polynomial import polyval


def p(x): 

	#x = 0.0

	#get user input, feel incredibly reckless and don't check user input at all. 
	#surname = raw_input("What is your last name?")

	#convert to lowercase. 
	#surname = surname.lower()

	surname = 'minor' 

	#print surname

	#intializing an array to store the numbers. 
	numbers = np.zeros(len(surname)) 

	#converting from the ASCII values to make 'a' = 1 
	for i in range(len(surname)): 
		numbers[i] = ord(surname[i])  - 96.0

	#print numbers 

	#subtracting 13 as part of the original problem.  
	for i in range(len(numbers)): 
		numbers[i] -= 13.0

	#print numbers 

	for i in range(len(numbers)): 
		numbers[i] = numbers[i] / 6.0 
	#print numbers 
		
	for i in range(len(numbers)): 
		numbers[i] = numbers[i] / np.power(2.0, i) 
		
	print numbers 

	#evaluates a polynomial using horner form
	#http://docs.scipy.org/doc/numpy-1.10.1/reference/generated/numpy.polynomial.polynomial.polyval.html
	p = polyval(x,numbers) 

	#print p 



	return p

#a simple example of evaluating at x=0 
#a = p(0) 

#print a 


