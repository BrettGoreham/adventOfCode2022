string = ''

for x in range(14):
    for y in range(x + 1, 14):
        if x == y:
            continue
        else:
            if len(string) > 0:
                string += ' and '

            string += f'buffer[{x}] != buffer[{y}]'

print(string)