function f = minor(x)

surname = 'minor'; 

name = double(surname)

%subtract 96 to get a=1 
name = name - 96

name = name -13.0

name = name./6.0

temp = 0:4; 

c = 2.^temp

name = name./c

f = sum(name.*x.^(0:4))

