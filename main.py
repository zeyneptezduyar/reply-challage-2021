import classes as z

f = open("d.txt", "r")

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


def calc_distance(x1,y1,x2,y2):
    dis = abs(x1-x2) + abs(y1-y2)
    return dis

#building_list.sort(key=lambda b: b.x, reverse=False) #put them in horizontal order
antennas_list.sort(key=lambda a: a.range_A, reverse=True) #sort by range

# for b in building_list:
#     print(b)

dist_list = []

for i in range(0, len(building_list)-1):
    current_b = building_list[i]
    next_b = building_list[i+1]
    dis = calc_distance(current_b.x, next_b.x, current_b.y, next_b.y)
    dist_list.append(dis)

midpoints = []
second_list = []

for i in range(0,int(len(building_list)), 35):
    second_list.append(building_list[i])

building_list = second_list

for i in range(0, len(antennas_list)):
    x  = building_list[i].x 
    y  = building_list[i].y 

    if x >= width_grid:
        x = width_grid-1
    if y >= height_grid:
        y = height_grid -1
    
    midpoints.append([x,y])


antenna_count = len(antennas_list)
print(antenna_count)
midpoin_count = len(midpoints)
print(midpoin_count)
index = 0

f = open("d_output.txt", "w")
f.write(str(antenna_count) +'\n')
while midpoin_count >0:

    f.write(str(index) + " " + str(midpoints[index][0]) + " " + str(midpoints[index][1]))
    if antenna_count > 1:
        f.write('\n')
    index += 1
    midpoin_count-=1
f.close()


