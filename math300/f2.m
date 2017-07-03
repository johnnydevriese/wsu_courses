function [extra_credit] = f2(x) 

%multiplication because && and + becomes an ||
extra_credit = (x>=0).*(x<1).*sqrt(x)+(x>=1);  


end 
