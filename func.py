# -*- coding: utf-8 -*-
   
# Find the station by its name     
def find_station(stations, sta_name):
	for item in stations:
		if item.name == sta_name:
			return item
	else:
		return False
			
# Get the stations of a trip from names			
def get_trip(sta_src_name, sta_des_name, stations):
	sta_src = find_station(stations, sta_src_name)
	sta_des = find_station(stations, sta_des_name)
	return [sta_src, sta_des]

# Dijkstra algorithm for routing: focus on less time
def my_Dijkstra_less_time(trip, stations):
	sta_src = trip[0]
	sta_des = trip[1]
	Q = []
	distance = {}
	for sta in stations:
		Q.append(sta.name)
		distance[sta.name] = [10000, "null"]
	distance[sta_src.name] = [0, "null"]
	def find_min_distance():
		temp = 100000
		sta_name = ""
		for name in Q:
			if distance[name][0] < temp:
				sta_name = name
				temp = distance[name][0]
		return sta_name
	def find_distance_u_v(src_name, des_name):
		src = find_station(stations, src_name)
		for item in src.neighbors:
			if item[0] == des_name:
				return item[1]
	current = 0
	while len(Q) > 0:
		temp = find_min_distance()
		if current < 5:
			print "temp is: ",temp
			current = current + 1
		Q.remove(temp)
		temp_sta = find_station(stations, temp)
		for item in temp_sta.neighbors:
			new_distance = distance[temp][0] + find_distance_u_v(temp, item[0])
			if new_distance < distance[item[0]][0]:
				distance[item[0]] = [new_distance, temp]
	return distance
	
# Dijkstra algorithm for routing: focus on less transfer
def my_Dijkstra_less_transfer(trip, stations):
	for sta in stations:
		for i in range(len(sta.neighbors)):
			if sta.neighbors[i][1] == 0.1:
				temp = sta.neighbors[i][0]
				sta.neighbors[i] = (temp,200)

	sta_src = trip[0]
	sta_des = trip[1]
	Q = []
	distance = {}
	for sta in stations:
		Q.append(sta.name)
		distance[sta.name] = [10000, "null"]
	distance[sta_src.name] = [0, "null"]
	def find_min_distance():
		temp = 100000
		sta_name = ""
		for name in Q:
			if distance[name][0] < temp:
				sta_name = name
				temp = distance[name][0]
		return sta_name
	def find_distance_u_v(src_name, des_name):
		src = find_station(stations, src_name)
		for item in src.neighbors:
			if item[0] == des_name:
				return item[1]
	current = 0
	while len(Q) > 0:
		temp = find_min_distance()
		if current < 5:
			print "temp is: ",temp
			current = current + 1
		Q.remove(temp)
		temp_sta = find_station(stations, temp)
		for item in temp_sta.neighbors:
			new_distance = distance[temp][0] + find_distance_u_v(temp, item[0])
			if new_distance < distance[item[0]][0]:
				distance[item[0]] = [new_distance, temp]
	return distance
	
# output the path
def get_path(distance, sta_src_name, sta_des_name):
	sta_path = sta_des_name
	path = []
	while distance.get(sta_path)[1] != "null":
		path = [sta_path] + path
		sta_path = distance.get(sta_path)[1]
	return [path, distance.get(sta_des_name)[0]]
	
	
	
		