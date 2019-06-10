/**
 * 题目描述

写出一个程序，接受一个由字母和数字组成的字符串，和一个字符，然后输出输入字符串中含有该字符的个数。不区分大小写。
输入描述:

输入一个有字母和数字以及空格组成的字符串，和一个字符。

输出描述:

输出输入字符串中含有该字符的个数。

示例1
输入


ABCDEF A

输出


1
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int isBig(char big)
{
    int flag = 0;
    if (big >= 'A' && big <= 'Z')
    {
        flag = 32;
    }
    else if (big >= 'a' && big <= 'z')
        flag = -32;
    return flag;
}

int countA(char *source, char dest, int flag)
{
    int cnt = 0;
    if (source == NULL)
    {
        return cnt;
    }

    int s_len = strlen(source), i = 0;
    for (; i < s_len; ++i)
    {
        if (source[i] == dest | source[i] == (dest + flag))
        {
            cnt++;
        }
    }

    return cnt;
}

int main()
{
    char source[5000];
    char dest;
    int cnt = 0;
    int flag;
    gets(source);
    scanf("%c\n", &dest);
    cnt = countA(source, dest, isBig(dest));
    printf("%d\n", cnt);

    return 0;
}