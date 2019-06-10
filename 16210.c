#include <stdio.h>
#include <stdlib.h>
#include <string.h>

long transfer16210(char *source)
{
    long result = 0;
    if (source == NULL || (*source != '0' || *(source + 1) != 'x'))
    {
        printf("error:[%s]\n", source);
        return result;
    }

    int len = strlen(source);
    char *p = source++;
    char *head = p++;
    p = head;
    char *tail = NULL;
    while (p)
    {
        tail = p;
        p++;
    }

    while (tail > p)
    {
        printf("%c ", *tail);
        result += (*tail - 'A' + 1) * 16;
        tail--;
    }
    return result;
}

int main()
{
    char buf[1000];
    long result;
    while (~scanf("%s", buf) != EOF)
    {
        result = transfer16210(buf);
        printf("%ld\n", result);
    }

    return 0;
}