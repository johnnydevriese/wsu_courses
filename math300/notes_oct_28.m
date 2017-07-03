%Strings and plots 

hello = ['h','e','l','l','o']

%matlab puts it together as a string even though you have put it all alone. 

%Note that catlab has only one quation character or apostrophe. 

%this is the usual way of making a character string 
world = 'world' 

%the third element in world array 
world(3) 

hi = [hello ', ' world] 

% We can format character strings using sprintf
% '%g' is generic 
% 4.2 means 0000.00 four in front two in back 

myrand = sprintf('Right Now my random number is: %4.2e', rand())

myrand = sprintf('Right Now my random number is: %f', rand())

%**** now to do the function from homework 7 
%this would need to be in it's own .m file, but we'll just stick it right here... 
function [poly_value] = name_poly(name, x)
%poly_name(name, x)
%	This evaluates the polynomial from the variable name, on the points in the variable x

n_characters = length(name); 

coeffs = ((name - 96) - 13)/6) ./ 2.^(0:n_characters - 1);

x_vec = x.^(0:n_characters-1); 

poly_value = coeffs*x_vec(:); 

end 


%Now we plot a polynomial corresponding to a name 



x = -2:0.01:2; 
plot(x,sin(x),'g:o', x, ))
plot(x,sin(x),x,cos(x))

%the x-y vector pairs are called data series 

%if you don't know what the hell is going on you can do: 'help plot' 

%we can modify the appearance of the plot from 
xlabel('x')
ylabel('p(x)')
title('The "name" polynomial') 
legend('sin(x)', 'name polynomial')




