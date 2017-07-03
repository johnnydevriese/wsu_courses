#include <cstdlib>
#include <iostream>
#include <math.h>
#include <stdio.h> 
#include <iomanip> 

using namespace std;

double f(double x) //for the function f(x)
{
	double y = 0.0; 
	
	y = 2.0 * x + log(1.0 - x); 
	
	return y ;	
}

double ff(double x) //Differentiating function f(x)
{
	double y = 0.0;  
    
    y = 2.0 + (1.0 / (1.0 - x) ) * (-1.0)  ; 
    
    
    return y ; 
}

void NR(double aerr, int maxitr, double a)
{
     int i = 0;
     double b = 0.0, prev = 0.0;
     while (i <= maxitr)
     {
           b = a - (f(a))/ff(a);
           
           cout << "Iter " << i << ": x = " << setprecision(16) << b << endl;
           
           //cout << setprecision(16) << b << "\n";
            
           
           i++;
           
           if (fabs(b - a) < aerr)
              break;
           a = b;
     }
    
}

int main()
{
    double aerr = 0.0, a = 0.0, b = 0.0;
    int maxitr = 0;
    cout << "Enter absolute error, maximum iterations before exit, and your initial guess." << endl;
    cin >> aerr;
    cin >> maxitr;
    cin >> a;
    NR(aerr, maxitr, a);
    
    system("PAUSE");
    return EXIT_SUCCESS;
}
