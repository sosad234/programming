#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void fill(int n, int a[]) 
{
    for (int i = 0; i < n; i++)
    a[i] = rand() % 11 - 5;
}
int findFirst(int n, int a[])
{ 
    for (int i = 0; i < n - 1; i++) 
    {
        for (int j = i + 1; j < n; j++) 
        {
            if (a[i] == a[j])  
            {
                return i;
            }
        }
    }
return -1;
}

int findSecond(int start, int n, int a[]) 
{
    for (int i = start + 1; i < n; i++) 
    {
        if (a[start] == a[i]) 
        {
            return i;
        }
    }
    return -1;
}

void process(int n, int a[], int findFirst, int findSecond) 
{
    int sum = 0;
    int proiz = 1;
    for (int k = findFirst + 1; k < findSecond; k++) 
    {
        sum += a[k];
        proiz *= a[k];
    }
    printf("summ: %d\n", sum);
    printf("proiz: %d\n", proiz); 

    a[findFirst] = sum;
    a[findSecond] = proiz;
}

int main() 
{
    srand(time(NULL));
    int n;
    printf("n -> ");
    scanf("%d", &n);
    int A[n];
    fill(n, A);
    int first = findFirst(n, A);
    int second = findSecond(first, n, A);
    printf("firstIndex: %d\n", first);
    printf("secondIndex: %d\n", second);
    int number = A[first];
    printf("number %d\n", number);
    printf("Original\n");
    for (int i = 0; i < n; i++)
    printf("%5d", A[i]);
    printf("\n");

    process(n, A, first, second);

    printf("Ne original\n");
    for (int i = 0; i < n; i++)
    printf("%5d", A[i]);
    printf("\n");

    return 0;
}