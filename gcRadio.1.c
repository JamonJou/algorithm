#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int gcRadio(char *dna, int d)
{
    int len = strlen(dna);
    int start = 0;
    if (len <= d || len <= 0 || d <= 0)
    {
        return start; // 起始位置
    }

    int max_sub_len = len - d + 1;
    int *max_sub = (int *)calloc(max_sub_len, sizeof(int));
    for (int i = 0; i < max_sub_len; ++i)
    {
        for (int j = i; j < i + d; ++j)
            if (dna[j] == 'G' || dna[j] == 'C')
                max_sub[i] += 1;
    }

    start = 0;
    for (int i = 1; i < max_sub_len; ++i)
    {
        if (max_sub[i] > max_sub[start])
        {
            start = i;
        }
    }
    return start;
}

int main()
{
    char data[1000];
    int n, start = 0;

    scanf("%s \n%d", data, &n);
    start = gcRadio(data, n);
    for (int i = start; i < start + n; ++i)
        printf("%c", data[i]);
    printf("\n");
    return 0;
}