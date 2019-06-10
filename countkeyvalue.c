#include <stdio.h>
#include <stdlib.h>

#define MAX_KEY 1000

void countKV(int *key, int *value, int len)
{
    int *cur = key;
    int *mi = cur;

    // 先排序
    while (cur)
    {
        int *p = cur;
        while (p)
        {
            if (*mi < *p)
            {
                mi = p;
            }
            p++;
        }

        if (mi != cur)
        { // 交换数据
            int tmp = *mi;
            *mi = *cur;
            *cur = tmp;
        }
        cur++;
    }
    // 先统计
    int *cur_value = value;
    int *head = NULL;
    int *head_value = NULL;
    cur = key;
    while (cur && cur_value)
    {
        head = cur;
        head_value = cur_value;
        int *p = cur++;
        int *q = cur_value++;
        int cnt = 0;
        while (p && q)
        {
            if (*p != *head)
            {
                break;
            }
            *head_value = (*head_value + *q);
            *q = 0;
            p++;
            q++;
            cnt++;
        }
        printf("%d %d\n", head, head_value);
        cur += cnt;
    }

    // 排序
}

int main()
{
    int n, i;
    int key, value;
    int array[MAX_KEY] = {0};
    while (~scanf("%d", &n) && n > 0)
    {
        // int *key = malloc(n * sizeof(int));
        // int *value = malloc(n * sizeof(int));
        for (i = 0; i < n; ++i)
        {
            // scanf("%d %d\n", &key[i], &value[i]);
            // countKV(key, value, n);
            scanf("%d %d\n", &key, &value);
            array[key] += value;
        }
        // free(key);
        // free(value);
        for (i = 0; i < n; ++i)
        {
            if (array[i])
            {
                printf("%d %d\n", i, array[i]);
            }
        }
    }

    return 0;
}