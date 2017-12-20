#! /usr/bin/env python3

def change(llist, rlist):
	r=lenth-1
	tflag=1
	global flag
	global div
	while r>=0 and tflag:
		for l in range(lenth):
			if((rlist[r]-llist[l])*2<=div and rlist[r]>llist[l]):
				rlist[r],llist[l]=llist[l],rlist[r]
				rlist.sort()
				llist.sort()
				div=sum(rlist)-sum(llist)
				tflag=0
				break
			else:
				r-=1
	if(r<0):
	    flag=0
	return (llist,rlist)          

if(__name__=='__main__'):
	aa = [1782, 101, 21, 10, 3, 1]
	bb = [113, 453, 23, 121, 50, 1178]
#first
		#sumA = 1918 [1782, 101, 21, 10, 3, 1]
		#sumB = 1938 [113, 453, 23, 121, 50, 1178]
		#switch
		#sumA = 1930 [1782, 113, 21, 10, 3, 1]
		#sumB = 1926 [101, 453, 23, 121, 50, 1178]
#secord
		#sumA = 1918 [1782, 101, 21, 10, 3, 1]
		#sumB = 1938 [113, 453, 23, 121, 50, 1178]
		#[3, 10, 21, 23, 50, 1782]1889
		#[1, 101, 113, 121, 453, 1178]1967
		#78
	A = sum(aa)
	B = sum(bb)
	print("------------------source--------------")
	print("sumA = %d " % A, end='')
	print(aa)
	print("sumB = %d " % B, end='')
	print(bb)
	sourcelist=aa+bb
	sourcelist.sort()
	lenth=int(len(sourcelist)/2)
	llist=sourcelist[:lenth]
	rlist=sourcelist[lenth:]
	div=sum(rlist)-sum(llist)
	flag=1
	while flag:
		(llist,rlist) = change(llist,rlist)
	print(llist,end='')
	print(sum(llist))
	print(rlist,end='')
	print(sum(rlist))
	print(div)
