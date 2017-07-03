from snippet import * 
from Kepler_solver import * 
import math
from pprint import pprint

#original date to match Guy Worthey's values 
JDE = 2816786.5000

#julian day for september 1 2015 
#JDE = 2457266.500000

#julian day for october 1 2015
#JDE = 2457296.500000

#julian day for november 1 2015
#JDE = 2457327.500000


T = (JDE - 2451545.0 ) / 36525.0


#this will be a list where all of the L values of each planet are located. 
#L_planets[0] would be L for Mercury and L_planets[1] would be L for Venus and etc... 
L_planets = [0.00] * 8 
a_planets = [0.00] * 8 
e_planets = [0.00] * 8 
i_planets = [0.00] * 8 
Omega_planets = [0.00] * 8 
pi_planets = [0.00] * 8 
M_planets = [0.00] * 8 

			
for i in range(8): 
	L_planets[i] = L8[i][0] + L8[i][1]*T + L8[i][2]*numpy.power(T,2) + L8[i][3]*numpy.power(T,3)  
	L_planets[i] = L_planets[i] * 0.01745329251

#~ print 'these are L values for the planets' 
#~ pprint(L_planets)

for i in range(8): 
	a_planets[i] = a8[i][0] + a8[i][1]*T + a8[i][2]*numpy.power(T,2) + a8[i][3]*numpy.power(T,3)  
	#a_planets[i] = a_planets[i] * 0.01745329251


#~ print 'these are a values for the planets'
#~ pprint(a_planets)


for i in range(8): 
	e_planets[i] = e8[i][0] + e8[i][1]*T + e8[i][2]*numpy.power(T,2) + e8[i][3]*numpy.power(T,3)  
	#e_planets[i] = e_planets[i] * 0.01745329251

#~ print 'these are the e values for the planets'
#~ pprint(e_planets)

for i in range(8): 
	i_planets[i] = i8[i][0] + i8[i][1]*T + i8[i][2]*numpy.power(T,2) + i8[i][3]*numpy.power(T,3)  
	i_planets[i] = i_planets[i] * 0.01745329251

#~ print 'these are the i values for the planets'
#~ pprint(i_planets)	
	
for i in range(8): 
	Omega_planets[i] = Om8[i][0] + Om8[i][1]*T + Om8[i][2]*numpy.power(T,2) + Om8[i][3]*numpy.power(T,3)  
	Omega_planets[i] = Omega_planets[i] * 0.01745329251	
	
#~ print 'these are the Omega values for the planets'
#~ pprint(Omega_planets)	

for i in range(8): 
	pi_planets[i] = pi8[i][0] + pi8[i][1]*T + pi8[i][2]*numpy.power(T,2) + pi8[i][3]*numpy.power(T,3)  
	pi_planets[i] = pi_planets[i] * 0.01745329251

#~ print 'these are the pi values for the planets'
#~ pprint(pi_planets)


#I ~THINK~ M is in degrees?
for i in range(8): 
	M_planets[i] = L_planets[i] - pi_planets[i]


print'this is M for the planets'	
pprint( M_planets)


#****************************** END of the FIRST TABLE (we have M, a, e, i, Omega, and pi) *********************************



#Now, we have to solve for r and theta(nu) using the Kepler equation. 
#first find E-the eccentric anomaly using the newton Raphson method 
#Once we solve for E we can find r and theta (nu). 

# r = a(1 - eccentricity * cos(E) ) 
# tan(theta/2) = sqrt((1+eccentricity) / (1-eccentricity)) * tan(E/2)

E_planets = [0.00] * 8 

for i in range(8): 
	E_planets[i] = Kepler_solve(e_planets[i], M_planets[i]) 

#print 'This is E for the planets'
#print E_planets 

#this is just a check to make sure that the newton method is working correctly. 
#which it is --  this number agrees with a simple test on wolfram alpha... 
#~ temp = Kepler_solve(0.2,0.8)
#~ print 'this is temp:',temp 

r_planets = [0.00] * 8 

for i in range(8):
	
	r_planets[i] = a_planets[i]*(1.0 - e_planets[i] * numpy.cos(E_planets[i]))

#~ print 'this is r of the planets' 
#~ pprint(r_planets)		

nu_planets = [0.00] * 8

for i in range(8): 
	
	temp = numpy.sqrt((1.0 + e_planets[i])/(1.0 - e_planets[i]))
	#print'this is temp:', temp 
    
	nu_planets[i]=2.0*numpy.arctan(temp * numpy.tan((E_planets[i] / 2.0))) 
	
	if nu_planets[i] <= 0:		
		nu_planets[i] += 2.0 * numpy.pi 

#~ print'this is nu of the planets'	
#~ pprint(nu_planets)

 
#***************** done with calculation of r and nu(theta) ********************* 
	 
	 
	 
#now we need to find F, G, H, and P, Q, R (Equation 33.7 on p 228) 

F_planets = [0.00] * 8 
G_planets = [0.00] * 8 
H_planets = [0.00] * 8 

P_planets = [0.00] * 8 
Q_planets = [0.00] * 8 
R_planets = [0.00] * 8 

#these were constants that were defined in the book on page 228 
sin_e = 0.397777156
cos_e = 0.917482062

for i in range(8): 
	F_planets[i] = numpy.cos(Omega_planets[i])
	
for i in range(8): 
	G_planets[i] = numpy.sin(Omega_planets[i]) * cos_e
	
for i in range(8):
	H_planets[i] = numpy.sin(Omega_planets[i]) * sin_e
	
for i in range(8): 
	P_planets[i] = -numpy.sin(Omega_planets[i]) * numpy.cos(i_planets[i]) 
	
for i in range(8): 
	Q_planets[i] = numpy.cos(Omega_planets[i]) * numpy.cos(i_planets[i])*cos_e - numpy.sin(i_planets[i]) * sin_e
	
for i in range(8): 
	R_planets[i] = numpy.cos(Omega_planets[i]) * numpy.cos(i_planets[i]) * sin_e + numpy.sin(i_planets[i]) * cos_e 
	
	
#We could check that these relations are correct with: F^2 + G^2 + H^2 = 1 and P^2 + Q^2 + R^2 = 1 

test_FGH = [0.00] * 8 
test_PQR = [0.00] * 8

for i in range(8): 
	test_FGH[i] = numpy.power(F_planets[i],2) + numpy.power(G_planets[i],2) + numpy.power(H_planets[i],2) 

#F G and H are equal to ~ONE! - GOOD! 
#print test_FGH

for i in range(8): 
	test_PQR[i] = numpy.power(P_planets[i],2) + numpy.power(Q_planets[i],2) + numpy.power(R_planets[i],2) 

#F Q and R are equal to ~ONE! 
#print test_PQR 	

#Now, we need A, B, C and a, b, c (on p 229) 

A_planets = [0.00] * 8 
B_planets = [0.00] * 8 
C_planets = [0.00] * 8 

a_const_planets = [0.00] * 8 
b_const_planets = [0.00] * 8 
c_const_planets = [0.00] * 8 

#in the packet is it says:"the quantities a, b, c should be taken positive, while the angles A, B, C should be taken in the correct quadrant, 
#according to the following rules: sin(A) has the same sign as cos(Omega) 
#sin(B) and sin(C) have the same sign as sin(Omega). Apparently you can use the arctan2 function to achieve this result.  
for i in range(8): 
	A_planets[i] = numpy.arctan2(F_planets[i], P_planets[i]) 

for i in range(8): 
	B_planets[i] = numpy.arctan2(G_planets[i], Q_planets[i])
	
for i in range(8): 
	C_planets[i] = numpy.arctan2(H_planets[i], R_planets[i])
	
for i in range(8): 
	a_const_planets[i] = numpy.sqrt(numpy.power(F_planets[i],2) + numpy.power(P_planets[i],2))
	
for i in range(8): 
	b_const_planets[i] = numpy.sqrt(numpy.power(G_planets[i],2) + numpy.power(Q_planets[i],2))
	
for i in range(8): 
	c_const_planets[i] = numpy.sqrt(numpy.power(H_planets[i],2) + numpy.power(R_planets[i],2))	
	
#with these values we can compute what x y and z are! 
#from equation 33.9 on page 229

X_planets = [0.00] * 8 
Y_planets = [0.00] * 8 
Z_planets = [0.00] * 8 

#we need lowercase omega to calculate the xyz! 
omega_planets = [0.00] * 8 
 
for i in range(8): 
	 omega_planets[i] = pi_planets[i] - Omega_planets[i]

for i in range(8): 
	X_planets[i] = r_planets[i] * a_const_planets[i] * numpy.sin((A_planets[i] + omega_planets[i] + nu_planets[i]))
	
#~ print 'This is X'
#~ pprint(X_planets)	
	
for i in range(8): 
	Y_planets[i] = r_planets[i] * b_const_planets[i] * numpy.sin((B_planets[i] + omega_planets[i] + nu_planets[i]))
	
#~ print 'This is Y'
#~ pprint(Y_planets)	
	
for i in range(8):
	Z_planets[i] = r_planets[i]	* c_const_planets[i] * numpy.sin((C_planets[i] + omega_planets[i] + nu_planets[i]))

#~ print 'This is Z'
#~ pprint(Z_planets)

#**************** end of X, Y, Z coordinates. They all match Dr. Worthey's values!! *************************

	
#now we have to compute the right ascension and declination (alpha and delta) 

#we want to calculate from Earth's position so we set X,Y,Z equal to -xyz? 
#X = -Xearth 

#We need to add the sun to these x,y,z and say it is (0,0,0) 
X_planets.append(0.00) 
Y_planets.append(0.00) 
Z_planets.append(0.00) 

#pprint (X_planets)

X_earth = -X_planets[2]  	
Y_earth = -Y_planets[2]
Z_earth = -Z_planets[2]


eta_planets = [0.00] * 9 
zeta_planets = [0.00] * 9 
xi_planets = [0.00] * 9 
Delta_planets = [0.00] * 9 

alpha_planets = [0.00] * 9 
delta_planets = [0.00] * 9 

#subtracting off the earth from each elements. 
for i in range(9): 
	xi_planets[i] = X_earth + X_planets[i] 
	
for i in range(9): 
	eta_planets[i] = Y_earth + Y_planets[i]
 
for i in range(9): 
	zeta_planets[i] = Z_earth + Z_planets[i]

for i in range(9): 
	Delta_planets[i] = numpy.sqrt(numpy.power(xi_planets[i],2) + numpy.power(eta_planets[i],2) + numpy.power(zeta_planets[i],2)) 
	
for i in range(9): 	
	alpha_planets[i] = numpy.arctan2(eta_planets[i],xi_planets[i])
	
	if alpha_planets[i] < 0: 
		alpha_planets[i] += 2.0 * numpy.pi 
		
for i in range(9): 
	delta_planets[i] = numpy.arcsin( zeta_planets[i] / Delta_planets[i] ) 	
	
#it gives 'nan' so I'll just set it to 0.00 for now... I'm assuming this is because we're trying to divide by zero... 	
delta_planets[2] = 0.00
	
print'these are alpha for the planets (Right Ascension)'
pprint(alpha_planets)	
 
print'these are lowercase delta for the planets(Declination)'
pprint(delta_planets)

alpha_hours = [0.00] * 9

#can multiply alpha*3.84 to get Dr. Worthey's numbers. (not sure why it is multiplied by 3.84...) 

for i in range(9): 
	alpha_hours[i] = alpha_planets[i] * 3.819718655480724962487772
	
print'these are right ascension in hours'
pprint(alpha_hours) 	

degrees_delta_planets = [0.00] * 9

#converting from radians back to degrees.

for i in range(9):
	degrees_delta_planets[i] = delta_planets[i] * 57.295715143328830

print'these are delta in degrees'
pprint(degrees_delta_planets)
