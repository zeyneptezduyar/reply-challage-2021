
class Map:
    def __init__(self, width, height, building_num, num_antennas, building_list, antennas_list):
        self.width = width
        self.height = height
        self.building_num = building_num
        self.num_antennas = num_antennas
        self.building_list = building_list
        self.antennas_list = antennas_list

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