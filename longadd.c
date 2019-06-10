

/**
 * 实现高精度的十进制加法 
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * return :
 *      0: =0;
 *      1: >0;正数
 *     -1: <0;负数
 */
int symbol(const char *n1, const char *n2, int *flag)
{
    int positive = 0;
    int len1 = strlen(n1);
    int len2 = strlen(n2);

    // 同号情况下
    if (*n1 == '-' && *n2 == '-')
    {
        positive = -1;
        *flag = 1;
    }
    else if (*n1 != '-' && *n2 != '-')
    {
        positive = 1;
        *flag = 1;
    }
    // 不同号情况下
    else if (*n1 == '-' && *n2 != '-')
    {
        *flag = -1;
        if (len1 > len2) // 负值长
        {
            positive = -1;
        }
        else if (len1 < len2) // 正值长
        {
            positive = 1;
        }
        else if (len1 == len2)
        {
            char *f1 = n1 + 1;
            char *f2 = n2;
            while (*f1 == *f2)
            {
                f1++;
                f2++;
            }
            if (f1 == '\0' && f2 == '\0')
            {
                positive = 0;
            }
            else
            {
                positive = *f1 < *f2 ? 1 : -1;
            }
        }
    }
    else if (*n1 != '-' && *n2 == '-')
    {
        if (len1 > len2) // 正值长
        {
            positive = 1;
        }
        else if (len1 < len2) // 负值长
        {
            positive = -1;
        }
        else if (len1 == len2)
        {
            char *f1 = n1;
            char *f2 = n2 + 1;
            while (*f1 == *f2)
            {
                f1++;
                f2++;
            }
            if (f1 == '\0' && f2 == '\0')
            {
                positive = 0;
            }
            else
            {
                positive = *f1 > *f2 ? 1 : -1;
            }
        }
    }
    return positive;
}

/**
 * return:
 *      < 0;
 *      > 9;
 *      [0-9];
 */
int add(char a, char b, int flag)
{
    int res;
    if (flag == 1)
    {
        res = atoi(a) + atoi(b);
    }
    else
    {
        res = atoi(a) - atoi(b);
    }
    return res;
}

void addLong(const char *num1, const char *num2, char *result)
{
    // 先确定符号
    int index;
    int positive = symbol(num1, num2);
    if (positive == 0)
    {
        result[0] = '0';
        result[1] = '\0';
        return;
    }
    if (positive == 1)
    {
        index = 0;
    }
    else
    {
        result[0] = '-';
        index = 1;
    }

    // tail
    int t1 = strlen(num1) - 1;
    int t2 = strlen(num2) - 1;
    char *p1 = num1 + t1;
    char *p2 = num2 + t2;
}