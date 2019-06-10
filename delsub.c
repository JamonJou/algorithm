
/**
 * 问题描述:
 * 给定一个字符串,查找所有特定子串并删除,若没有找到子串,则不做任何操作,
 * 例子: 
 *  给定字符串: "abababab", 特定子串: "aba", 结果: "bb"
 *  给定字符串: "aabcbc", 特定子串: "abc", 结果: "abc",而不是NULL
*/
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int delete_sub_str(const char *str, const char *sub_str, char *result_str)
{
    int result = 0, index = 0;
    int len = strlen(str);
    int s_len = strlen(sub_str);

    for (int i = 0; i < len;)
    {
        int t = 0;
        for (; t < s_len; ++t)
        {
            if (str[i + t] != sub_str[t])
            {
                break;
            }
        }
        if (t >= s_len)
        { // 找到子串
            i += s_len;
            result++;
        }
        else
        {
            result_str[index++] = str[i];
            i++;
        }
    }
    result_str[index] = '\0';

    return result;
}
void showResult(const char input[], const char substr[], char output[], int res_count)
{
    printf("[%s] - [%s](%d)count is [%s]\n", input, substr, res_count, output);
    printf("\n\n\n");
}

int main()
{
    int res_count = 0;
    const char input[] = "abababab";
    const char sub[] = "aba";
    char *res = (char *)calloc(strlen(input), sizeof(char));
    res_count = delete_sub_str(input, sub, res);
    showResult(input, sub, res, res_count);

    const char input2[] = "aabcbc";
    const char sub2[] = "abc";
    char *res2 = (char *)calloc(strlen(input2), sizeof(char));
    res_count = delete_sub_str(input2, sub2, res2);
    showResult(input2, sub2, res2, res_count);

    const char input3[] = "abcde123abcd123";
    const char sub3[] = "1234";
    char *res3 = (char *)calloc(strlen(input3), sizeof(char));
    res_count = delete_sub_str(input3, sub3, res3);
    showResult(input3, sub3, res3, res_count);

    const char input4[] = "abcde123abcd123";
    const char sub4[] = "123";
    char *res4 = (char *)calloc(strlen(input4), sizeof(char));
    res_count = delete_sub_str(input4, sub4, res4);
    showResult(input4, sub4, res4, res_count);

    return 0;
}