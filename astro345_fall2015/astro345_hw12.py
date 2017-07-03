import matplotlib.pyplot as plt
from pylab import * 

def moon(x): 
	
	P = 3340 * 1.622 * x 
	
	return P 
	
def mars(x): 
	P = 3930 * 3.711 * x 
	return P
	
def earth(x): 
	P = 5510 * 9.807 * x 
	return P 

def jupiter(x): 
	P = 1330 * 24.79 * x 
	return P 
	
def f(x): 
	P = 4e9
	return ones(shape(x)) * P	

x = arange(0,3e6,100)

y_max = earth(3e6) 

plt.xlabel('Depth Inside Planet (meters)')
plt.ylabel('Pressure Inside Planet (Pascals)')
plt.title('Depth vs Pressure for Planets')

plt.plot(x,f(x)) 

plt.plot(x,moon(x), label='Moon')
plt.plot(x,mars(x), label='Mars')
plt.plot(x,earth(x), label='Earth')
plt.plot(x,jupiter(x), label='Jupiter')


 
plt.axis([0,3e6,0,y_max])

plt.legend()

#~ plt.plot([1,2,3,4])
#~ plt.ylabel('some numbers')
plt.show()
