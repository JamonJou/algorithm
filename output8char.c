
/**
 *  连续输入字符串，请按长度为8拆分每个字符串后输出到新的字符串数组；
    长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void output8C(char a[], int len)
{
    int i = 0;
    while (i < len)
    {
        printf("%c", a[i++]);
        if ((i % 8) == 0)
            printf("\n");
    }
    int left = 8 - i % 8;
    if ((len % 8) != 0)
    {
        for (i = 0; i < left; ++i)
            printf("0");
        printf("\n");
    }
}

int main()
{
    char source[100];
    gets(source);
    output8C(source, strlen(source));
    gets(source);
    output8C(source, strlen(source));
}