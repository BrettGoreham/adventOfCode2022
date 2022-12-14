with open('day14Input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]


rocksand= {}
for c in content:
    points = c.split(' -> ')

    start = points[0]
    start = [int(x) for x in start.split(',')]

    for point in points[1:]:
        point = [int(x) for x in point.split(',')]
        rocksand[(start[0], start[1])] = '#'
        if start[0] == point[0]:
            increase = int((point[1] - start[1]) / abs(point[1] - start[1]))
            while start[1] != point[1]:
                start[1] += increase
                rocksand[(start[0], start[1])] = '#'
        else:
            increase = int((point[0] - start[0]) / abs(point[0] - start[0]))
            while start[0] != point[0]:
                start[0] += increase
                rocksand[(start[0], start[1])] = '#'


highesty = max([x[1] for x in rocksand.keys()])
floor = highesty + 2

tiptopped = False
sand_before_floor = 0
sand_count = 0
while not tiptopped:
    sand_count += 1
    sand = [500, 0]
    rested = False
    while not rested:
        if sand[1] + 1 > highesty and sand_before_floor == 0:
            sand_before_floor = sand_count - 1

        if sand[1] == floor - 1:
            rested = True
            rocksand[(sand[0], sand[1])] = '+'
        elif (sand[0], sand[1] + 1) not in rocksand.keys():
            sand[1] += 1
        elif (sand[0] - 1, sand[1] + 1) not in rocksand.keys():
            sand[0] -= 1
            sand[1] += 1
        elif (sand[0] + 1, sand[1] + 1) not in rocksand.keys():
            sand[0] += 1
            sand[1] += 1
        else:
            rested = True
            rocksand[(sand[0], sand[1])] = '+'

    if (500, 0) in rocksand.keys():
        tiptopped = True


print('part 1: ' + str(sand_before_floor))
print('part 2: ' + str(sand_count))
