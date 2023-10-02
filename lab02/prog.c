#include <stdio.h>
#include <math.h> 


int main()
{
    double x,s,res;
    x = 0.0;
    
    scanf("%lf",&s);    
    while(x <= 3)
    {
        if (x >= 0 && x <= 1.5)
        res =  pow(2,x) - 2 + x*x;
        if(x <= 1.5 && x <= 3)
        res = sqrt(x) * exp(pow(-x, 2));
        printf(" %lf %lf/n", x, res);
    }
}