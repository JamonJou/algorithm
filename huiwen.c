

/**
 * 问题描述:
 * 给定一个字符串,寻找它的最大子字符串,该子字符串是回文.
 * 例子: "gabcdcbaef", 最大回文子串: "abcdcba"
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void huiwen(char input[], int len, char output[])
{
    if (len < 0)
    {
        printf("input is null, len = %d\n", len);
        return;
    }
    if (len == 1)
    {
        output[0] = input[0];
        return;
    }
    printf("input = %s, len = %d\n", input, len);
    int start = -1, end = -1;
    int index = 0;
    for (int i = 0; i < len; ++i)
    {
        int j;
        for (j = len - 1; j > i; j--)
        {
            printf("cur compare is input[%d]=[%c] and input[%d]=[%c].\n", i, input[i], j, input[j]);
            if (input[j] == input[i])
            {
                start = i;
                end = j;
                break;
            }
        }
        printf("start = %d, end = %d,[i:j]=[%d:%d]\n", start, end, i, j);

        if (j <= i) // 没有找到对应的,继续查找
        {
        }
        else
        {
            while (start >= 0 && end >= 0 && start < end)
            {
                printf("find a char, then cur compare is input[%d]=[%c] and input[%d]=[%c].\n", start, input[start], end, input[end]);
                if (input[++start] != input[--end])
                {
                    break;
                }
            }
            if (start >= end)
            {
                // find
                printf("start = %d, end = %d,\n", i, j);
                while (i <= j)
                {
                    output[index++] = input[i++];
                }
                return;
            }
        }
    }
}

void huiwen2(char input[], int len, char output[])
{
    int max = 0, left = 0, start = 0;
    for (int i = 0; i < len; ++i)
    {
        for (int t = 0; t <= i; ++t)
        {
            if (i + t > len) // 越界
                break;
            if (input[i + t] != input[i - t])
            {
                break;
            }
            else
            {
                left++;
            }
        }
        // 总回文数: 2*(left-1)
        if (2 * (left - 1) + 1 > max)
        {
            max = 2 * (left - 1);
            start = i - left + 1; //指定起始位置.
        }
        left = 0;
    }
    memcpy(output, input + start, max);
}

void showResult(char input[], char output[])
{
    printf("[%s]'s max sub huiwen str is [%s]\n", input, output);
    printf("\n\n\n");
}

int main()
{
    char input[] = "gabcdcbaefg";
    char input2[] = "a";
    char input3[] = "cbbd";
    char input4[] = "bb";
    char input5[] = "babad";
    char input6[] = "bab";
    // char *output = (char *)calloc(strlen(input), sizeof(char));

    char output[1024] = {0};
    char output2[1024] = {0};
    char output3[1024] = {0};
    char output4[1024] = {0};
    char output5[1024] = {0};
    char output6[1024] = {0};

    huiwen(input, strlen(input), output);
    showResult(input, output);

    huiwen(input2, strlen(input2), output2);
    showResult(input2, output2);

    huiwen(input3, strlen(input3), output3);
    showResult(input3, output3);

    huiwen(input4, strlen(input4), output4);
    showResult(input4, output4);

    huiwen(input5, strlen(input5), output5);
    showResult(input5, output5);

    huiwen(input6, strlen(input6), output6);
    showResult(input6, output6);

    printf("------------------------------------------------------\n");
    huiwen2(input, strlen(input), output);
    showResult(input, output);

    huiwen2(input2, strlen(input2), output2);
    showResult(input2, output2);

    huiwen2(input3, strlen(input3), output3);
    showResult(input3, output3);

    huiwen2(input4, strlen(input4), output4);
    showResult(input4, output4);

    huiwen2(input5, strlen(input5), output5);
    showResult(input5, output5);

    huiwen2(input6, strlen(input6), output6);
    showResult(input6, output6);

    return 0;
}