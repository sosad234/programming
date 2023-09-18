#include <stdio.h>
#include <math.h>

int main()
{
    int a, b, x;
    printf("Enter a -> ");
    scanf("%d", &a);
    printf("Enter b -> ");
    scanf("%d", &b);
    printf("Enter x -> ");
    scanf("%d", &x);

    if((a + b) < x)    
    {
        if (x == 0)
            printf("znamenatel' raven 0\n");
        else  
            printf("%.3f\n", (float)(a + b)/ x);  
    }
    if((a + b) > x) 
    {
        if(a + b == 0)
            printf("znamenatel' raven 0\n");
        else  
            printf("%.3f\n", (float)x / (a + b));
    }
    if ((a + b) == x)
    {
        if (x == 0)
            printf("znamenatel' raven 0\n");
        else  
            printf("%.3f\n", (float)b / x);
    }
    return 0;
}

