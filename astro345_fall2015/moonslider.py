# How I could have gotten extra credit
# or
# An annotated matplotlib example, including interactive graphical sliders,
# to discover the age of a rock sample returned from the lunar maria.
# import some things
from pylab import *
from matplotlib.widgets import Slider
#import math   <--- I didn't need "math" as the exp function worked anyway

# the lunar rock data
Rb = [0.00982, 0.00159, 0.0252, 0.0197, 0.0501, 0.0629, 0.0844]
Sr = [0.69962, 0.69919, 0.70060, 0.70011, 0.70173, 0.70236, 0.70362]
Serr = [0.00012,0.00006, 0.00011,0.00006, 0.00008, 0.00005, 0.00005]

#ax = subplot(111)    <-- uncommenting this does nothing. This is a default subplot.func_closure
subplots_adjust(bottom=0.27)  # make room for a pair of sliders
a0 = 0.6988   # initial (wrong) guess for initial isotope ratio
f0 = 1        # initial guessed age in Gyr
endline = 0.1 # isochron line gets drawn from zero to this number

axis([-0.008, 0.105, 0.6986, 0.705])  # I fussed with these params a lot
linex = [0.0, endline]                            # x values of isochron
liney = [a0,a0 + endline*(exp(f0*1.42e-2)-1.0)]   # y values of isochron
L, = plot(linex,liney, lw=2, color='red')  # plot the isochron line
errorbar(Rb,Sr,yerr=Serr,fmt='ko',ms=3)# plot the isotope ratio value and error
                                    # bars. This call comes last so that
                                    # the points are drawn on top of the
                                    # red isochron line.
xlabel('$^{87}$Rb/$^{86}$Sr')       # TeX math mode works for labels!
ylabel('$^{87}$Sr/$^{86}$Sr')
title('Apollo 11 Rock 44 Rb-Sr data')

# to draw the actual sliders on the screen:
axcolor = 'lightgoldenrodyellow'
ageslid = axes([0.15, 0.1, 0.65, 0.03], axisbg=axcolor)  # name and position
initslid  = axes([0.15, 0.15, 0.65, 0.03], axisbg=axcolor) # the sliders
# set the limits of slider values and specify more sig figs for the display
sage = Slider(ageslid, 'Age (Gyr)', 0.0, 6.0, valinit=f0, valfmt='%1.5f',facecolor='olive')
sinit = Slider(initslid, 'Initial Sr', 0.698, 0.700, valinit=a0, valfmt='%1.5f',facecolor='burlywood')

# define an updater function
def update(val):
    newinit = sinit.val    # get new values from slider(s)
    newage = sage.val
    liney = [newinit,newinit+endline*(exp(newage*1.42e-2)-1.0)]
    L.set_ydata(liney)     # update the Y data for the drawn line
    sum = 0.0
    for i in range(6):
        sum = sum + ((Sr[i] - (newinit + (exp(newage*1.42e-2) - 1.0)*Rb[i]))/Serr[i])**2
    sum = sqrt(sum/6.0)
    print 'RMS of fit = ',sum
    draw()
    
sage.on_changed(update)
sinit.on_changed(update)

show()
