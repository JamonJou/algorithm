/**
 * 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
 * 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
 * 示例:
 * 给定 nums = [2, 7, 11, 15], target = 9
 * 因为 nums[0] + nums[1] = 2 + 7 = 9
 * 所以返回 [0, 1]
 * 
*/
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int *twoSum(int *nums, int numsSize, int target, int *returnSize)
{
    // int *result = (int *)calloc(2, sizeof(int));
    int *result = NULL;
    int i, j;
    for (i = 0; i < numsSize - 1; ++i)
    {
        if (nums[i] < target)
            for (j = i + 1; i < numsSize; ++j)
            {
                if (nums[i] + nums[j] == target)
                {
                    result = (int *)calloc(2, sizeof(int));
                    // result = malloc(sizeof(int) * 2);
                    result[0] = i;
                    result[1] = j;
                    *returnSize = 2;
                    return result;
                }
            }
    }
    return NULL;
}
int main()
{
    int nums[] = {2, 7, 11, 15};
    int target = 9, size = 2;
    int *res = twoSum(nums, 4, target, &size);
    printf("%d %d\n", res[0], res[1]);
}