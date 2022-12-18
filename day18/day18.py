with open('day18Input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]


maxx = 0
maxy = 0
maxz = 0
cubes = []
for c in content:
    string_cube = c.split(',')
    cube =(int(string_cube[0]), int(string_cube[1]), int(string_cube[2]))
    cubes.append(cube)
    if int(cube[0]) >= maxx:
        maxx = cube[0]

    if int(cube[1]) >= maxy:
        maxy = cube[1]

    if int(cube[2]) >= maxz:
        maxz = cube[2]

maxx +=2
maxz +=2
maxy +=2

moves = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

sidesFree = 0
for cube in cubes:
    for move in moves:
        xyz = (cube[0] + move[0], cube[1] + move[1], cube[2] + move[2])

        if xyz not in cubes:
            sidesFree += 1

print('part 1 exposed sides: ' + str(sidesFree))


checkAround = [(0, 0, 0)]
air = set()
seen = set()
ans = 0
while len(checkAround) > 0:
    check = checkAround.pop()

    if check not in cubes:
        air.add(check)
        for move in moves:
            xyz = (check[0] + move[0], check[1] + move[1], check[2] + move[2])
            if -1 <= xyz[0] < maxx and -1 <= xyz[1] < maxy and -1 <= xyz[2] < maxz:
                if xyz in cubes:
                    ans += 1
                if xyz not in air and xyz not in checkAround:
                    checkAround.append(xyz)

print('part2 lava reachable sides: ' + str(ans))
