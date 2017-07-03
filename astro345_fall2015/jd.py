# jd.py
import math
# given a date, convert to julian day
# input variables m, d, y for month, day, and year
# input variable  utc for Universal time 
y = input("Enter year ")
m = input("Enter month ")
d = input("Enter day ")
utc = input("Enter decimal hour time of day ")
# At this point, a REAL programmer would put in error checks to see if the
#   user entered sensible data. We are not real programmers.

# a few other inputs regarding (tiny) corrections
s = 4
tai_utc = 30.00
ut1_utc = 0.00
# this is 2*pi, not pi squared 
#pi2 = 6.2831853072
pi2 = math.pi*2.0

if (m == 1) | (m == 2):
    y = y - 1
    m = m + 12

datnum = y + 0.01*m + 0.0001*d

if datnum >= 1582.1015:
    a = int(0.01 * y)
    b = 2 - a + int(0.24*a)
else:
    a = 0
    b = 0

if y < 0:
    term1 = int(365.25*y - 0.75)
else:
    term1 = int(365.25*y)

jed = term1 + int(30.6001*(m+1.0)) + d + utc/24.0 + 1720994.5 + b

print 'Raw JD is ',jed

# the program could stop here for our purposes, but in the interests of
# completeness, we add the corrections

if s == 1:                              # UT1
    corr = ut1_utc/86400.0
elif s == 2:                            # UT2
    corr = ut1_utc/86400.0
    jed = jed + corr
    t = 2000.0 + (jed - 2451544.5333981)/365.242198781
    corr = (0.022*math.sin(pi2*t) -0.012*math.cos(pi2*t) 
         -0.006*math.sin(2.0*pi2*t) +0.007*math.cos(2.0*pi2*t))
    corr = corr/86400.0
elif s == 3:
    corr = (tai_utc + 32.184)/86400.0
elif s == 4:
    corr = (tai_utc + 32.184)/86400.0
    jed = jed + corr
    t = (jed - 2451545.0 )/36525.0 
    r2d = 57.2957795131
    corr = (1656.675   * math.sin((35999.3729*t + 357.5287)/r2d)
             +22.418   * math.sin((32964.467 *t + 246.199 )/r2d)
             +13.840   * math.sin((71998.746 *t + 355.057 )/r2d)
             + 4.770   * math.sin(( 3034.906 *t +  25.463 )/r2d)
             + 4.677   * math.sin((34777.259 *t + 230.394 )/r2d)
             +10.216*t * math.sin((35999.373 *t + 243.451 )/r2d)
             + 0.171*t * math.sin((71998.746 *t + 240.98  )/r2d)
             + 0.027*t * math.sin(( 1222.114 *t + 194.661 )/r2d)
             + 0.027*t * math.sin(( 3034.906 *t + 336.061 )/r2d)
             + 0.026*t * math.sin((  -20.186 *t +   9.382 )/r2d)
             + 0.007*t * math.sin((29929.562 *t + 264.911 )/r2d)
             + 0.006*t * math.sin((  150.678 *t +  59.775 )/r2d)
             + 0.005*t * math.sin(( 9037.513 *t + 256.025 )/r2d)
             + 0.043*t * math.sin((35999.373 *t + 151.121 )/r2d) )
    corr = corr * 0.000001
    corr = corr / 86400.0
elif s == 5:
    corr = 0.0
else:
    print 'that choice of s parameter is not supported'

jed = jed + corr
print 'Corrected JD is ',jed

jed = jed - 2400000.5
print 'Modified JD is ',jed

# END

