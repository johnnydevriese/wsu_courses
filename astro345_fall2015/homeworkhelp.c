#include<stdio.h>
#include<stdlib.h> //malloc

void modInt(int *num);

void function(char arraystr[100][50]); 

int main(void)
{
	//immutable memory
	char *ptr = "string";
	//mutable memory 	
	char ptr[] = "string"; 

	// you can increment the pointer and get to the next spot. 

	//* is the dereference operator. i.e. indirection operator 

	//follow pointer/address to place in memory and access contents of memory. 

	//& is the address of operator 
	
	//******* create a function that modifies an integer and retains the result without using the result value. 
	
	//-> operator can only be used with a pointer to a struct. 

	//when you have a pointer struct. 
	(*pstudent).id = 1234; 
	//is equivalent to
	pstduent->id = 1234;

	int *num = 0; 
	modInt(&num);   

	//*****How to pass a 2d array to a function 
	//2nd dimension has to be explicit. 
	
	char arrayStrings[100][50];

	//some function
	function(arrayString); 
 

	return 0; 
}

void modInt(int *num);
{
	int newint = 0; 
	scanf("%d", &newint); 
	*num = newint; 


	return; 
}
