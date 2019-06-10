#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import time

course = ["美术", "英语", "数学", "计算机", "音乐"]
time_list = [["09:00","10:00"], ["09:30","10:30"], ["10:00","11:00"], ["10:30","11:30"], ["11:00","12:00"]]

# 将起始处加入
result = [["美术"]]
processed = []

def collect_course():
	# 从1开始
	for i in range(1, len(course)):
		inner = []
		# 要比较的时间点
		start = time.mktime(time.strptime(time_list[i][0], "%H:%M"))
		end = time.mktime(time.strptime(time_list[i][1], "%H:%M"))

		# 依次获取result中的每个item（都是list）
		for k in range(len(result)):
			# 当前list
			item_list = result[k]
			print("rrr %s" % item_list)
			conflict = False
			# 遍历当前list的数据，然后比较
			for j in range(len(item_list)):
				#t = ([r for r, rr in enumerate(course) if rr == item_list[j]])[0]
				t = course.index(item_list[j])
				#print(t)
				b = time.mktime(time.strptime(time_list[t][0], "%H:%M"))
				c = time.mktime(time.strptime(time_list[t][1], "%H:%M"))
				print("%s, %s, %s" % (time_list[i][0], time_list[j][0], time_list[j][1]))
				print("abc, start %s, end %s, %s, %s" % (start, end, b, c))
				# 时间有冲突，查找下一个list
				if( (start < b and end > b and end < c) or (start > b and start < c) ):
					conflict = True
					print("conflict")
					break
			# 与当前list的数据都没有冲突，加入当前list,并跳出循环，进入下一轮
			if ((j >= (len(item_list)-1)) and not conflict):
				item_list.append(course[i])
				print("ttt %s" % item_list)
				break
		# 遍历结束还有冲突，就重新构造list
		if( (k >= (len(result)-1)) and conflict):
			inner.append(course[i])
			result.append(inner)
	print(result)

if __name__ == "__main__":
	for i in range(len(course)):
		print("%s: %s" % (course[i], time_list[i]),end= ',  ')
	print()
	collect_course()
