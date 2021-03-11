import classes as z
import random
import sys

if (len(sys.argv) == 1):
	print('Type input filename!!')
	sys.exit()

filename = str(sys.argv[1])

f = open(filename, "r")

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

f.close()

num_antennas = len(antennas_list)
placed_antennas = []

for i in range(num_antennas):
	placing = []
	while True:
		rand_x = random.randint(0, width_grid)
		rand_y = random.randint(0, height_grid)
		placing = [rand_x, rand_y]

		if placing not in placed_antennas:
			break

	placed_antennas.append(placing)

print(placed_antennas)

filename = filename[:-2]
output_filename = 'output_' + filename + 'txt'

out = open(output_filename, 'w')
# first line is num of antennas placed on grid
out.write(str(num_antennas) + '\n')

# next m lines is id of antenna, x, y coordinates
for i in range(num_antennas):
	out.write(str(i) + ' ' + str(placed_antennas[i][0]) + ' ' + str(placed_antennas[i][1]) + '\n')

out.close()