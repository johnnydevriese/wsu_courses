#done on 12.15.15 an interesting way to make a 21 x 2 matrix. 

from numpy import * 
#~ 
#~ a = 2 * ones(21) 
#~ 
#~ b = arange(1,19 + 1, 2) 
#~ 
#~ c = zeros(21) 
#~ 
#~ for i in arange(len(b)): 
	#~ c[i] = b[i]
#~ 
#~ z = append(a,c).reshape(2,21) 
#~ 
#~ z = transpose(z) 
#~ 
#~ print z 


#perhaps a more traditional method using slices. 

a = zeros((21, 2)) 

a[:,0] =  2 

b = arange(1,19+1,2) 

for i in arange(len(b)): 
	a[i,1] = b[i] 

print a 
