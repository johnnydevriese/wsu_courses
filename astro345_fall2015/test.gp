# test.gp

reset

set term pdf 

set output 'output.pdf'


set title "Classical Mechanics-Problem 2.20" 
set xlabel "x(position)"
set ylabel "y(height)" 
set xrange[0.0 : 3.0]
set yrange[-5 : 2.0]


#set samples will increase the density of points in the plot. This is helpful when you have an asymptote
set samples 100000

set xzeroaxis


#Terminal velocity of 0.3 (EQ. 2.37)
h(x) = (1.3 * x) + (0.3 * 0.3) * log(1.0 - (x/0.3)) 

#Terminal Velocity of 1.0 
y(x) = (2.0*x) + 1.0 * log(1.0-x)

#Terminal velocity of 3.0
p(x) = (4.0 * x) + (3.0*3.0) * log(1.0-(x/3.0))


#Terminal velocity of infinity 

#a(x) = (11.0 * x) + 10.0 * 10.0 * log(1.0 - (x/10.0) ) 

a(x) = (6.0 * x) + 5.0 * 5.0 * log(1.0 - (x / 5.0) ) 


plot h(x) title "v-ter=0.3", y(x) title "v-ter=1.0", p(x) title "v-ter=3.0", a(x) title "v-ter=infinity"


pause -1 
	
