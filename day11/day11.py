with open('day11Input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]


class Monkey:
    def __init__(self, items, operation, operand, divisible_by, true, false):
        self.items = items
        self.operation = operation
        self.operand = operand
        self.divisible = divisible_by
        self.true = true
        self.false = false
        self.inspected = 0


def get_inspected(monkey):
    return monkey.inspected

monkeys = []

monkeys.append(Monkey([54, 98, 50, 94, 69, 62, 53, 85], '*', 13, 3, 2, 1))
monkeys.append(Monkey([71, 55, 82], '+', 2, 13, 7, 2))
monkeys.append(Monkey([77, 73, 86, 72, 87], '+', 8, 19, 4, 7))
monkeys.append(Monkey([97, 91], '+', 1, 17, 6, 5))
monkeys.append(Monkey([78, 97, 51, 85, 66, 63, 62], '*', 17, 5, 6, 3))
monkeys.append(Monkey([88], '+', 3, 7, 1, 0))
monkeys.append(Monkey([87, 57, 63, 86, 87, 53], '*', -1, 11, 5, 0))
monkeys.append(Monkey([73, 59, 82, 65], '+', 6, 2, 4, 3))

for x in range(20):
    for monkey in monkeys:
        operand = monkey.operand

        while len(monkey.items) > 0:
            item = monkey.items.pop(0)
            monkey.inspected += 1

            if monkey.operand == -1:
                operand = item

            if monkey.operation == '+':
                item += operand
            else:
                item *= operand

            item = int(item / 3)

            if item % monkey.divisible == 0:
                monkeys[monkey.true].items.append(item)
            else:
                monkeys[monkey.false].items.append(item)

print('part 1')
for monkey in monkeys:
    print(monkey.inspected)

monkeys.sort(key=get_inspected, reverse=True)
print('part 1 answer : ' + str(monkeys[0].inspected * monkeys[1].inspected))


monkeys = []

monkeys.append(Monkey([54, 98, 50, 94, 69, 62, 53, 85], '*', 13, 3, 2, 1))
monkeys.append(Monkey([71, 55, 82], '+', 2, 13, 7, 2))
monkeys.append(Monkey([77, 73, 86, 72, 87], '+', 8, 19, 4, 7))
monkeys.append(Monkey([97, 91], '+', 1, 17, 6, 5))
monkeys.append(Monkey([78, 97, 51, 85, 66, 63, 62], '*', 17, 5, 6, 3))
monkeys.append(Monkey([88], '+', 3, 7, 1, 0))
monkeys.append(Monkey([87, 57, 63, 86, 87, 53], '*', -1, 11, 5, 0))
monkeys.append(Monkey([73, 59, 82, 65], '+', 6, 2, 4, 3))

smallestCommonMultiple = 1
for monkey in monkeys:
    smallestCommonMultiple *= monkey.divisible

for x in range(10000):
    for monkey in monkeys:
        operand = monkey.operand

        while len(monkey.items) > 0:
            item = monkey.items.pop(0)
            monkey.inspected += 1

            if monkey.operand == -1:
                operand = item

            if monkey.operation == '+':
                item += operand
            else:
                item *= operand

            item = item % smallestCommonMultiple

            if item % monkey.divisible == 0:
                monkeys[monkey.true].items.append(item)
            else:
                monkeys[monkey.false].items.append(item)


print('\npart 2 after 10000 round ')
for monkey in monkeys:
    print(monkey.inspected)

monkeys.sort(key=get_inspected, reverse=True)
print('part 2 answer : ' + str(monkeys[0].inspected * monkeys[1].inspected))
