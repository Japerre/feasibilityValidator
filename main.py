import json

def checkDomains(timePoints, solutions):
    solutionsCopy = solutions[:]
    for t in timePoints:
        for s in solutionsCopy:
            if s.get('id') == t.get('id'):
                for index, d in enumerate(t.get('domains')):
                    if d.get('l') <= s.get('solution') <= d.get('u'):
                        solutionsCopy.remove(s)
                        break
                    elif index+1 == len(t.get('domains')):
                        return False
    return True


def checkConstraints(constraints, solutions):
    for c in constraints:
        string = c.split()
        t_i = int(string[0])
        t_j = int(string[1])
        w_ij = int(string[2])

        s_i = 0
        s_j = 0
        for s in solutions:
            if s.get('id') == t_i:
                s_i = s.get('solution')
            elif s.get('id') == t_j:
                s_j = s.get('solution')

        if s_i - s_j > w_ij:
            return False

    return True

f = open(
    'C:/Users/tibol/Desktop/FIIW Tibo Laperre/fase 4 - master/MASTERPROEF/feasibility algorithm/feasibilityAlgo/solutions/inc-1_sol.json')

instance = json.load(f)
f.close()
nTimePoints = instance['num-variables']
nArcs = instance['num-constraints']
timePoints = instance['variables']
constraints = instance['constraints']
solutions = instance['solutions']

feasible = checkDomains(timePoints, solutions)
print(feasible)
feasible = checkConstraints(constraints, solutions)
print(feasible)
