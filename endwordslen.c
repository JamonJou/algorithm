/**
 * 项目描述:
 * 计算字符串最后一个单词的长度，单词以空格隔开。
输入描述:
    一行字符串，非空，长度小于5000。
输出描述:
    整数N，最后一个单词的长度。
 * 示例:
    输入
        hello world
    输出
        5
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int endwordslen(char *source)
{
    int result = 0;
    if (source == NULL)
        return result;

    char *cur = source;
    char *end = NULL;

    /**
     * 1. end指向最后一个word
     * 2. 回溯end到空格或者start(也就是source),cnt++
     * 3. 如果end == start表示没有没有空格,即cnt+1;
     * 4. 如果end != start表示遇到过空格,即cnt;
     */
    while (*cur != '\0')
    {
        end = cur;
        cur++;
    }

    while (*end != ' ' && end != source)
    {
        result++;
        end--;
    }
    if (end == source)
    {
        result += 1;
    }

    return result;
}

int main()
{
    char source[5000];
    int cnt = 0;
    while (NULL != gets(source))
    {
        break;
    }
    cnt = endwordslen(source);
    printf("%d\n", cnt);

    return 0;
}