import re

with open('day6Input.txt') as f:
    content = f.readlines()


content = content[0]



buffer = list(content[0:3])

for x in range(3, len(content)):
    buffer.append(content[x])

    if(buffer[0] != buffer[1] and buffer[0] != buffer[2] and buffer[0] != buffer[3] and buffer[1] != buffer[2] and buffer[1] != buffer[3] and buffer[2] != buffer[3]):
        print(x + 1)
        break

    buffer.remove(buffer[0])


buffer = list(content[0:13])

for x in range(13, len(content)):
    buffer.append(content[x])

    charset = set(buffer)
    if len(charset) == 14:
        print(x + 1)
        break

    buffer.remove(buffer[0])