#include <stdio.h>
#include <math.h>


void sums(int n)
{
    int exponent = n - 1;
    int sum[n];
    int tmp;
    int total = (1 << exponent) - 1;

    for (int i = 0; i < total; i++)
    {
        for (int i = 0; i < n; i++)
            sum[i] = 0;

        tmp = 1;
        for (int j = 0; j < exponent; j++)
        {
            if (!(i & (1 << j)))
            {
                sum[n - j - 1] = tmp;
                tmp = 1;
            }
            else
                tmp += 1;

        }
        sum[0] = tmp;

        int num;
        for (int i = 0; i < n; i++)
        {
            num = sum[i];
            if (num != 0)
                printf("%d ", num);
        }
        printf("\n");
    }
    printf("Total: %d", total);
}

int main()
{
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    sums(n);

    return 0;
}