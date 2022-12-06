import re

with open('day6Input.txt') as f:
    content = f.readlines()


content = content[0]

buffer = list(content[0:3])

for x in range(3, len(content)):
    buffer.append(content[x])

    if buffer[0] != buffer[1] and buffer[0] != buffer[2] and buffer[0] != buffer[3] and buffer[1] != buffer[2] and buffer[1] != buffer[3] and buffer[2] != buffer[3]:
        print(x + 1)
        break

    buffer.remove(buffer[0])


buffer = list(content[0:13])

for x in range(13, len(content)):
    buffer.append(content[x])

    if buffer[0] != buffer[1] and buffer[0] != buffer[2] and buffer[0] != buffer[3] and buffer[0] != buffer[4] and buffer[0] != buffer[5] and buffer[0] != buffer[6] and buffer[0] != buffer[7] and buffer[0] != buffer[8] and buffer[0] != buffer[9] and buffer[0] != buffer[10] and buffer[0] != buffer[11] and buffer[0] != buffer[12] and buffer[0] != buffer[13] and buffer[1] != buffer[2] and buffer[1] != buffer[3] and buffer[1] != buffer[4] and buffer[1] != buffer[5] and buffer[1] != buffer[6] and buffer[1] != buffer[7] and buffer[1] != buffer[8] and buffer[1] != buffer[9] and buffer[1] != buffer[10] and buffer[1] != buffer[11] and buffer[1] != buffer[12] and buffer[1] != buffer[13] and buffer[2] != buffer[3] and buffer[2] != buffer[4] and buffer[2] != buffer[5] and buffer[2] != buffer[6] and buffer[2] != buffer[7] and buffer[2] != buffer[8] and buffer[2] != buffer[9] and buffer[2] != buffer[10] and buffer[2] != buffer[11] and buffer[2] != buffer[12] and buffer[2] != buffer[13] and buffer[3] != buffer[4] and buffer[3] != buffer[5] and buffer[3] != buffer[6] and buffer[3] != buffer[7] and buffer[3] != buffer[8] and buffer[3] != buffer[9] and buffer[3] != buffer[10] and buffer[3] != buffer[11] and buffer[3] != buffer[12] and buffer[3] != buffer[13] and buffer[4] != buffer[5] and buffer[4] != buffer[6] and buffer[4] != buffer[7] and buffer[4] != buffer[8] and buffer[4] != buffer[9] and buffer[4] != buffer[10] and buffer[4] != buffer[11] and buffer[4] != buffer[12] and buffer[4] != buffer[13] and buffer[5] != buffer[6] and buffer[5] != buffer[7] and buffer[5] != buffer[8] and buffer[5] != buffer[9] and buffer[5] != buffer[10] and buffer[5] != buffer[11] and buffer[5] != buffer[12] and buffer[5] != buffer[13] and buffer[6] != buffer[7] and buffer[6] != buffer[8] and buffer[6] != buffer[9] and buffer[6] != buffer[10] and buffer[6] != buffer[11] and buffer[6] != buffer[12] and buffer[6] != buffer[13] and buffer[7] != buffer[8] and buffer[7] != buffer[9] and buffer[7] != buffer[10] and buffer[7] != buffer[11] and buffer[7] != buffer[12] and buffer[7] != buffer[13] and buffer[8] != buffer[9] and buffer[8] != buffer[10] and buffer[8] != buffer[11] and buffer[8] != buffer[12] and buffer[8] != buffer[13] and buffer[9] != buffer[10] and buffer[9] != buffer[11] and buffer[9] != buffer[12] and buffer[9] != buffer[13] and buffer[10] != buffer[11] and buffer[10] != buffer[12] and buffer[10] != buffer[13] and buffer[11] != buffer[12] and buffer[11] != buffer[13] and buffer[12] != buffer[13]:
        print(x + 1)
        break

    buffer.remove(buffer[0])

