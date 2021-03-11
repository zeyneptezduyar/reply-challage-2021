import math;


class Map:
    def __init__(self, width, height, building_num, num_antennas):
        self.width = width
        self.height = height
        self.building_num = building_num
        self.num_antennas = num_antennas

    def __str__(self):
        return "This map has the width of " + str(self.width) + ", height of " + str(self.height) + ", " + str(self.building_num) + " buildings, and " + str(self.num_antennas) + " antennas"


class Building:
    def __init__(self, x, y, latency, speed):
        self.x = x
        self.y = y
        self.latency = latency
        self.speed = speed
    
    def __str__(self):
        return "This building is located on " + str(self.x) + " " + str(self.y) + " with latency " + str(self.latency) + " and speed " + str(self.speed)

class Antennas:
    def __init__(self, range_A, speed):
        self.range_A = range_A
        self.speed = speed
    
    def __str__(self):
        return "This antenna has the range of " + str(self.range_A) + " and speed " + str(self.speed)

def calc_distance(x1, y1, x2, y2):
    distance = abs(x1-x2) + abs(y1-y2)
    return distance


f = open("a.txt", "r")

width_grid, height_grid = f.readline().rstrip('\n').split(" ")
width_grid, height_grid = int(width_grid), int(height_grid)
num_building, num_antennas, reward = f.readline().rstrip('\n').split(" ")
num_building, num_antennas, reward = int(num_building), int(num_antennas), int(reward)

map = Map(width_grid, height_grid, num_building, num_antennas)
building_list = []
antennas_list = []

for i in range(num_building):
    x, y, latecy, speed = f.readline().rstrip('\n').split(" ")
    x, y, latecy, speed =  int(x), int(y), int(latecy), int(speed)
    building_list.append(Building(x, y, latecy, speed))

for i in range(num_antennas):
    range_A, speed = f.readline().rstrip('\n').split(" ")
    range_A, speed = int(range_A), int(speed)
    antennas_list.append(Antennas(range_A, speed))

print(map)

for building in building_list:
    print(building)

for antenna in antennas_list:
    print(antenna)

print(calc_distance( 1,5, 4,17))
