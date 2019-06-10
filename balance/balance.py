#! /usr/bin/env python3
import sys
#aa = [1782, 101, 21, 10, 1, 3]
aa = [100 ,99 ,98 ,1 ,2 ,3]
#aa = [93, 91, 90, 82, 81, 74, 74, 74, 74, 68]
#bb = [23,113, 453, 121, 50, 1178]
bb = [1, 2, 3, 4, 5, 40]
#bb = [60, 57, 49, 48, 48, 45, 36, 35, 29, 22]
div = sum(aa)-sum(bb)

def balance(a, b, lenab):
	global div
	if div == 0:
		return;
	for i in range(lenab):
		for j in range(lenab):
			x = a[i] - b[j]
			A1 = div - 2*x
			print("abs(A1) = %d, abs(A) =%d" % (A1, div))
			if ( abs(A1) < abs(div) ):
				a[i],b[j] = b[j],a[i]
				div,A1 = A1,div
				print("========A=%d,A1=%d======switch a[%d] b[%d]========================" % (div, A1, i,j))
				print("sumA = %d " % sum(a), end='')
				print(a)
				print("sumB = %d " % sum(b), end='')
				print(b)
				print("sumA - sumB = %d " % (sum(a) - sum(b)))
				balance(a, b, lenab)

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
		balance(aa, bb,len(aa))
		print("------------------balance--------------")
		A = sum(aa)
		B = sum(bb)
		C = sum(aa)-sum(bb)
		print("sumA = %d " % A, end='')
		print(aa)
		print("sumB = %d " % B, end='')
		print(bb)
		print("sumA - sumB = %d " % C)
