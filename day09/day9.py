def print_visited_of_tail(steps, rope_length):
    rope = []
    for x in range(10):
        rope.append([0, 0])
    visited = set()
    visited.add((rope[rope_length-1][0], rope[rope_length-1][1]))

    for c in steps:
        direction, amount = c.split(' ')

        for i in range(int(amount)):
            if direction == 'R':
                rope[0][0] += 1
            elif direction == 'L':
                rope[0][0] -= 1
            elif direction == 'U':
                rope[0][1] += 1
            elif direction == 'D':
                rope[0][1] -= 1

            for x in range(1, rope_length):

                if not (rope[x - 1][0] - 1 <= rope[x][0] <= rope[x - 1][0] + 1 and rope[x - 1][1] - 1 <= rope[x][1] <=
                        rope[x - 1][1] + 1):
                    
                    if rope[x][0] != rope[x - 1][0]:
                        rope[x][0] += int((rope[x - 1][0] - rope[x][0]) / abs((rope[x - 1][0] - rope[x][0])))
                    if rope[x][1] != rope[x - 1][1]:
                        rope[x][1] += int((rope[x - 1][1] - rope[x][1]) / abs((rope[x - 1][1] - rope[x][1])))
                    if x == rope_length - 1:
                        visited.add((rope[x][0], rope[x][1]))

    return len(visited)


with open('day9Input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]
print('part 1: ' + str(print_visited_of_tail(content, 2)))
print('part 2: ' + str(print_visited_of_tail(content, 10)))
