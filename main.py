import classes as z

f = open("a.txt", "r")

width_grid, height_grid = f.readline().rstrip('\n').split(" ")
width_grid, height_grid = int(width_grid), int(height_grid)
num_building, num_antennas, reward = f.readline().rstrip('\n').split(" ")
num_building, num_antennas, reward = int(num_building), int(num_antennas), int(reward)

map = z.Map(width_grid, height_grid, num_building, num_antennas)
building_list = []
antennas_list = []

for i in range(num_building):
    x, y, latecy, speed = f.readline().rstrip('\n').split(" ")
    x, y, latecy, speed =  int(x), int(y), int(latecy), int(speed)
    building_list.append(z.Building(x, y, latecy, speed))

for i in range(num_antennas):
    range_A, speed = f.readline().rstrip('\n').split(" ")
    range_A, speed = int(range_A), int(speed)
    antennas_list.append(z.Antennas(range_A, speed))