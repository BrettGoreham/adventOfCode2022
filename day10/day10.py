with open('day10Input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

cycleChecks = [20, 60, 100, 140, 180, 220]
pixels = []
sum = 0
cycle = 0
x = 1
for c in content:
    cycle += 1
    if x <= cycle % 40 <= x + 2:
        pixels.append('▮')
    else:
        pixels.append('▯')
    if cycle in cycleChecks:
        sum += cycle * x
    line = c.split(' ')
    if line[0] != 'noop':
        cycle += 1
        if x <= cycle % 40 <= x + 2:
            pixels.append('▮')
        else:
            pixels.append('▯')
        if cycle in cycleChecks:
            sum += cycle * x
        x += int(line[1])


print('part 1: ' + str(sum))

print('part 2: find 7 capital letters in picture')
s = ''
for x in range(240):
    if x != 0 and x % 40 == 0:
        print(s)
        s = ''
    s += pixels[x]
print(s)
