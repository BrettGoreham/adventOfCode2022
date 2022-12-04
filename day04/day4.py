with open('day4Input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

contains = 0
overlap = 0
for c in content:
    pairs = c.split(',')

    first = pairs[0].split('-')
    second = pairs[1].split('-')

    if (int(first[0]) <= int(second[0]) and int(first[1]) >= int(second[1])) or (int(second[0]) <= int(first[0]) and int(second[1]) >= int(first[1])):
        contains += 1

    if int(second[0]) <= int(first[0]) <= int(second[1]) or (int(second[0]) <= int(first[1]) <= int(second[1])) or \
            int(first[0]) <= int(second[0]) <= int(first[1]) or (int(first[0]) <= int(second[1]) <= int(first[1])):
        overlap += 1


print(contains)
print(overlap)
