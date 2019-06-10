/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 * 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
 * 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
 * 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
 * 示例：
 * 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
 * 输出：7 -> 0 -> 8
 * 原因：342 + 465 = 807
 */
#include <stdio.h>
#include <stdlib.h>

struct ListNode
{
    int val;
    struct ListNode *next;
};

struct ListNode *addTwoNumbers(struct ListNode *l1, struct ListNode *l2)
{
    if (l1 == NULL)
    {
        return l2;
    }
    if (l2 == NULL)
    {
        return l1;
    }

    struct ListNode *head = l1;
    struct ListNode *l1_cur = l1;
    struct ListNode *l2_cur = l2;
    struct ListNode *l1_cur_prev = NULL;
    // struct ListNode *l2_cur_prev = NULL;
    int delta = 0;
    int sum = 0;

    while (l1_cur && l2_cur)
    {
        sum = l1_cur->val + l2_cur->val + delta;
        l1_cur->val = sum % 10;
        delta = sum / 10;
        l1_cur_prev = l1_cur;
        // l2_cur_prev = l2_cur;
        l1_cur = l1_cur->next;
        l2_cur = l2_cur->next;
    }

    if (l1_cur != NULL || l2_cur != NULL)
    {
        if (l1_cur == NULL)
        {
            l1_cur_prev->next = l2_cur;
            l1_cur = l2_cur;
        }

        while (l1_cur)
        {
            sum = l1_cur->val + delta;
            l1_cur->val = sum % 10;
            delta = sum / 10;
            l1_cur_prev = l1_cur;
            l1_cur = l1_cur->next;
        }
        if (delta > 0)
        {
            struct ListNode *tmp = (struct ListNode *)malloc(sizeof(struct ListNode));
            tmp->val = delta;
            tmp->next = NULL;
            l1_cur_prev->next = tmp;
        }
    }
    else
    {
        if (delta > 0)
        {
            struct ListNode *tmp = (struct ListNode *)malloc(sizeof(struct ListNode));
            tmp->val = delta;
            tmp->next = NULL;
            l1_cur_prev->next = tmp;
        }
    }

    return head;
}
