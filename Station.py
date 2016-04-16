# -*- coding: utf-8 -*-

'''
index int: index of the station
line int: num of metro line
name string: name of the station
neighbor list: neighbors of the station and their distances from the station 
'''

# Station Class
class Station:
    def __init__(self, index, line, name, neighbors):
        self.index = index
        self.line = line
        self.name = name
        self.neighbors = neighbors
        
    def get_name(self):
        return self.name
        
    def get_line(self):
        return self.line
        
    def get_index(self):
        return self.index
        
    def get_neighbors(self):
        return self.neighbors