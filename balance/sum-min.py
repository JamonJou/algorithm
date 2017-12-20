#! /usr/bin/env python3
'''
   有两个序列a,b，大小都为n,序列元素的值任意整形数，无序；要求：通过交换a,b中的元素，使[序列a元素的和]与[序列b元素的和]之间的差绝对值最小
   求解思路：

'''
aa = [1782, 101, 21, 10, 3, 1]
bb = [113, 453, 23, 121, 50, 1178]
dp = [[False for i in range(len(aa)+1)] for i in range(len(bb)+1)]
#bool dp[100][10000]
def dongtaiguihua(items, alllen, allsum):
	sublen = alllen/2
	dp[0][0] = True
	i = 1
	while i <= alllen:
		j = min(i, sublen)
		while j >= 1:
			s = 1
			while s <= allsum/2:
				if s >= items[i] and dp[j-1][s-items[i]]:
					dp[j][s] = True
				s = s + 1
			j = j - 1
		i = i + 1
	t = allsum/2
	while (t >= 1) and (not dp[alllen][t]):
		t = t - 1
	print(allsum - 2*t)

if __name__ == "__main__":
	if(len(aa) == len(bb)):
		print(dp)
		c = aa + bb
		print(c)
		print("len = %d, sum = %ld" % (len(c), sum(c)))
		dongtaiguihua(c, len(c), sum(c))
