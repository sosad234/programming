#include <stdio.h>
#include <math.h> 


int main()
{
    
    double x,h,res;
    x = 0.0;
    int z; 
    scanf("%lf", &h);
    z = 3 / h + 1;  
    while(z)
    {
        if (x >= 0 && x <= 1.5)
            res =  pow(2,x) - 2 + x*x;
        if(x > 1.5 && x <= 3.0)
            res = sqrt(x) * exp(-x * x);
        printf(" %lf %lf\n", x, res);
        x += h;
        z = z - 1;
    }
}
