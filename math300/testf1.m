%this is script is to test the f1(x) function 

clear 
x = -1:1e-5:2; 

tic
result = zeros(1,length(x));

%compiled vs interpretted language
%~ 
%~ for i=1:length(x)
	%~ result(i) = f1(x(i));
%~ end 

%you want to be able to leverage your knowledge of how functions work. 
%Question:whats the difference between a function and a script? 
%Answer:function gets called with arguments a script has not arguments 
%big thing is global and local functions! 
%what happens in the function stays in the function. 

result = f2(x) 
toc

plot(x,result)


