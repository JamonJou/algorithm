

/**
 * 实现高精度的十进制加法 
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void displayIntArrary(int *arr, int len)
{
    if (len < 0)
        return;
    printf("\n");
    for (int i = 0; i < len; ++i)
    {
        printf("%d", arr[i]);
    }
    printf("\n");
}

void addLong(const char *num1, const char *num2, char *result)
{
    int len1 = strlen(num1);
    int len2 = strlen(num2);

    printf("len1 = %d, len2 =%d\n", len1, len2);

    int *n1 = (int *)malloc((len1) * sizeof(int));
    int *n2 = (int *)malloc((len2) * sizeof(int));
    memset(n1, 0, (len1) * sizeof(int));
    memset(n2, 0, (len2) * sizeof(int));

    int reslen = len1 > len2 ? len1 : len2;
    int *res = (int *)malloc((reslen + 1) * sizeof(int));
    memset(res, 0, (reslen + 1) * sizeof(int));

    if (n1 == NULL || n2 == NULL || res == NULL)
    {
        printf("malloc failed.\n");
        return;
    }
    int positive_1, positive_2; // 指定符号

    // 将两个字符数组转换为int数组, 反向存储
    int i, flag;
    if (*num1 == '-')
    {
        flag = 1;
        positive_1 = -1;
    }
    else
    {
        positive_1 = 1;
        flag = 0;
    }
    for (i = len1 - 1; i >= flag; i--)
    {
        n1[i] = num1[i] - '0';
    }

    if (*num2 == '-')
    {
        flag = 1;
        positive_2 = -1;
    }
    else
    {
        flag = 0;
        positive_2 = 1;
    }
    for (i = len2 - 1; i >= flag; i--)
    {
        n2[i] = num2[i] - '0';
    }
    printf("positive_1 = %d, positive_2 = %d\n", positive_1, positive_2);
    displayIntArrary(n1, len1);
    displayIntArrary(n2, len2);

    // 同号情况下
    if (positive_1 == positive_2)
    {
        for (i = 0; i < reslen + 1; ++i)
        {
            res[i] = n1[i] + n2[i];
            res[i + 1] += res[i] / 10;
            res[i] = res[i] % 10;
        }
        displayIntArrary(res, reslen);

        i = 0;
        if (positive_1 == -1)
        {
            result[i++] = '-';
        }

        for (; i < reslen + 1; ++i)
        {
            result[i] = '0' + res[reslen - 1 - i];
            // sprintf(result[i], "%d", res[reslen - 1 - i]);
        }
    }

    // result = res;
}

void showResult(char output[])
{
    printf("output[%s]\n", output);
    printf("\n\n\n");
}

int main()
{
    char n1[20] = "9876543210";
    char n2[20] = "1234567890";
    char result[100] = {'\0'};
    addLong(n1, n2, result);
    showResult(result);

    return 0;
}