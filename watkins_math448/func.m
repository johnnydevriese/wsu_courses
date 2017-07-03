% euler.m calls fun.m to find out which DE it's solving.
function val = func(t,y)
    val = 99.0*exp(-t) - 100.0*y; 


    