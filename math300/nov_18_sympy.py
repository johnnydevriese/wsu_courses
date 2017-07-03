#sympy 

from pylab import * 
import sympy as sp 


print(pi) 
print(sp.pi) 

#there is a symbolic pi, which we can evaluate using the evalf method. 

#get 32 digits of pi 
print(sp.pi.evalf(32))

#There are other kinds of numeric objects 

p = sp.Rational(3,7) 
q = sp.Rational(2,3) 
print(p+q)
print(p*q) 

#when dealing with symbolic results, things can get ugly 
print(sp.integrate('x*sin(3/x)'))

#that is ugly. Sympy has a "pretty print" function. 
sp.pprint(sp.integrate('x*sin(3/x)'))

#In general, we want to use symbolic variables. 
sp.var('x,y') 
sp.pprint(x/2) 


#now we can define expressions in terms of symbolic variables. 
s = x*sp.sin(3/x) 

#Now we can evaluate this expression anywhere. 
print(s.subs(x,pi))

#kcooper does song and dance between 'f' and 'f(x)' 
#f(x) is NOT a function, it's the value of the function. It's the value of function 
# f is just the function and is a rule for mapping one input to another. 
#function you give it an input and get an output. 
#s is just an expression and is a collection of symbols you cannot do s(x) 
print(s.subs(x,pi).evalf(50))


#We have noted that s is an expression. Let's make a function. 

t = lambda x: x*sp.sin(3/x) 

#y is a symbolic variable. 
#Note now the difference between the expression s and the function t 
sp.pprint(s(y))
sp.pprint(t(y))

#Now let's define a new expression. 
#don't care about 64.0 or anything because they are just symbolic numbers and we could use evalf() to evalute to arbitrary precision 
u = 64*x**4-100*x**3 + 22*x**2 - 65*x+4

#didn't have to tell him how many points to choose or anything. 
sp.plot(u,(x,-.5,1.5))
#sympy plot doesn't need the show() command 

3h = arange(-0.5,1.5,0.001)

h = (1.5 -(-.5))/1000.0 
x_vec = arange(-.5,1.5+h,h)

u_vec = zeros(len(x_vec))

#have to evaluate u at 1001 points. 
for i in arange(len(x_vec)): 
	u_vec[i] = u.subs(x, x_vec[i])

plot(x_vec, u_vec)
show() 


#***********************************NOVEMBER 30TH LECTURE NOTES ******************************* 

#trying to find the root of the polynomial. K Cooper designed it to have the root at x = 1/16 
print(u.subs(x,sp.Rational(1,16)))
first_root = sp.Rational(1,16) 

v = sp.simplify(u / (x-first_root))
sp.pprint(v)


#simplify always checks to divide out polynomial factors, and execute trig identities. 
#x^2 + 2x + 1 is a perfect square. 
sp.pprint((x**2 + 2*x + 1) / (x + 1) )
sp.pprint(sp.simplify((x**2 + 2*x + 1) / (x + 1)))
sp.pprint((sp.sin(x)**2 + sp.cos(x)**2 / sp.cos(x)))u  



#We can factor polynomials 
sp.pprint(u.factor()) 

#we can also expand polynomials 
w = u.factor()
sp.pprint(w) 
sp.pprint(sp.expand(w)) 

sp.var('a')
p = (x -1) * (x-a) * (x +a) 

sp.pprint(p.expand().collect(x))
sp.pprint(p.expand().collect(a))
sp.pprint(sp.horner(p,x))

#sympy can do calculus 

#this limit would be 1 
sp.pprint(sp.limit(sp.sin(x) / x , x, 0))

#limit would be zero(0) because it's 0 * bounded function 
sp.pprint(sp.limit( x * sp.sin(3/x), x, 0))

#you can take a limit of a limit 
sp.pprint(sp.limit(sp.limit((x**2+1) / (a*x**2 + 2*x + 1), x , sp.oo), a, 97)

#sympy can take derivatives
#differentiate u with respect to x  
sp.pprint(sp.diff(u,x))

#we can take a second derivative. 
sp.pprint(sp.diff(u,x,2))

u_prime = sp.diff(u,x) 
sp.pprint(u_prime) 

u_double_prime = sp.diff(u,x,2)
sp.pprint(u_double_prime.expand() - sp.diff(u_prime,x))

#the things inside would have to be REAL 
arc_length_integrand = sp.sqrt(1 + sp.diff(u,x)**2)

arc_length = sp.integrate(arc_length_integrand, (x,0,1)) 

#it doesn't know how to evaluate the integral so it'll just print the last known correct answer. 
#but we need to force it to do the integral 
sp.pprint(arc_length)

#can get 10 digits if you want. 
arc_length = sp.integrate(arc_length_integrand, (x,0,1)).evalf(10) 
sp.pprint(arc_length) 

#more integrals 
#u is a quartic polynomial 
sp.pprint(sp.integrate(u))

sp.pprint(sp.integrate(arc_length) )

#showing to use a tuple going from negative infinity to positive infinity. 
#use .evalf() to make him do it with 20 digits of accuracy. 
sp.pprint(sp.integrate(sp.exp(-x**2), [x,-sp.oo,sp.oo]).evalf(20))
#solution is sqrt(pi) 

# ******************* SERIES **********************88 
#why do we learn series? because polynomials are what we can evluate on a computer. 
#anything we can write as a series we can integrate. 

s = sp.series(sp.sin(x), x)

sp.pprint(s)

#big O denotes what the dominant term is. Exampel is  O<x^6> means that x^6 is the dominant term  

#can expand something other than 0. 
s = sp.series(sp.sin(x), x, 3)

#now what if we want 16 terms from the series. 
s = sp.series(sp.sin(x), x, 3, 16) 

#this would be expanding around 0 
s = sp.series(sp.sin(x), x, 0, 16) 

#you get a list of ordered terms. We could reconstruct the function by taking the sum of these terms in the list. 
t = s.as_ordered_terms() 

#if you give it a negative index it will start at the end. 
t = sum(s.as_ordered_terms()[0:-1])
 
sp.pprint(t) 

h = 0.01 
x_vec = arange(-1.0, 1.0 + h, h) 

#y_vec must be numbers! 
y_vec = zeros(len(x_vec))

for i in arange(len(x_vec)): 
	y_vec[i] = t.subs(x, x_vec[i]).evalf()

plot(x_vec, y_vec, x_vec, sin(x_vec)) 
show()


#********************* DECEMBER 4th NOTES *************** 

#we could use less terms to make it look worse. 


















