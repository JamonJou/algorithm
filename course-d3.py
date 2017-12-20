#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import time

course_dict = {}
course_dict["美术"] = ["09:00", "10:00"]
course_dict["英语"] = ["09:30", "10:30"]
course_dict["数学"] = ["10:00", "11:00"]
course_dict["计算机"] = ["10:30", "11:30"]
course_dict["音乐"] = ["11:00", "12:00"]

result = []

def collect_course():
	for item in course_dict.keys():
		inner = []
		# 要比较的时间点 
		start = time.mktime(time.strptime(course_dict[item][0], "%H:%M"))
		end = time.mktime(time.strptime(course_dict[item][1], "%H:%M"))

		if (len(result)):
			 # 依次获取result中的每个item（都是list）
			for k in range(len(result)):
				each_list = result[k]
				conflict = False
				# 遍历当前list的数据，然后比较
				for i in range(len(each_list)):
					b = time.mktime(time.strptime(course_dict[each_list[i]][0], "%H:%M"))
					c = time.mktime(time.strptime(course_dict[each_list[i]][1], "%H:%M"))
					# 时间有冲突，查找下一个list
					if( (start < b and end > b and end < c) or (start > b and start < c) ):
						conflict = True
						break
				# 与当前list的数据都没有冲突，加入当前list,并跳出循环，进入下一轮
				if (i >= (len(each_list)-1) and not conflict):
					each_list.append(item)
					break
			# 遍历结束还有冲突，就重新构造list
			if( (k >= (len(result)-1)) and conflict):
				inner.append(item)
				result.append(inner)
		else: # 加入第一个元素
			print("just print one time")
			inner.append(item)
			result.append(inner)
	print(result)

if __name__ == "__main__":
	print(course_dict)
	collect_course()
