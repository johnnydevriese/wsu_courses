from pylab import * 

# STRINGS 
hello = 'Hello, ' 
print(hello[6])

world = """world!"""

hi = hello + world

print(hi) 

# Strings are objects. 
print(hi.upper())
#the () mean that they are METHODS of the CLASS

#Object oriented porgramming 
#Python encourages the use of "objects" - 
#basically an object is always a collection of data together with functions to manage and manipulate those data. 
#Thus each object is an entity that acts as a caretake for its private data. 
#when we use the notation object_name.method_name
#we are requesting that the object access or deliver or change some part of its data. 

#there is no sprint. Instead we use the format method. 

n = 4
mytitle = '''Line segments used in trapezoids rule on {} subinterverals'''.format(n)
print(mytitle) 
#we can do multiple arguments 
times = "it was the {} and {}".format('best','worst') 
print(times) 

#we can use a colon to specify formatting details. 
error = pi/1000.

err_str = 'the nrom of the error is {:.4f} '.format(error) 
#six before the decimal and four after the decimal 
err_str = 'the nrom of the error is {:10.4f} '.format(error) 
#we can do scientific notation too 
#python will always display the number first, the number of digits right of the decimal, and then maybe do how much total space you told it to. 
err_str = 'the nrom of the error is {:8.4e} '.format(error) 

print(err_str) 

#gon wryt a trap rule 
def trapezoid(f,a,b,n): 
	h = float(b-a)/float(n)
	#otherwise he won't get the b. 
	x = arange(a,b+h,h)
	fx = f(x)
	#division takes longer than multiplication
	integral = h*0.5*(fx[0]+fx[n]+2.0*sum(fx[1:n]))
	
	return integral
	
def f(x): 
	return x*x

a = 0.0
b = 1.0 
n = 4.0 

print(trapezoid(f,a,b,n))


#****************************** NOV. 9th NOTES ********************************* 
# Flow control!! 

for i in [0,1,2,3]:
	print(i)
	
for i in arange(0,4):
	print(i) 

for i in range(4): 
	print(i) 


# When do we need 'for' loops? 
#1. when each new computation depends on the result of previous computations. 
#2. When we need to fill in the entries of an array
# in a particularly complicated way, possibly dependent on other entries. (partially overlaps number 1) 


# Legendre polynomials 
# three term recurrence relation. : 
# (n+1)P_{n+1} (x) = (2n+1) xP_n(x) - nP_{n-1}(x) 
#plot these up to degree d 
#legendre polynomials are defined from -1 to 1 

#this is how kcooper would do it. 
d = 4 
delta_x = 0.02 
x = arange(-1.0,1.0+delta_x,delta_x) 
n_points = len(x) 
#make a d by n_points matrix and then fill each row with each legendre polynomial. 
L = zeros([d+1,n_points]) 
#colon says: just get em all 
L[0,:] = ones([1,n_points]) #legendre polynomial of degree 0 
L[0,:] = x  #legendre polynomial of degree 1 

plot(x, L[0,:], 'b', x, L[1,:])



#need to go one beyond otherwise we won't get the whole thing!! 
for n in arange(1,d): 
	L[n+1,:] = (1.0/(n+1.0)) *((2.0*n+1.0) * x * L[n,:] - n*L[n-1,:]) 
	plot(x, L[n+1,:], 'b')
	
#we can approximate a function with a series of polynomials! And in the limit the polynomials converge to the actual function! 

title('Legendrre Polynomials up to degree {}'.format(d)) 
xlabel('x')
#we can render this in latex! 
ylablel(r'$P_n(x)$') 
xlim(-1,1)


show()

#************************* November 13th notes ******************************* 

#from numpy import * 
#we can import files other ways. 
#import time 

#I can time stuff as follows 
t0 = time.time() 
print(t0) 
t1 = time.time() = t0 
print(t1) 


#import strings as s 
#can call things in strings with prefix "s."

def f(x): 
	return (x>pi/4.0) * (x-pi/4.0) 
	
#kcooper is trying to screw up trazpezoidal rule 
def g(x): 
	return (x>pi/4.0) 

exact = 0.5 * (1-pi/4.0)**2 
exactg = 1.0-pi/4.0 

t0 =time.time() 
trap_approx = s.trapezoid(f,0,1, 100)
t1 = time.time() - t0 
print(t1) 

print('the trap error was {}'.format(exact-trap_approx))

def adaptive_trap(f, a, b, tolerance): 
	#we need the function values. 
	fleft = f(a) 
	fright = f(b) 
	#base times height to get the area. 
	int_coarse = float(b-a) * (fleft + fright) * 0.5 
	f_this = float(a + b) * 0.5
	int_fine = 0.25 * float(b-a) * (fleft+fright+ 2.0*f(f_this)) 
	difference = absolute(int_coarse - int_fine)
	#this is the fail safe if statement. if the thing is on order of machine precision then just be done. 
	if float(b-a) < 1e-14:
		return int_fine 
	
	elif tol < difference : 
		tol2 = tol * 0.5 
		return adaptive_trap(f, a, f_this, tol2) + adaptive_trap(f, f_this, b, tol2)	
		
	else: 
		return int_fine 
		
t0 = time.time() 
adapt_int = adaptive_trap(f,0.0, 1.0, 0.0000001) 
t1 = time.time()  -t0 
#print (adapt_int-exact)

#tolerances never catches up with error 







