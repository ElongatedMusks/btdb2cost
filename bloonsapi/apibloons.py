t = open('bloonsapi/monkeycosts.txt','r')
api = t.readlines()
s = []

for i in range(len(api)):
    s.append(api[i].split())

def towerindex(tower):
    for i in range(len(s)):
        if tower == s[i][0]:
            ti = i
            break
    return ti

def upgradecost(tower, p1, p2, p3):
    if p1 != 0:
        ti = towerindex(tower) + 1
        return int(s[ti][p1])
    elif p2 != 0:
        ti = towerindex(tower) + 2
        return int(s[ti][p2])
    elif p3 != 0:
        ti = towerindex(tower) + 3
        return int(s[ti][p3])
    else:
        return int(s[towerindex(tower)][1])

def totalcost(tower, p1, p2, p3):
    cost = upgradecost(tower, 0, 0, 0)
    if p1 != 0:
        for i in list(range(p1 + 1)):
            if i != 0:
                cost = cost + upgradecost(tower, i, 0, 0)
    if p2 != 0:
        for i in list(range(p2 + 1)):
            if i != 0:
                cost = cost + upgradecost(tower, 0, i, 0)
    if p3 != 0:
        for i in list(range(p3 + 1)):
            if i != 0:
                cost = cost + upgradecost(tower, 0, 0, i)
    return cost

