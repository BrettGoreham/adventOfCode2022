import re

with open('day5Input.txt') as f:
    content = f.readlines()
content = [x.replace("\n", "") for x in content]


stacks = {}
count = 0
for c in content:
    if c[1] == '1':
        count += 2
        break
    groups = re.split(' ', c)
    groups = [x for x in groups if x]
    found = {}
    for group in groups:
        indexskip = found.setdefault(group, 0)
        indices = [s.start() for s in re.finditer(group, c)]
        index = indices[indexskip]
        column = int(index / 4 + 1)

        stack = stacks.setdefault(column, [])
        stack.insert(0, group[1])

        found[group] += 1
    count += 1

for c in content[count::]:
    moves = re.split(' ', c)
    for x in range(int(moves[1])):
        fra = stacks[int(moves[3])]

        stacks[int(moves[5])].append(fra.pop())

output = ''
for x in sorted(stacks):
    output += stacks[x][len(stacks[x]) - 1]

print(output)


stacks = {}
count = 0
for c in content:
    if c[1] == '1':
        count += 2
        break
    groups = re.split(' ', c)
    groups = [x for x in groups if x]
    found = {}
    for group in groups:
        indexskip = found.setdefault(group, 0)
        indices = [s.start() for s in re.finditer(group, c)]
        index = indices[indexskip]
        column = int(index / 4 + 1)

        stack = stacks.setdefault(column, [])
        stack.insert(0, group[1])

        found[group] += 1
    count += 1


for c in content[count::]:
    moves = re.split(' ', c)
    fra = stacks[int(moves[3])]
    moving = []

    for x in range(int(moves[1])):
        moving.insert(0, fra.pop())

    for x in moving:
        stacks[int(moves[5])].append(x)

output = ''
for x in sorted(stacks):
    output += stacks[x][len(stacks[x]) - 1]

print(output)

