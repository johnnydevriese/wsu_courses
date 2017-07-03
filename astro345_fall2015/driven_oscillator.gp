# driven_oscillator.gp

reset

set term pdf 

set output 'output.pdf'


set title "Classical Mechanics-Driven Oscillation Problem" 
set xlabel "t(time)"
set ylabel "x(position)" 
set xrange[0.0 : 2.0 * pi]
set yrange[-20.0 : 20.0]


#set samples will increase the density of points in the plot. This is helpful when you have an asymptote
set samples 100000

set xzeroaxis


#position function solution 
y(x) = 4.0*sin(x)*sin(5.0*x) 

#enevelope functions 
h(x) = 4.0*sin(x) 
f(x) = -4.0*sin(x) 

plot y(x) title "x(t)=4.0*sin(t)*sin(5.0*t)", h(x) title "x(t)=4.0*sin(t)", f(x) title "x(t)=-4.0*sin(t)" 



pause -1 
	
