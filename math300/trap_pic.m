function integral = trap_pic(func, a, b, sub_interval)
%this function will take a single variable function, the beginning of the interval(a), the end of the interval(b)
and the number of sub intervals   


%could make inteval by going 
%start:end:step? 
%would need to plot this vector as the points of trapezoid. 
%in matlab it is called the colon operator. 

x = a:((b - a)/sub_interval):b

y = func(x) 


Q = trapz(y) 

%now we need to plot this stuff! 

x_function = linspace(a,b); 
%this should hopefully plot the trapezoidal points. 
plot(x,y,'--rd')
hold on 

output = f(x_function); 

plot(x_function, output, '-b');  

%we can modify the appearance of the plot from 
grid on 
xlabel('x')
ylabel('f(x)')
title('Line segments used in trapezoidal rule on "sub_interval" subintervals')
legend('Trapz segment', 'f(x)')

hold off



end 
