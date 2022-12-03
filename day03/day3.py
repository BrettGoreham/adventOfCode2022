import re


def get_answer(answer_list):
    priority_answer = 0
    for character in answer_list:
        if re.search('[a-z]', character):
            priority_answer += ord(character) - ord('a') + 1
        else:
            priority_answer += ord(character) - ord('A') + 1 + 26
    return priority_answer


with open('day3Input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

priority = []
for c in content:
    half = int(len(c)/2)
    priority.append(set(c[0:half]).intersection(c[half:len(c)]).pop())

print('part 1: ' + str(get_answer(priority)))

badges, elfnum = [], 0
while elfnum < len(content):

    groupBadge = set(content[elfnum])\
                        .intersection(content[elfnum+1])\
                        .intersection(content[elfnum+2]).pop()
    badges.append(groupBadge)
    elfnum += 3

print('part 2: ' + str(get_answer(badges)))
