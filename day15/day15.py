import re

with open('day15Input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]


def merge_intervals(intervals):
    intervals.sort()
    stack = [intervals[0]]

    for i in intervals[1:]:
        if stack[len(stack) - 1][0] <= i[0] <= stack[len(stack) - 1][1]:
            stack[len(stack) - 1][1] = max(stack[len(stack) - 1][1], i[1])
        else:
            stack.append(i)

    return stack



stuff = {}
sensors = []
beacons = []
for c in content:
    x = c.split(':')
    sensor = x[0]
    result = re.search('x=([-]?[0-9]*), y=([-]?[0-9]*)', sensor)
    sensor_place = (int(result.group(1)), int(result.group(2)))
    stuff[sensor_place] = 'S'

    beacon = x[1]
    beacon_result = re.search('x=([-]?[0-9]*), y=([-]?[0-9]*)', beacon)
    beacon_place = (int(beacon_result.group(1)), int(beacon_result.group(2)))
    stuff[beacon_place] = 'B'

    distance = abs(sensor_place[0] - beacon_place[0]) + abs(sensor_place[1] - beacon_place[1])
    sensors.append([sensor_place, distance])
    beacons.append(beacon_place)


ygoal = 2000000

xranges = []
for sensor in list(filter(lambda a: a[0][1] - a[1] <= ygoal <= a[0][1] + a[1], sensors)):
    distance = sensor[1]
    x = sensor[0][0]
    y = sensor[0][1]

    xrange = (distance - (abs(ygoal - y)))
    xranges.append([x - xrange,  x + xrange])

intervals = merge_intervals(xranges)

count = 0
for i in intervals:
    count += i[1] - i[0]


print('part 1: ' + str(count))

maxsearch = 4000000
sets = []
for curry in range(maxsearch + 1):
    if curry % 100000 == 0:
        print(curry)

    xranges = []
    for sensor in list(filter(lambda a: a[0][1] - a[1] <= curry <= a[0][1] + a[1], sensors)):
        distance = sensor[1]
        x = sensor[0][0]
        y = sensor[0][1]

        xrange = (distance - (abs(curry - y)))
        xranges.append([max(0, x - xrange), min(maxsearch, x + xrange)])

    intervals = merge_intervals(xranges)

    if len(intervals) > 1:
        currx = intervals[0][1] + 1
        print('part 2:  y: ' + str(curry) + ' x: ' + str(currx) + ' answer: ' + str(currx * 4000000 + curry))

    curry += 1
