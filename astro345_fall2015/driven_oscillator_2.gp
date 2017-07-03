# driven_oscillator.gp

reset

set term pdf 

set output 'oscillator.pdf'


set title "Classical Mechanics-Driven Oscillation Problem #2" 
set xlabel "t(time)"
set ylabel "x(position)" 
set xrange[0.0 : 6.0 * pi]
set yrange[-20.0 : 20.0]


#set samples will increase the density of points in the plot. This is helpful when you have an asymptote
set samples 100000

set xzeroaxis


#position function solution 
y(x) = cos(x - pi/2) + x * sin(x) 


plot y(x) title "x(t)=cos(t - pi/2)+t*sin(t)"



pause -1 
	
