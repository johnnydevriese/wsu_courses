from pylab import * 


def trapezoid(f,a,b,n): 
	h = float(b-a)/float(n)
	#otherwise he won't get the b. 
	x = arange(a,b+h,h)
	fx = f(x)
	#division takes longer than multiplication
	integral = h*0.5*(fx[0]+fx[n]+2.0*sum(fx[1:n]))
	
	return integral
