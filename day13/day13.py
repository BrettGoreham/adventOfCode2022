from functools import cmp_to_key

with open('day13Input.txt') as f:
    content = f.readlines()
content = [eval(x.strip()) for x in list(filter(lambda a: a.strip() != '', content))]


def check(list_left, list_right):
    index = 0
    while index < len(list_left):
        if index >= len(list_right):
            return -1

        left_val = list_left[index]
        right_val = list_right[index]

        if isinstance(left_val, int) and isinstance(right_val, int):
            if int(left_val) < int(right_val):
                return 1
            elif int(left_val) > int(right_val):
                return -1

        else:
            left_val = left_val if isinstance(left_val, list) else [left_val]
            right_val = right_val if isinstance(right_val, list) else [right_val]
            val = check(left_val, right_val)
            if val != 0:
                return val
        index += 1

    if len(list_right) > len(list_left):
        return 1
    else:
        return 0


x = 0

sum = 0
pair = 0
while x < len(content):
    pair += 1
    left = content[x]
    x += 1
    right = content[x]
    x += 1

    check_val = check(left, right)
    if 1 == check_val:
        sum += pair


print('part 1: ' + str(sum))

content.append([[2]])
content.append([[6]])
content.sort(key=cmp_to_key(check), reverse=True)

mult = (content.index([[2]]) + 1) * (content.index([[6]])+ 1)

print('part 2: ' + str(mult))

