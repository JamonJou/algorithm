

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void gcRadio(char *dna, int d)
{
    int len = strlen(dna);
    int start = 0;

    if (len <= 0 || d <= 0)
    {
        return; // 起始位置
    }
    if (len <= d)
    { // 直接输出
        for (int i = 0; i < len; ++i)
            printf("%c", dna[i]);
        printf("\n");
        return;
    }

    int max_sub_len = len - d + 1;
    int *max_sub = (int *)calloc(max_sub_len, sizeof(int));
    // printf("dna=[%s]len(%d), d=%d, max_sub_len=%d\n", dna, len, d, max_sub_len);

    for (int i = 0; i < max_sub_len; ++i)
    {
        for (int j = i; j < i + d; ++j)
            if (dna[j] == 'G' || dna[j] == 'C')
                max_sub[i] += 1;
    }

    start = 0;
    // printf("max_sub>>> %d", max_sub[start]);
    for (int i = 1; i < max_sub_len; ++i)
    {
        // printf(" %d ", max_sub[i]);
        if (max_sub[i] > max_sub[start])
        {
            start = i;
        }
    }
    // printf("\nstart = %d\n", start);
    for (int i = start; i < start + d; ++i)
        printf("%c", dna[i]);
    printf("\n");
}

int main()
{
    char data[1000];
    int n;
    // while (NULL != gets(data))
    // {
    //     break;
    // }
    // scanf("%d\n", &n);

    scanf("%s \n%d", data, &n);
    gcRadio(data, n);
    return 0;
}