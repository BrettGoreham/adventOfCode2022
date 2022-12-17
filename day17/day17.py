with open('day17Input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

windstring = content[0]


def findHighest(coords):
    v = -1
    for k in coords:
        if k[1] > v:
            v = k[1]

    return v


line = [(0, 0), (1, 0), (2, 0), (3, 0)]
cross = [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)]
L = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
vert = [(0, 0), (0, 1), (0, 2), (0, 3)]
square = [(0, 0), (1, 0), (1, 1), (0, 1)]

objects = [line, cross, L, vert, square]


cycleHeight = -1

cycleDetector = {}
objectCount = 0
windCount = 0
map = {}
while objectCount < 4000:
    if objectCount == 2022:
        print('part 1: ' + str(findHighest(map) + 1))

    rockList = objects[objectCount % len(objects)]
    objectCount += 1
    bottomLeft = [2, findHighest(map.keys()) + 4]
    rested = False
    while not rested:
        wind = windstring[windCount % len(windstring)]
        windCount += 1
        winddir = 1 if wind == '>' else -1

        pushed = True
        for x in rockList:
            check = [bottomLeft[0] + x[0] + winddir, bottomLeft[1] + x[1]]

            if not (0 <= check[0] < 7 and (check[0], check[1]) not in map):
                pushed = False

        if pushed:
            bottomLeft[0] += winddir

        fallable = True
        for x in rockList:
            check = [bottomLeft[0] + x[0], bottomLeft[1] + x[1] - 1]
            if (check[0], check[1]) in map or bottomLeft[1] + x[1] == 0:
                fallable = False

        if not fallable:
            rested = True
        else:
            bottomLeft[1] -= 1

    for x in rockList:
        index = (bottomLeft[0] + x[0], bottomLeft[1] + x[1])
        map[index] = "#"

    if (objectCount % len(objects), windCount % len(windstring)) in cycleDetector:
        last = cycleDetector[(objectCount % len(objects), windCount % len(windstring))]
        objectCycle = objectCount - last[0]
        cycleHeight = findHighest(map) - last[1]

        if (1000000000000 - objectCount) % objectCycle == 0:
            cyclesRemaining = (1000000000000 - objectCount) / objectCycle
            height = int(cyclesRemaining * cycleHeight)
            print('1trilly = ' + str(height + findHighest(map) + 1))

    else:
        cycleDetector[(objectCount % len(objects), windCount % len(windstring))] = (objectCount, findHighest(map))




