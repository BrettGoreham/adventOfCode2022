with open('day2Input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

points = 0
for c in content:
    them = c[0]
    us = c[2]

    if us == 'X':
        points += 1
        if them == 'A':
            points += 3
        elif them == 'C':
            points += 6

    elif us == 'Y':
        points += 2
        if them == 'A':
            points += 6
        elif them == 'B':
            points += 3

    elif us == 'Z':
        points += 3
        if them == 'B':
            points += 6
        elif them == 'C':
            points += 3

print(points)

point = {'A': 1, 'B': 2, 'C': 3}
win = {'A': 'B', 'B': 'C', 'C': 'A'}
lose = {'A': 'C', 'B': 'A', 'C': 'B'}
points = 0
for c in content:
    them = c[0]
    us = c[2]

    if us == 'X':
        points += point[lose[them]]

    elif us == 'Y':
        points += point[them]
        points += 3

    elif us == 'Z':
        points += point[win[them]]
        points += 6

print(points)