import operator
import random

class Map:
    def __init__(self, width, height, building_num, num_antennas, building_list, antennas_list):
        self.width = width
        self.height = height
        self.building_num = building_num
        self.num_antennas = num_antennas
        self.building_list = building_list
        self.antennas_list = antennas_list
        self.matrix = [[False for j in range(height)] for i in range(width)]

    def __str__(self):
        return "This map has the width of " + str(self.width) + ", height of " + str(self.height) + ", " + str(self.building_num) + " buildings, and " + str(self.num_antennas) + " antennas"

    def get_building_list(self):
        return self.building_list
    
    def get_antenna_list(self):
        return self.antennas_list


class Building:
    def __init__(self, x, y, latency, speed):
        self.x = x
        self.y = y
        self.latency = latency
        self.speed = speed
    
    def __str__(self):
        return "This building is located on " + str(self.x) + " " + str(self.y) + " with latency " + str(self.latency) + " and speed " + str(self.speed)

    def get_speed(self):
        return self.speed

class Antennas:
    def __init__(self, range_A, speed):
        self.range_A = range_A
        self.speed = speed
        self.point = 0
    
    def __str__(self):
        return "This antenna has the range of " + str(self.range_A) + " and speed " + str(self.speed)

    def get_speed(self):
        return self.speed
    
    def set_point(self, x, y):
        self.point = Point(x, y)



class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def get_distance(x1, y1, x2, y2):
    return abs(x1-x2) + abs(x2-y2)

def get_mid_point(x1, y1, x2, y2):
    x_mid = abs(x1-x2)
    y_mid = abs(x2-y2)
    if (x1 < x2):
        x = x1+x_mid
    else:
        x = x2+x_mid
    
    if (y1 < y2):
        y = y1+y_mid
    else:
        y = y2+y_mid
    if (x > map.width):
        x = random.randint(1, width_grid-1)
    if (y == map.height):
        y = random.randint(1, height_grid-1)
    return x,y


f = open("c.txt", "r")

width_grid, height_grid = f.readline().rstrip('\n').split(" ")
width_grid, height_grid = int(width_grid), int(height_grid)
num_building, num_antennas, reward = f.readline().rstrip('\n').split(" ")
num_building, num_antennas, reward = int(num_building), int(num_antennas), int(reward)

building_list = []
antennas_list = []

for i in range(num_building):
    x, y, latecy, speed = f.readline().rstrip('\n').split(" ")
    x, y, latecy, speed =  int(x), int(y), int(latecy), int(speed)
    building_list.append(Building(x, y, latecy, speed))

i = 0
for i in range(num_antennas):
    range_A, speed = f.readline().rstrip('\n').split(" ")
    range_A, speed = int(range_A), int(speed)
    antennas_list.append(Antennas(range_A, speed))
    i+=1

f.close()

map = Map(width_grid, height_grid, num_building, num_antennas, building_list, antennas_list)

building_list_sorted = sorted(building_list, key=operator.attrgetter('speed'))
antennas_list_sorted = sorted(antennas_list, key=operator.attrgetter('speed'))

mid_points = []

for i in range(len(building_list_sorted)-1):
    b1 = building_list_sorted[i]
    b2 = building_list_sorted[i+1]
    mid_point_x, mid_point_y = get_mid_point(b1.x, b1.y, b2.x, b2.y)
    mid_point = [mid_point_x, mid_point_y]
    if (mid_point[0] > width_grid):
        mid_point[0] = width_grid - 1
    if (mid_point[1] > height_grid):
        mid_point[1] = height_grid - 1
    while (mid_point in mid_points):
        mid_point = [random.randint(1, width_grid-1), random.randint(1, height_grid-1)]
    mid_points.append(mid_point)


f = open("answerC.txt", "w")
f.write(str(num_antennas))
i = 0 

for ant in antennas_list_sorted:
    ant.set_point(mid_points[i][0], mid_points[i][1])
    i+=1

i = 0
for ant in antennas_list:
    f.write("\n"+str(i) + " " + str(ant.point.x) + " " + str(ant.point.y))
    i+=1

f.close()