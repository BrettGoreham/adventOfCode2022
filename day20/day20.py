with open('day20Input.txt') as f:
    content = f.readlines()
content = [int(x.strip()) for x in content]


class IntHolder:
    def __init__(self, i):
        self.val = i


orderedList = []
MoveOrder = []

part2MoveOrder = []
part2OrderedList = []
for x in content:
    obj = IntHolder(x)
    orderedList.append(obj)
    MoveOrder.append(obj)

    part2 = IntHolder(x * 811589153)
    part2MoveOrder.append(part2)
    part2OrderedList.append(part2)

lengthOfList = len(MoveOrder)


def positive_find_new_index(_index, _val, list_length):
    while _val > 0:
        _index += 1
        if _index == list_length:
            _index = 1
        _val -= 1
    return _index


def with_modulus(_index, _val, list_length):
    _val = _val % (list_length -1)
    return positive_find_new_index(_index, _val, list_length)


def do_moves_x_times(ordered_list, move_order, x):
    for i in range(x):
        for obj in move_order:
            move_count = obj.val
            curr_index = ordered_list.index(obj)

            new_index = with_modulus(curr_index, move_count, lengthOfList)

            if new_index != curr_index:
                ordered_list.remove(obj)
                ordered_list.insert(new_index, obj)


def find_x_thousands_after_zero(ordered_list):
    found = False
    thousand_index = 0
    two_thousand_index = 0
    three_thousand_index = 0

    index = 0
    count = 0
    start_count = False
    while not found:
        if not start_count:
            if ordered_list[index].val == 0:
                start_count = True
            else:
                index += 1

        else:
            index = (index + 1) % lengthOfList

            count += 1
            if count == 1000:
                thousand_index = ordered_list[index].val
            if count == 2000:
                two_thousand_index = ordered_list[index].val
            if count == 3000:
                three_thousand_index = ordered_list[index].val
                found = True

    return thousand_index, two_thousand_index, three_thousand_index


do_moves_x_times(orderedList, MoveOrder, 1)
thou, twothou, threethou = find_x_thousands_after_zero(orderedList)
print('part 1: ' + str(thou + twothou + threethou))


do_moves_x_times(part2OrderedList, part2MoveOrder, 10)
thou, twothou, threethou = find_x_thousands_after_zero(part2OrderedList)
print('part 2: ' + str(thou + twothou + threethou))