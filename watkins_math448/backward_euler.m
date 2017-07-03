a = 0; b = 1; 
init_val = 1;
h = 1/10;
t = a:h:b;
last = size(t,2);
y = zeros(size(t));
y(1) = init_val;

for k = 1:last-1
 y(k+1) = (y(k) + h*99.0*exp(-t(k+1))) / (1.0 + 100.0*h);
end
true_sol = exp(-t);
numerical_solution = y
true_solution = true_sol
max_error = norm(y-true_sol,'inf')
% Plot true solution and approximation
t_fine = a:h/10:b;
sol_fine = exp(-t_fine);
plot(t_fine,sol_fine,'b-',t,y,'r+')
