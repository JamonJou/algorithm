#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void test_student(int *arr, int n)
{
    int t[1001] = {0};
    int i;
    for (i = 0; i < n; ++i)
    {
        t[arr[i]] = 1;
    }
    for (i = 0; i < 1001; ++i)
    {
        if (t[i] == 1)
        {
            printf("%d\n", i);
        }
    }
}

int main()
{
    int i, n;
    while (~scanf("%d", &n) && n > 0)
    {
        int *a = malloc(n * sizeof(int));
        for (i = 0; i < n; ++i)
        {
            scanf("%d", &a[i]);
        }
        test_student(a, n);
        free(a);
    }

    return 0;
}