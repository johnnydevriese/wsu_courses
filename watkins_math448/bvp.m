% Quick-and-dirty code to solve a linear BVP
% Number of subintervals n must be prespecified by user.
n = 40;
h = 1/n; % subinterval length
k = 4; m = 2;
% Build the coefficient matrix.  
d  = (2 + (k*h)^2)*ones(n-1,1);
sd = -ones(n-2,1);
A = diag(d) + diag(sd,-1) + diag(sd,1);
% Because the problem is small, I am not bothering to store the 
% matrix in sparse format.
b = zeros(n-1,1);
b(n-1) = m; % boundary condition at 1.
b(1) = 0; % boundary condition at 0.
u = A\b;
x = (0:h:1)'; % prime symbol transposes the matrix
uu = [ 0; u; m];
ts = m*sinh(k*x)/sinh(k); % True solution
format short e
maxerr = norm(uu-ts,'inf')
% Plot true and approximate solutions just for fun.
xfine = (0:.005:1)';
tsf = m*sinh(k*xfine)/sinh(k);
plot(xfine,tsf,'k-',x,uu,'r+') 
