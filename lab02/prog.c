#include <stdio.h>
#include <math.h> 
#include <unistd.h>

int main()
{
    
    double x,h,res;
    x = 0.0;
    scanf("%lf", &h);
    int z;
    int k;
    k = 0;
    z = 3 / h + 1; 
    
    while(z > k)
    {
        if (x >= 0 && x <= 1.5)
            res =  pow(2,x) - 2 + pow(x, 2);
        if (x > 1.5 && x <= 3)
            res = sqrt(x) * exp(-x * x);
        printf("%lf %lf\n", x, res);
        x += h;
        k++;
    }
    return 0;
}