#this is a comment 
from numpy import * 

print('Hello, World!')

#major differences between Python and CATLAB
#1. Results from scripts do not print unless you tell them. 

x = 5 
print(x)

#2. numbers are integers unless they have a decimal point. 
#decimal points taint an expression so all results are floats. 
print(3/4)
print(3.0/4.0)
print(3./4.) 
print(3./4)
print(3/4.) 


#3. many things require us to load package numpy. 
print(pi) 

#3a. In particular, we need Numpy for arrays we like. 
# Note that na ordinary array is called a list. 

x = [1, 2, 3]
 
print(x+x) 
print(2*x) 

#instead of lists, we use Numpy arrays. 

x = array([1,2,3])
print(x+x)
#4. in Python, all multiplication is elementwise 

#5. All arrays start with index 0. 
#Also, we refer to elements of arrays using brackets. 

print(x[0])
print(x[2])

#but python doesn't like this. 
#in matlab they were just linked lists but in python they are contiguous blocks of memory and thus faster! 
#x[3] = 4 

x = append(x,[4]) 

print('x is now', x) 

#can also just use resize to add a zero. 
x.resize(5)


# 6. The exponentiation operator is ** 
print(x**2) # we don't like exponentiation becuase it is a log operation and it is thus slow... 

#7. If you need to do matrix multiplication, use dot()
y = array([42, 2, 4, 67, 3])

print(x*y) 

print(dot(x,y))

x = array([6,6,6]) 
A = array([[1,0,0],[2,0,2],[3,-1,3]])

print(dot(A,x))


# We cna solve systems 
print(linalg.solve(A,x))

#****** Now it's November 4th 2015 ************* 

#slices! 

#lists vs arrays 
#arange is way of making proper array to do stuff. 
x = arange(5)
x = 1.0*arange(5) 
print(x) 

x = arange(1,6.0)
x = arange(1,6.0,2)

#python will stop at the number strictly less than that number.  
x = arange(-2.,2.00002,0.2)

#We can change entire sections of an array using slices. 

x[0:3] = pi 

#print(x) 

#want to do all of the odd entires as -1 


x[1:len(x):2] = -1 

x[1::2] = -9 #essentially leaving that entry blank! 

x[:] = -9 #this would be all of the elements. 

#We can make 2D arrays. How to make a 2D array would be a quiz question. 
A = zeros([3,4]) 

A[0:2,0:2] = pi 

print(A) #returns floating point zeros. 

#A = zeros(8) 

#print(A) 

A[2,0::2] = exp(1) 

A[1,3] = -1


print(A) 

#we can make functions again. 

f = lambda x: x * x 

print(f(2)) 

def g(x): 
	
	return x * x  



















