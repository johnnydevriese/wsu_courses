% How to make a loop and exit when the 
% stopping criterion is satisfied.

a = 2;  % or your favorite positive number
u = a;
duu = zeros(3,1); % storage space
for iteration = 1:100
  % code arranged for readable syntax, not efficiency
  du = -(u^2-a)/(2*u);
  duu(iteration) = du; % saved to be displayed later
  u = u + du;
  if abs(du) < 10^(-15) 
    break % exit loop if correction is small enough
  end
end
format long
disp('And the answer is: '),disp(' '),disp(u)
disp('By the way, what does this code do?')
format short e
corrections = duu
disp('Do you see evidence of quadratic convergence?'), disp(' ')
disp('Now onto something else ...')

% How to make your starting vector for Newton's method
n = 4; h = 1/n;
xf = h; xl = 1-h;
xx = (xf:h:xl)'
format % Returns to default 'short' format.
uu = 2*xx

% How to raise all entries of an array to the same power and make a diagonal matrix

disp('... and check this out:')

p = 1.5;
D = diag(p*uu.^(p-1))
