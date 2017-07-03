# bsc.py
# reads in and plots the Bright Star Catalog 5th Edition in R.A. and dec,
# Epoch 2000 coordinates.  9096 stars to magnitude 7.5 ish.
# coded up by GW
import matplotlib.pyplot as plot
import numpy as np
import math
from pylab import *
import re     # "regular expressions"
from planetary_orbit_nov1 import * 

# set plot limits here (whole sky would be 0,365, -90,90)
x_low = 370
x_hi  = -5
y_low = -91
y_hi = 91

# read from the file
hr,rah,ram,ras,dd,dm,ds,v = loadtxt('bsc5.trim',unpack=True, usecols=[0,1,2,3,4,5,6,8])

# convert sexagesimal R.A. and dec to decimal degrees
ra = 15.0*(rah + ram/60.0 + ras/3600.)
sign = range(len(dd))
regex = re.compile('-')
for d1 in range(len(dd)):
    sign[d1] = 1
    foo = str(dd[d1])  #subtlety: only the degrees column has a negative
                       # sign, but the neg needs to apply to min and sec too
    if (regex.match(foo)):   # --> hence, this wierd regex workaround,
        sign[d1] = -1        # since -0 is different in meaning than 0
dec = abs(dd) + dm/60.0 + ds/3600.0
dec = dec*sign


# note to user: uncomment the 'plot' line and comment the 'scatter' line, if
# desired.
#plot(ra,dec,'ro',color='r',ms=0.5)    # uniform marker size



#******************* beginning of my code *********************** 

#surprisingly regular polynomial doesn't fit the data very well at all.
#~ coefficients = np.polyfit(ra, dec, 15)
#~ polynomial = np.poly1d(coefficients)
x = arange(0.0, 360, 0.1)
#~ ys = polynomial(x)
#print coefficients
#print polynomial

#arange is (start, stop, step) 


#try to get some extra credit points for this stuff! 
def f(x): 
	
	f = 65.0*cos((1.0/57.2958) * x) 
	
	return f 

y = f(x) 

plot(x, y)

colors = ['g', 'b','c','m', 'y', 'Aqua', 'Crimson', 'ForestGreen','Chartreuse' ]


mercury = scatter(alpha_hours[0], degrees_delta_planets[0], c=colors[0], s=100) 
venus = scatter(alpha_hours[1], degrees_delta_planets[1], c=colors[1], s=100)
earth = scatter(alpha_hours[2], degrees_delta_planets[2], c=colors[2], s=100)
mars = scatter(alpha_hours[3], degrees_delta_planets[3], c=colors[3], s=100)
jupiter = scatter(alpha_hours[4], degrees_delta_planets[4], c=colors[4], s=100)
saturn = scatter(alpha_hours[5], degrees_delta_planets[5], c=colors[5], s=100)
uranus = scatter(alpha_hours[6], degrees_delta_planets[6], c=colors[6], s=100)
neptune = scatter(alpha_hours[7], degrees_delta_planets[7], c=colors[7], s=100)
sun = scatter(alpha_hours[8], degrees_delta_planets[8], c=colors[8], s=100)


legend((mercury, venus, earth, mars, jupiter, saturn, uranus, neptune,sun), ('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune','Sun'), 
scatterpoints=1, loc='lower left', ncol=3, fontsize=8)


#*********************** end of my code *********************** 

# fancy, nonlinear marker size trick
ssize = (100.0 - 14.0*v)*(100.0-14.0*v)/100.0
scatter(ra,dec,c='r',marker='s',s=ssize)    #variable marker size
xlim(x_low,x_hi)
ylim(y_low, y_hi)
xlabel('Right Ascension (degrees)')
ylabel('Declination (degrees)')
title('JDE = {}' .format(JDE)) 

legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# the next line is crucial
show()


