with open('day7Input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]


directories = {}
current = ''


for c in content:
    line = c.split(' ')
    if line[0] == '$' and line[1] == 'cd':
        if line[2] == '..':
            current = current[0:current.rindex('/')]
            if len(current) == 0:
                current = '/'
        elif len(current) == 1:
            current += line[2]
        elif len(current) != 0:
            current += '/' + line[2]
        else:
            current += line[2]
        directories.setdefault(current, 0)

    if line[0].isdigit():
        directories[current] += int(line[0])

sizemap = {}
total = 0
for x in directories.keys():
    count = 0
    for y in directories.keys():
        if y.startswith(x):
            count += directories[y]
    if count <= 100000:
        total += count

    sizemap[x] = count


freespace = 40000000
used = sizemap['/']

works = 0
for w in sorted(sizemap, key=sizemap.get):
    if used - sizemap[w] <= freespace:
        works = sizemap[w]
        break


print(total)
print(works)