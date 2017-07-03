from snippet import * 
from Kepler_solver import * 
import math
from planetary_orbit import * 


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
diff_planets = [0.00] * 8 


#just testing the accuracy of my double for loop method and this most explicit version. 

for i in range(8): 
	L_planets[i] = L8[i][0] + L8[i][1]*(T) + L8[i][2] * (T)**2.0 + L8[i][3] * (T)**3.0 
	L_planets[i] = L_planets[i] * 0.01745329251


for i in range(8): 
	pi_planets[i] = pi8[i][0] + pi8[i][1]*T + pi8[i][2]*(T)**2.0 + pi8[i][3] * (T)**3.0  
	pi_planets[i] = pi_planets[i] * 0.01745329251


for i in range(8): 
	M_planets[i] = L_planets[i] - pi_planets[i]


print'this is M for the planets'	
print M_planets

print 'this is m for the planets' 
print m_planets

for i in range(8): 
	diff_planets[i] = m_planets[i] - M_planets[i]
	
	
print 'this is difference:' 
print diff_planets 
