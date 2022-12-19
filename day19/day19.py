import math
import re
with open('day19Input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]


class Blueprint:
    def __init__(self, id, ore, clay, obsidian, geode):
        self.id = id
        self.ore = ore
        self.clay = clay
        self.obsidian = obsidian
        self.geode = geode

    def print(self, geods):
        print('blueprint: ' + str(self.id) + '  geodes: ' + str(geods))





possible_actions = ['skip', 'ore', 'clay', 'ob', 'g']
def check_if_possible(blueprint: Blueprint, action,resources):
    if action == 'skip':
        return True
    if action == 'ore':
        return blueprint.ore <= resources[0]
    if action == 'clay':
        return blueprint.clay <= resources[0]
    if action == 'ob':
        return blueprint.obsidian[0] <= resources[0] and blueprint.obsidian[1] <= resources[1]
    if action == 'g':
        return blueprint.geode[0] <= resources[0] and blueprint.geode[1] <= resources[2]





def get_max_geodes(blueprint: Blueprint, stop_before,  minute, resources, robots):

    if (minute, resources, robots) in seen:
        return 0
    else:
        seen.add((minute, resources, robots))

    if geodesAtIndex[stop_before] - resources[3] >= ((stop_before - minute) * (2 * robots[3] + stop_before - minute - 1)) // 2:
        return 0

    geodesAtIndex.setdefault(minute, 0)
    if geodesAtIndex[minute] < resources[3]:
        geodesAtIndex[minute] = resources[3]


    if minute == stop_before:
        return resources[3]

    actions = []
    for action in possible_actions:
        if check_if_possible(blueprint, action, resources):
            actions.append(action)

    new_resources = (resources[0] + robots[0], resources[1] + robots[1], resources[2] + robots[2], resources[3] + robots[3])
    answers = set()

    if 'g' in actions:
        geode_resources = (new_resources[0] - blueprint.geode[0], new_resources[1], new_resources[2] - blueprint.geode[1], new_resources[3])
        answers.add(get_max_geodes(blueprint, stop_before, minute + 1, geode_resources, (robots[0], robots[1], robots[2], robots[3] + 1)))
    if 'ob' in actions and robots[2] != max_ob_cost and 'g' not in actions:
        obsidian_resources = (new_resources[0] - blueprint.obsidian[0], new_resources[1] - blueprint.obsidian[1], new_resources[2], new_resources[3])
        answers.add(get_max_geodes(blueprint, stop_before, minute + 1, obsidian_resources, (robots[0], robots[1], robots[2] + 1, robots[3])))
    if 'ore' in actions and robots[0] != max_ore_cost and 'g' not in actions:
        ore_resources = (new_resources[0] - blueprint.ore, new_resources[1], new_resources[2], new_resources[3])
        answers.add(get_max_geodes(blueprint, stop_before, minute + 1, ore_resources, (robots[0] + 1, robots[1], robots[2], robots[3])))
    if 'clay' in actions and robots[1] != max_clay_cost and 'g' not in actions:
        clay_resources = (new_resources[0] - blueprint.clay, new_resources[1], new_resources[2], new_resources[3])
        answers.add(get_max_geodes(blueprint, stop_before, minute + 1, clay_resources, (robots[0], robots[1] + 1, robots[2], robots[3])))

    # no action
    if 'g' not in actions:
        answers.add(get_max_geodes(blueprint, stop_before, minute + 1, new_resources, robots))
    return max(answers)



geodeCounts = []
max_ore_cost = 0
max_clay_cost = 0
seen = set()

for c in content:
    # Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.

    result = re.search('Blueprint ([0-9]{1,2}): Each ore robot costs ([0-9]{1,2}) ore. Each clay robot costs ([0-9]{1,2}) ore. Each obsidian robot costs ([0-9]{1,2}) ore and ([0-9]{1,2}) clay. Each geode robot costs ([0-9]{1,2}) ore and ([0-9]{1,2}) obsidian', c)

    blueprint = Blueprint(int(result.group(1)), int(result.group(2)), int(result.group(3)), (int(result.group(4)), int(result.group(5))), (int(result.group(6)), int(result.group(7))))

    max_ore_cost = max(blueprint.clay, blueprint.geode[0], blueprint.obsidian[0])
    max_clay_cost = blueprint.obsidian[1]
    max_ob_cost = blueprint.geode[1]
    ore_robots = 1
    clay_robots = 0
    obsidian_robots = 0
    geodes_robots = 0

    minutes = 1

    clay = 0
    ore = 0
    obsidian = 0
    geodes = 0

    seen = set()
    geodesAtIndex = {}
    geodesAtIndex.setdefault(25, 0)
    geodesAtIndex.setdefault(33, 0)

    geodes = get_max_geodes(blueprint, 25, 1, (ore, clay, obsidian, geodes), (ore_robots, clay_robots, obsidian_robots, geodes_robots))
    blueprint.print(geodes)
    geodeCounts.append(geodes)


answer = 0
for i in range(1, len(geodeCounts) + 1):
    answer += i * geodeCounts[i - 1]

print('part 1: ' + str(answer))


geodeCounts = []
max_ore_cost = 0
max_clay_cost = 0
seen = set()

for c in content[0:3]:
    # Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.

    result = re.search('Blueprint ([0-9]{1,2}): Each ore robot costs ([0-9]{1,2}) ore. Each clay robot costs ([0-9]{1,2}) ore. Each obsidian robot costs ([0-9]{1,2}) ore and ([0-9]{1,2}) clay. Each geode robot costs ([0-9]{1,2}) ore and ([0-9]{1,2}) obsidian', c)

    blueprint = Blueprint(int(result.group(1)), int(result.group(2)), int(result.group(3)), (int(result.group(4)), int(result.group(5))), (int(result.group(6)), int(result.group(7))))

    max_ore_cost = max(blueprint.clay, blueprint.geode[0], blueprint.obsidian[0])
    max_clay_cost = blueprint.obsidian[1]
    max_ob_cost = blueprint.geode[1]
    ore_robots = 1
    clay_robots = 0
    obsidian_robots = 0
    geodes_robots = 0

    minutes = 1

    clay = 0
    ore = 0
    obsidian = 0
    geodes = 0

    seen = set()
    geodesAtIndex = {}
    geodesAtIndex.setdefault(25, 0)
    geodesAtIndex.setdefault(33, 0)

    geodes = get_max_geodes(blueprint, 33, 1, (ore, clay, obsidian, geodes), (ore_robots, clay_robots, obsidian_robots, geodes_robots))
    blueprint.print(geodes)
    geodeCounts.append(geodes)


print('part 1: ' + str(geodeCounts[0] * geodeCounts[1] * geodeCounts[2]))
