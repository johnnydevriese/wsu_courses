#  newton.py --- given M, e and a, 
#  output r and theta for an elliptical orbit at an arbitrary time

# just blindly import all this, ok?
import math
import matplotlib.pyplot as plot
import numpy as np
from pylab import *
import re # regular expressions

# some constants:
G = 6.674e-11        # m^3 kg^-1 s^-2
Msun = 1.989e30      # kg
mu = 1.32712440018e20 # m^3 s^-2  <-- more accurate than G or M separately
AU = 1.49597871e11   # m
secyr = 3.15569e7    #seconds per year
degrad = 57.2957795  # degrees per radian

def newton(M,e,aAU):     # function definition. Note colon. Note 3 "arguments".
    # use Newton's iteration to solve for theta and r
    Ezero = M            # first guess (inscribed angle E and M are in radians)
    for k in range(25):  # just looping 25 times is a shortcut; not good enough for NASA
        Eone = M + e*sin(Ezero) # new guess 
        Ezero = Eone     # copy new guess over, then rinse and repeat
    # after iterating to the solution, calculate r and theta
    r = aAU*(1.0 - e*cos(Eone))
    x2 = sqrt((1.0+e)/(1.0-e))
    theta = 2.0*math.atan( x2*tan(Eone/2.0) )
    #           get to correct quadrant 
    theta = theta + 2*math.pi if (theta <= 0.0) else theta
    return r,theta       # the return statement concludes the function definition

# statement of the problem:
aAU = 1.1   # A.U.
e = 0.2     # dimensionless
timeyr = (0.0, 0.2, 0.4, 0.6, 0.8)  # yr

# main code:
print '# time  Mean_anomaly   r_vector(AU)   theta(radians)  theta(degrees)'
a = aAU*AU                       # change to mks units
for ii in range(len(timeyr)):    # loop over Prof. Worthey's requested times
    time = timeyr[ii]*secyr      # t-T in seconds
    #M = time*sqrt((G*Msun)/a**3) # mean anomaly in radians
    M = time*sqrt(mu/a**3)         # mean anomaly in radians (more accurate)
    r,theta = newton(M,e,aAU)    # workhorse function
    thetadeg = theta*degrad      # I'm a human. I just relate to degrees better than radians.
    print ii,timeyr[ii],M,r,theta,thetadeg

print 'done.'    # for some reason, I like to restate the obvious.
if e > 0.8: print 'Warning: the orbit is very elliptical and we may not have convered very well.'

# upon a bit of reading, and it's obvious upon reflection, but the product mu = G*M_sun 
# is more accurately known than either G or M_sun separately.
# mu = 1.32712440018e11  km^3 s^-2   x(1000 m/km)^3 = 1.32712440018e20 m^3 s^-2 
# I think I'll use that number!
