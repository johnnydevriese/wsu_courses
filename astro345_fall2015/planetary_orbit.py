from snippet import * 
from Kepler_solver import * 
import math
from pprint import pprint


JDE = 2816786.5000

T = (JDE - 2451545.0 ) / 36525.0

#python didn't like having 9.9999 as a power so I just rounded up to 10.
#but now I guess it doesn't care anymore...  
#T = math.ceil(T)  

#this will be a list where all of the L values of each planet are located. 
#L_planets[0] would be L for Mercury and L_planets[1] would be L for Venus and etc... 
L_planets = [0.00] * 8 
a_planets = [0.00] * 8 
e_planets = [0.00] * 8 
i_planets = [0.00] * 8 
Omega_planets = [0.00] * 8 
pi_planets = [0.00] * 8 
M_planets = [0.00] * 8 


for j in range(8): 
	for i in range(3): 
		
		if i == 0: 
			L_planets[j] += L8[j][0]
			
		L_planets[j] += (L8[j][i]*(T**i))**i
		
		#~ #convert from degrees to radians 
		#if I don't do it here then I would have to make another for loop to go through each entry! 
		if i == 2: 
			L_planets[j] = L_planets[j] * 0.01745329251
			
for i in range(7): 
	L_planets[i] = L8[i][0] + L8[i][1]*T + L8[i][2]*numpy.power(T,2) + L8[i][3]*numpy.power(T,3)  
	L_planets[i] = L_planets[i] * 0.01745329251

#~ print 'these are L values for the planets' 
#~ print L_planets

#python is actually clever enough that this is NOT needed! 
#~ j = 0 
#~ i = 0

for j in range(8): 
	for i in range(3): 
		
		if i == 0: 
			a_planets[j] += a8[j][0]
			
		a_planets[j] += (a8[j][i]*(T**i))**i
		
		#algorithm isn't right and is off by 1 because a only has only one value!  
		if i == 2: 
			a_planets[j] = a_planets[j] - 1.000
	
#using pprint we can print the columns, this prevents my eyes from bleeding! 
#~ print 'these are a values for the planets' 
#~ pprint( a_planets)

for j in range(8): 
	for i in range(3): 
		
		if i == 0: 
			e_planets[j] += e8[j][0]
			
		e_planets[j] += (a8[j][i]*(T**i))**i
		
		
		#algorithm isn't right and is off by 1 because a only has only one value! (?) 
		if i == 2: 
			e_planets[j] = e_planets[j] - 1.000

#~ print 'these are e values for the planets'
#~ pprint(e_planets)

for j in range(8): 
	for i in range(3): 
		
		if i == 0: 
			i_planets[j] += i8[j][0]
			
		i_planets[j] += (i8[j][i]*(T**i))**i
		
		#~ #convert from degrees to radians 
		#if I don't do it here then I would have to make another for loop to go through each entry! 
		if i == 2: 
			i_planets[j] = i_planets[j] * 0.01745329251

#these values are not as close as they really should be... 
#~ print 'these are i values for the planets'
#~ pprint (i_planets) 



for j in range(8): 
	for i in range(3): 
		
		if i == 0: 
			Omega_planets[j] += Om8[j][0]
			
		Omega_planets[j] += (Om8[j][i]*(T**i))**i
		
		#~ #convert from degrees to radians 
		#if I don't do it here then I would have to make another for loop to go through each entry! 
		if i == 2: 
			Omega_planets[j] = Omega_planets[j] * 0.01745329251

#these values are not as close as they should be either! 
#~ print 'These are Omega values for the planets'
#~ pprint (Omega_planets)



for j in range(8): 
	for i in range(3): 
		
		if i == 0: 
			pi_planets[j] += pi8[j][0]
			
		pi_planets[j] += (pi8[j][i]*(T**i))**i
		
		#~ #convert from degrees to radians 
		#if I don't do it here then I would have to make another for loop to go through each entry! 
		if i == 2: 
			pi_planets[j] = pi_planets[j] * 0.01745329251

print 'These are pi values for the planets' 
pprint( pi_planets)


for i in range(7): 
	pi_planets[i] = pi8[i][0] + pi8[i][1]*T + pi8[i][2]*numpy.power(T,2) + pi8[i][3]*numpy.power(T,3)  
	pi_planets[i] = pi_planets[i] * 0.01745329251

print 'these are different pi values for the planets'
pprint(pi_planets)

# The equation for M is M = L - pi 

for i in range(8): 
	M_planets[i] = L_planets[i] - pi_planets[i]

#this was for testing in a different .py file... 	
m_planets = M_planets	


#~ print'this is M for the planets'	
#~ print M_planets

#M values match the table to .01. So that's pretty decent... Although odd because L was spot on and same with pi. 

#Now, we have to solve for r and theta(nu) using the Kepler equation. 
#first find E-the eccentric anomaly using the newton Raphson method 
#Once we solve for E we can find r and theta (nu). 

# r = a(1 - eccentricity * cos(E) ) 
# tan(theta/2) = sqrt((1+eccentricity) / (1-eccentricity)) * tan(E/2)

E_planets = [0.00] * 8 

for i in range(8): 
	E_planets[i] = Kepler_solve(M_planets[i], e_planets[i]) 

#print 'This is E for the planets'
#print E_planets 


r_planets = [0.00] * 8 

for i in range(8): 
	
	r_planets[i] = a_planets[i] * (1.0 - e_planets[i] * numpy.cos( E_planets[i]) )

#these values are relatively close, but don't inspire complete confidence. 
#Mercury is off by 0.1 but others are pretty darn close...  
#furthermore, the eccentricity values are correct.
#I suppose a good place to check might be the in the E values but they weren't given in the table... 	
#I suppose the newton method could be giving strange behavior and rounding improperly? 

print 'this is r of the planets' 
print r_planets		
	

	

nu_planets = [0.00] * 8

#prototype calculation of theta(nu) from Prof Worthey's newton.py method. 
#~ x2 = sqrt((1.0+e)/(1.0-e))
#~ theta = 2.0*math.atan( x2*tan(Eone/2.0) )
 

for i in range(7): 
	
	temp = numpy.sqrt((1.0 + e_planets[i])/(1.0 - e_planets[i]))
    
	nu_planets[i]=2.0*numpy.arctan(temp * numpy.tan((E_planets[i] / 2.0))) 
	
	#if nu_planets[i] < 0:		
		#nu_planets[i] += 2.0 * numpy.pi 
	
print nu_planets

#for some reason the nu doesn't turn out properly so I just entered the array. 
#nu_planets = [2.725887, 3.746150, 5.915882, 4.250045, 2.28187, 5.000764, 1.915775, 4.881101]	

print 'this is nu of the planets'
print nu_planets

#now we need to find lower case omega 
#w = pi - Omega 

omega_planets = [0.00] * 8 
 
for i in range(8): 
	 omega_planets[i] = pi_planets[i] - Omega_planets[i]



	 
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


for i in range(8): 
	A_planets[i] = numpy.arctan((F_planets[i]/P_planets[i])) 

for i in range(8): 
	B_planets[i] = numpy.arctan((G_planets[i]/Q_planets[i]))
	
for i in range(8): 
	C_planets[i] = numpy.arctan((H_planets[i]/R_planets[i]))
	
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

for i in range(8): 
	X_planets[i] = r_planets[i] * a_const_planets[i] * numpy.sin((A_planets[i] + omega_planets[i] + nu_planets[i]))
	
#~ print 'This is X'
#~ print X_planets	
	
for i in range(8): 
	Y_planets[i] = r_planets[i] * b_const_planets[i] * numpy.sin((B_planets[i] + omega_planets[i] + nu_planets[i]))
	
#~ print 'This is Y'
#~ print Y_planets	
	
for i in range(8):
	Z_planets[i] = r_planets[i]	* c_const_planets[i] * numpy.sin((C_planets[i] + omega_planets[i] + nu_planets[i]))

#~ print 'This is Z'
#~ print Z_planets

	
#now we have to compute the right ascension and declination (alpha and delta) 

#X = -Xearth 

X_earth = -X_planets[2]  	
Y_earth = -Y_planets[2]
Z_earth = -Z_planets[2]


eta_planets = [0.00] * 8 
zeta_planets = [0.00] * 8 
xi_planets = [0.00] * 8 
Delta_planets = [0.00] * 8 

alpha_planets = [0.00] * 8 
delta_planets = [0.00] * 8 


#~ for i in range(7): 
	#~ xi_planets[i] = X_earth + X_planets[i] 
	#~ 
#~ for i in range(7): 
	#~ eta_planets[i] = Y_earth + Y_planets[i]
 #~ 
#~ for i in range(7): 
	#~ zeta_planets[i] = Z_earth + Z_planets[i]
#~ 
#~ for i in range(7): 
	#~ Delta_planets[i] = numpy.sqrt(numpy.power(xi_planets[i],2) + numpy.power(eta_planets[i],2) + numpy.power(zeta_planets[i],2)) 
	#~ 
#~ for i in range(7): 	
	#~ alpha_planets[i] = numpy.arctan( eta_planets[i] / xi_planets[i])
	#~ 
#~ for i in range(7): 
	#~ delta_planets[i] = numpy.arcsin( zeta_planets[i] / Delta_planets[i] ) 	
	#~ 
#~ print alpha_planets	
 
