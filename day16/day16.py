import re
import copy

with open('day16Input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

check = {'res': (0,0)}

location_to_flowrate_paths = {}
valuedFlows = []
for c in content:
    result = re.search('Valve ([A-Z]{2}) has flow rate=([0-9]{1,2})', c)
    name = result.group(1)
    flow_rate = int(result.group(2))

    if 'valves' in c:
        paths = c.split('valves ')[1].split(', ')
    else:
        paths = [c.split('to valve ')[1]]

    location_to_flowrate_paths[name] = (flow_rate, paths)
    if flow_rate > 0 or name == 'AA':
        valuedFlows.append(name)


maxflow = 0
hoptions = {}
for x in valuedFlows:
    minsToValue = {}
    been = {x: 0}
    maxflow += location_to_flowrate_paths[x][0]
    locationsToTravel = [(x, 0)]

    while len(locationsToTravel) > 0:
        location = locationsToTravel.pop(0)
        hops = location_to_flowrate_paths[location[0]][1]

        for hop in hops:
            if hop not in been or been[hop] > location[1]:
                locationsToTravel.append([hop, location[1] + 1])
                been[hop] = location[1] + 1

        locationsToTravel.sort(key=lambda tup: tup[1])

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
            new_flow = current_flow + location_to_flowrate_paths[loc][0]

            newLocations = copy.deepcopy(open_locations)
            newLocations.append(loc)

            hopTo30(steps, new_flow, newLocations, new_total_flow)



hopTo30(30, 0, ['AA'], 0)
results.sort(reverse=True)

print(results[0])


def hopTo26(steps_remaining, current_flow, open_locations, partner_goal, steps_to_partner_goal, total_flow):

    if not total_flow + (steps_remaining * maxflow) < check['res'][0]:
        location = open_locations[-1]
        avail_goals = list(filter(lambda z: z not in open_locations and partner_goal != z and hoptions[location][z] < steps_remaining, hoptions[location]))

        if len(avail_goals) == 0:
            while steps_remaining > 0:
                total_flow += current_flow
                steps_to_partner_goal -= 1
                steps_remaining -= 1
                if steps_to_partner_goal == -1:
                    current_flow += location_to_flowrate_paths[partner_goal][0]
                    open_locations.append(partner_goal)
                    avail_goals = list(filter(lambda z: z not in open_locations and hoptions[partner_goal][z] < steps_remaining, hoptions[partner_goal]))
                    for x in avail_goals:
                        hopTo26(steps_remaining, current_flow, copy.deepcopy(open_locations), x, hoptions[partner_goal][x], total_flow)


            if total_flow > check['res'][0]:
                print('new high: ' + str(total_flow))
                check['res'] = (total_flow, open_locations)
        else:
            for goal in avail_goals:
                steps_to_goal = hoptions[location][goal]

                if steps_to_goal < steps_to_partner_goal:

                    steps = steps_remaining
                    steps -= steps_to_goal
                    new_total_flow = total_flow + (current_flow * steps_to_goal)

                    #open
                    steps -= 1
                    new_total_flow += current_flow
                    new_flow = current_flow + location_to_flowrate_paths[goal][0]

                    new_locations = copy.deepcopy(open_locations)
                    new_locations.append(goal)

                    hopTo26(steps, new_flow, new_locations, partner_goal, steps_to_partner_goal - (steps_to_goal + 1), new_total_flow)

                if steps_to_partner_goal < steps_to_goal:
                    if partner_goal == 'AA':
                        hopTo26(steps_remaining, current_flow, open_locations, goal, steps_to_goal, total_flow)
                    else:
                        steps = steps_remaining
                        steps -= steps_to_partner_goal
                        new_total_flow = total_flow + (current_flow * steps_to_partner_goal)

                        #open
                        steps -= 1
                        new_total_flow += current_flow
                        new_flow = current_flow + location_to_flowrate_paths[partner_goal][0]

                        new_locations = copy.deepcopy(open_locations)
                        new_locations.append(partner_goal)
                        hopTo26(steps, new_flow, new_locations, goal, steps_to_goal - (steps_to_partner_goal + 1), new_total_flow)

                if steps_to_partner_goal == steps_to_goal:
                    steps = steps_remaining
                    steps -= steps_to_goal
                    new_total_flow = total_flow + (current_flow * steps_to_goal)

                    # open
                    steps -= 1
                    new_total_flow += current_flow
                    new_flow = current_flow + location_to_flowrate_paths[goal][0] + location_to_flowrate_paths[partner_goal][0]
                    new_locations = copy.deepcopy(open_locations)
                    new_locations.append(goal)
                    new_locations.append(partner_goal)

                    avail_goals = list(filter(lambda z: z not in new_locations and hoptions[goal][z] < steps, hoptions[goal]))
                    for b in avail_goals:
                        hopTo26(steps, new_flow, new_locations, b, hoptions[goal][b], new_total_flow)



hopTo26(26, 0, ['AA'], 'AA', 0, 0)


print(check['res'][0])
print(check['res'][1])





