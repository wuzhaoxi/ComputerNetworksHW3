# -*- coding: utf-8 -*-

# usage: map.xxx
from map1 import *
from func1 import *
import sys

while True:
	print("###############")
	print("这是一个上海地铁导航图程序")
	print("接下来，请根据提示输入起站点和终点站的中文名称")
	print("输入q退出程序")
	print("###############\n")
	
	src = raw_input("请输入起点站名称（中文）:\n")
	if src == "q":
		sys.exit()
	des = raw_input("请输入终点站名称（中文）:\n")
	if des == "q":
		sys.exit()
		
	if (find_station(stations, src) == False) or (find_station(stations, des) == False):
		print("站点名称有误，请重新输入！\n")
	else:
		my_Bellmen_less_transfer(get_trip(src, des, stations), stations)
		#my_Bellmen_less_time(get_trip(src, des, stations), stations)
		temp = find_station(stations, src).table
		#for key in temp:
		#	print "key is: ", key, " and distance is ", temp[key][0], " , previous node is ", temp[key][1]
		[path, time] = get_path(src, des, stations)
		print "\n一共要经过 ", len(path)," 站", ", 总共耗时: ", time, " 分钟\n"
		print "经过的站点为: "
		station_number = 1
		for item in path:
			print station_number, " : ", item
			station_number = station_number + 1
		print "\n"