import re
import copy

with open('day16Input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

check = {'res': (0,0)}

stuff = {}
valuedFlows = []
for c in content:
    result = re.search('Valve ([A-Z]{2}) has flow rate=([0-9]{1,2})', c)
    name = result.group(1)
    flow_rate = int(result.group(2))

    if 'valves' in c:
        paths = c.split('valves ')[1].split(', ')
    else:
        paths = [c.split('to valve ')[1]]

    stuff[name] = (flow_rate, paths)
    if flow_rate > 0 or name == 'AA':
        valuedFlows.append(name)


maxflow = 0
hoptions = {}
for x in valuedFlows:
    minsToValue = {}
    been = {x: 0}
    maxflow+= stuff[x][0]
    places = [(x, 0)]

    while len(places) > 0:
        place = places.pop(0)
        hops = stuff[place[0]][1]

        for hop in hops:
            if hop not in been or been[hop] > place[1]:
                places.append([hop, place[1] + 1])
                been[hop] = place[1] + 1

        places.sort(key=lambda tup: tup[1])

    hoptions[x] = {k: v for k, v in been.items() if k in valuedFlows and k != x}


results = []
def hopTo30(steps_remaining, current_flow, open_locations, total_flow):
    location = open_locations[-1]

    a = list(filter(lambda z: z not in open_locations and hoptions[location][z] + 1 <= steps_remaining, hoptions[location]))

    if len(a) == 0:
        total_flow += steps_remaining * current_flow
        results.append(total_flow)
    else:
        for option in a:
            loc = option
            steps_used = hoptions[location][option]
            steps = steps_remaining
            steps -= steps_used
            new_total_flow = total_flow + (current_flow * steps_used)

            #open
            steps -= 1
            new_total_flow += current_flow
            new_flow = current_flow + stuff[loc][0]

            newLocations = copy.deepcopy(open_locations)
            newLocations.append(loc)

            hopTo30(steps, new_flow, newLocations, new_total_flow)



hopTo30(30, 0, ['AA'], 0)
results.sort(reverse=True)

print(results[0])


def hopTo26(steps_remaining, current_flow, open_locations, partnerGoal, stepsToGoal, total_flow):
    if not total_flow + (steps_remaining * maxflow) < check['res'][0]:
        location = open_locations[-1]
        a = list(filter(lambda z: z not in open_locations and partnerGoal != z and hoptions[location][z] + 1 <= steps_remaining, hoptions[location]))

        if len(a) == 0:
            while steps_remaining > 0:
                total_flow += current_flow
                stepsToGoal -= 1
                if stepsToGoal == -1:
                    current_flow += stuff[partnerGoal][0]
                    open_locations.append(partnerGoal)
                steps_remaining -= 1

            if total_flow > check['res'][0]:
                print('new high: ' + str(total_flow))
                check['res'] = (total_flow, open_locations)
        else:
            for option in a:
                steps_used = hoptions[location][option]

                if steps_used < stepsToGoal:

                    steps = steps_remaining
                    steps -= steps_used
                    new_total_flow = total_flow + (current_flow * steps_used)

                    #open
                    steps -= 1
                    new_total_flow += current_flow
                    new_flow = current_flow + stuff[option][0]

                    new_locations = copy.deepcopy(open_locations)
                    new_locations.append(option)

                    hopTo26(steps, new_flow, new_locations, partnerGoal, stepsToGoal - (steps_used + 1), new_total_flow)

                if stepsToGoal < steps_used:
                    if partnerGoal == 'AA':
                        hopTo26(steps_remaining, current_flow, open_locations, option, steps_used, total_flow)
                    else:
                        steps = steps_remaining
                        steps -= stepsToGoal
                        new_total_flow = total_flow + (current_flow * stepsToGoal)

                        #open
                        steps -= 1
                        new_total_flow += current_flow
                        new_flow = current_flow + stuff[partnerGoal][0]

                        new_locations = copy.deepcopy(open_locations)
                        new_locations.append(partnerGoal)
                        hopTo26(steps, new_flow, new_locations, option, steps_used - (stepsToGoal + 1), new_total_flow)

                if stepsToGoal == steps_used:
                    steps = steps_remaining
                    steps -= steps_used
                    new_total_flow = total_flow + (current_flow * steps_used)

                    # open
                    steps -= 1
                    new_total_flow += current_flow
                    new_flow = current_flow + stuff[option][0] + stuff[partnerGoal][0]
                    new_locations = copy.deepcopy(open_locations)
                    new_locations.append(partnerGoal)
                    new_locations.append(option)

                    a = list(filter(lambda z: z not in new_locations and hoptions[partnerGoal][z] + 1 <= steps, hoptions[partnerGoal]))
                    for b in a:
                        hopTo26(steps, new_flow, new_locations, b, hoptions[partnerGoal][b], new_total_flow)



hopTo26(26, 0, ['AA'], 'AA', 0, 0)


print(check['res'][0])
print(check['res'][1])





