with open('day1Input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

list = []

count = 0
for c in content:
    if c == '':
        list.append(count)
        count = 0
    else:
        count += int(c)

list.sort(reverse=True)
print('part 1: ' + str(list[0]))
print('part 2: ' + str(list[0] + list[1] + list[2]))
