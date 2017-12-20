#! /usr/bin/env python3
'''
   有两个序列a,b，大小都为n,序列元素的值任意整形数，无序；要求：通过交换a,b中的元素，使[序列a元素的和]与[序列b元素的和]之间的差绝对值最小
   求解思路：
    当前数组a和数组b的和之差为
    A = sum(a) - sum(b)
    a的第i个元素和b的第j个元素交换后，a和b的和之差为
    A' = sum(a) - a[i] + b[j] - （sum(b) - b[j] + a[i])
           = sum(a) - sum(b) - 2 (a[i] - b[j])
           = A - 2 (a[i] - b[j])
    设x = a[i] - b[j]
    |A| - |A'| = |A| - |A-2x|
    |A'|= |A-2x|
    假设A > 0,
    当x 在 (0,A)之间时，做这样的交换才能使得交换后的a和b的和之差变小，x越接近A/2效果越好,
    如果找不到在(0,A)之间的x，则当前的a和b就是答案。
    所以算法大概如下：
    在a和b中寻找使得x在(0,A)之间并且最接近A/2的i和j，交换相应的i和j元素，重新计算A后，重复前面的步骤直至找不到(0,A)之间的x为止。
'''
'''
if sum(a) == sum(b), return 0
so we suppose sum(a) > sum(b)
def entry(a, b, A):
	A = sum(a)-sum(b)
	B = {2^32-1};
	C = [];
	for i in range(n):
		for j in range(n):
			if(a[i] - b[j] > 0)
				B[i][j] = abs(A/2 - a[i] - b[j])
		# compare B[i][j]
		flag = int(1)
		for k in range(n):
			if(B[i][flag] > B[i][k])
				flag = k
		C[i] = k
'''
aa = [1782, 101, 21, 10, 3, 1]
bb = [113, 453, 23, 121, 50, 1178]

def balance(a, b):
	if len(a) != len(b):
		return
	n = len(a)
	ifCycle = True
	while ifCycle:
		ifCycle = False
		for i in range(n):
			for j in range(n):
				x = a[i] - b[j]
				t = sum(a) - sum(b)
				if x > 0 and x < t:
					ifCycle = True
					a[i],b[j] = b[j],a[i]
					print("=====================switch a[%d] b[%d]========================" % (i,j))
					print(a)
					print(b)
				#elif x > :

if __name__ == "__main__":
	if(len(aa) == len(bb)):
		A = sum(aa)
		B = sum(bb)
		C = sum(aa)-sum(bb)
		print("------------------source--------------")
		print("sumA = %d " % A, end='')
		print(aa)
		print("sumB = %d " % B, end='')
		print(bb)
		print("sumA - sumB = %d " % C)
		if C > 0:
			balance(aa, bb)
		else:
			balance(bb, aa)
		print("------------------balance--------------")
		print("sumA = %d " % sum(aa), end='')
		print(aa)
		print("sumB = %d " % sum(bb), end='')
		print(bb)
		print("sumA - sumB = %d " % (sum(aa) - sum(bb)))
