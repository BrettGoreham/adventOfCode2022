with open('day8Input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

rows = []

for y in content:
    row = []
    for x in y:
        row.append(int(x))

    rows.append(row)


visible = set()
for y in range(len(rows)):
    currentMax = -5
    for x in range(len(rows[0])):
        if(rows[y][x])  > currentMax:
            visible.add((x, y))
            currentMax = rows[y][x]

for y in range(len(rows)):
    currentMax = -5
    for x in reversed(range(len(rows[0]))):
        if(rows[y][x]) > currentMax:
            visible.add((x, y))
            currentMax = rows[y][x]

for x in range(len(rows[0])):
    currentMax = -5
    for y in range(len(rows)):
        if(rows[y][x]) > currentMax:
            visible.add((x, y))
            currentMax = rows[y][x]

for x in range(len(rows[0])):
    currentMax = -5
    for y in reversed(range(len(rows))):
        if(rows[y][x]) > currentMax:
            visible.add((x, y))
            currentMax = rows[y][x]

print(visible)
print(len(visible))

highestTotal = -5
index = (-5,-5)


for y in range(len(rows)):
    for x in range(len(rows[0])):

        tree = rows[y][x]
        up = 0
        down = 0
        right = 0
        left = 0
        # up
        count = 0
        while x - count > 0:
            count += 1

            if rows[y][x-count] >= tree:
                break


        up += count

        count = 0
        while x + count < len(rows) - 1:
            count += 1

            if rows[y][x + count] >= tree:
                break


        down += count
        count = 0
        while y - count > 0:
            count += 1

            if rows[y - count][x] >= tree:
                break


        left += count
        count = 0
        while y + count < len(rows) - 1:
            count += 1

            if rows[y + count][x] >= tree:
                break

        right += count

        total = up * right * left * down
        if total > highestTotal:
            highestTotal = total
            index = (x,y)


print(index)
print(highestTotal)