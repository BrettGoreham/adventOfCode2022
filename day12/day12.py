with open('day12Input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

content = [x.strip() for x in content]
aplaces = []
goal = ()
map = []
start = []
for y in content:
    row = []
    for x in y:
        if x == 'E':
            goal = (len(map), len(row))
        if x == 'S':
            start = [len(map), len(row)]
            row.append('a')
        else:
            row.append(x)

        if row[len(row) - 1] == 'a':
            aplaces.append([len(map), len(row) - 1])

    map.append(row)


answers = {}

movement = [[0,1], [1, 0], [-1, 0], [0, -1]]

for startPlace in aplaces:

    been = {(startPlace[0], startPlace[1]): 0}

    places = [(startPlace, 0)]

    while len(places) > 0:
        place = places.pop(0)
        curr_height = map[place[0][0]][place[0][1]]

        for i, y in movement:
            position = [place[0][0] + i, place[0][1] + y]
            if 0 <= position[0] < len(map) and 0 <= position[1] < len(map[0]):

                position_height = map[position[0]][position[1]]
                if position_height == 'E':
                    if curr_height == 'z' or curr_height == 'y':
                        answers[(startPlace[0], startPlace[1])] = place[1] + 1
                        places.clear()
                        break

                elif ord(position_height) - ord(curr_height) <= 1:
                    if been.setdefault((position[0], position[1]), 99999999) > place[1] + 1:
                        places.append(([position[0], position[1]], place[1] + 1))
                        been[(position[0], position[1])] = place[1] + 1

        places.sort(key=lambda tup: tup[1])


print('part 1: ' + str(answers[(start[0], start[1])]))

print('part 2 ' + str(answers[min(answers, key=answers.get)]))