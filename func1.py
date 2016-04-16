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
	
# my_Bellmen algorithm: focus on less time
def my_Bellmen_less_time(trip, stations):
	sta_src = trip[0]
	sta_des = trip[1]
	
	# if some table changes
	flag = True
	while flag:
		flag = False
		for sta in stations:
			for neighbor_sta_name in sta.neighbors_set:
				if exchange_table(sta, neighbor_sta_name, stations):
					flag = True	
	
# my_Bellmen algorithm: focus on less transfer
def my_Bellmen_less_transfer(trip, stations):
	for sta in stations:
		for i in range(len(sta.neighbors)):
			if sta.neighbors[i][1] == 0.1:
				temp = sta.neighbors[i][0]
				sta.neighbors[i] = (temp,200)

	sta_src = trip[0]
	sta_des = trip[1]
	
	# if some table changes
	flag = True
	while flag:
		flag = False
		for sta in stations:
			for neighbor_sta_name in sta.neighbors_set:
				if exchange_table(sta, neighbor_sta_name, stations):
					flag = True

# Find the distance between two nodes					
def find_distance_u_v(src, des_name):
	#src = find_station(stations, src_name)
	for item in src.neighbors:
		if item[0] == des_name:
			return item[1]
					
# Exchange information between tables
def exchange_table(sta, neighbor_sta_name, stations):
	neighbor_sta = find_station(stations, neighbor_sta_name)
	flag = False
	for key in neighbor_sta.table:
		if sta.table.has_key(key):
			if sta.table[key][0] > neighbor_sta.table[key][0] + find_distance_u_v(sta, neighbor_sta_name):
				sta.table[key] = [neighbor_sta.table[key][0] + find_distance_u_v(sta, neighbor_sta_name), neighbor_sta.name]
				flag = True
		else:
			sta.table[key] = [neighbor_sta.table[key][0] + find_distance_u_v(sta, neighbor_sta_name), neighbor_sta.name]
			flag = True
	return flag
			
	
# Output the path
def get_path(sta_src_name, sta_des_name, stations):
	sta_src = find_station(stations, sta_src_name)
	path = []
	temp = sta_src
	while temp.table.get(sta_des_name)[1] != "null":
		path = path + [temp.table.get(sta_des_name)[1]]
		temp = find_station(stations, temp.table.get(sta_des_name)[1])
	path = path + [sta_des_name]
	return [path, sta_src.table.get(sta_des_name)[0]]
	
	
	
		