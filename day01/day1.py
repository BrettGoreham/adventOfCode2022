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
print('part 1: ' + str(max(list)))


top = max(list)
list.remove(top)
second = max(list)
list.remove(second)
third = max(list)

print('part 2: ' + str(top + second + third))
