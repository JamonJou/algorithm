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
processed = []

def collect_course():
	#print("美术 %s" % course_dict['美术'][0])
	for item in course_dict.keys():
		#if item not in processed:
		inner = []
		if (len(result)):
			for k in range(len(result)):
				each_list = result[k]
				for i in range(len(each_list)):
					a = time.mktime(time.strptime(course_dict[item][0], "%H:%M"))
					b = time.mktime(time.strptime(course_dict[each_list[i]][0], "%H:%M"))
					c = time.mktime(time.strptime(course_dict[each_list[i]][1], "%H:%M"))
					#a = int(time.strftime("%H:%M", course_dict[item][0]))
					#b = int(time.strftime("%H:%M", course_dict[each_list[i]][0]))
					#c = int(time.strftime("%H:%M", course_dict[each_list[i]][1]))
					if( (a >= b and a <= c) or (a <= b and a >= c) ):
						inner.append(item)
						break
			if(len(inner)):
				result.append(inner)
			else:
				each_list.append(item)
		else:
			inner.append(item)
			result.append(inner)
		#processed.append(item)
	print(result)

if __name__ == "__main__":
	print(course_dict)
	collect_course()
