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
                last_x, last_y = rope[x-1][0], rope[x-1][1]
                current = rope[x]
                if not (last_x - 1 <= current[0] <= last_x + 1 and last_y - 1 <= current[1] <= last_y + 1):
                    if current[0] != last_x:
                        current[0] += int((last_x - current[0]) / abs(last_x - current[0]))
                    if current[1] != last_y:
                        current[1] += int((last_y - current[1]) / abs(last_y - current[1]))

                    if x == rope_length - 1:
                        visited.add((current[0], current[1]))

    return len(visited)


with open('day9Input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]
print('part 1: ' + str(print_visited_of_tail(content, 2)))
print('part 2: ' + str(print_visited_of_tail(content, 10)))
