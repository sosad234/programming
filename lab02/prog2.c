#include <stdio.h>
#include <math.h>

int main()
{
   double x = 0.0, y;
   double eps;
   double h;
   scanf("%lf", &h);
   eps = h / 2.0;
   printf("x\t\ty\n");
   for(x = 0.0; x <= 3.0 + eps; x = x + h)
   {
       if(x <= 1.5 + eps)
         y = pow(2.0, x) - 2.0 + pow(x, 2);
       else
         y = sqrt(x) * exp(-pow(x, 2));
       printf("%f\t%f\n", x, y);
   }
   return 0;
}