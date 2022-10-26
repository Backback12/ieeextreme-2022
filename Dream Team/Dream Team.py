# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

# numpy and scipy are available for use
import numpy
# import scipy

max_budget = get_number()
positions = ['p', 'g', 's', 'f', 'c']
sal = {}

for pos in positions:
    playerCount = get_number()
    playerList = []
    for p in range(playerCount):
        player = get_word()
        salary = get_number()
        playerList.append({"name": player, "salary": salary})
        
    # playerList.sort(key=lambda x: x['salary'], reverse=True)
    
    sal[pos] = playerList



# curr = {'p': 0, 
#         'g': 0,
#         's': 0,
#         'f': 0,
#         'c': 0}
# diff = {'p': -1, 
#         'g': -1,
#         's': -1,
#         'f': -1,
#         'c': -1}


# budget = (sal['p'][0]['salary'] + 
#           sal['g'][0]['salary'] + 
#           sal['s'][0]['salary'] + 
#           sal['f'][0]['salary'] + 
#           sal['c'][0]['salary'])


bestTeam = []   # list of: names separated by space
bestBudget = -1 # closest budget to max budget

for p in sal['p']:
    for g in sal['g']:
        for s in sal['s']:
            for f in sal['f']:
                for c in sal['c']:
                    budget = p['salary'] + g['salary'] + s['salary'] + f['salary'] + c['salary']
                    if budget >= bestBudget and budget < max_budget:
                        if budget > bestBudget:
                            bestTeam = []
                            bestBudget = budget
                        bestTeam.append(p['name'] + " " + g['name'] + " " + s['name'] + " " + f['name'] + " " + c['name'])
                        # print(p['name'] + " " + g['name'] + " " + s['name'] + " " + f['name'] + " " + c['name'])

bestTeam.sort()
for name in bestTeam[0].split():
    print(name)

# while budget > max_budget:
    
#     # calculate differences to next player salary
#     for pos in positions:
#         if curr[pos] < len(sal[pos]) -1:
            
#             diff[pos] = sal[pos][curr[pos]]['salary'] - sal[pos][curr[pos]+1]['salary']
#         else:
#             diff[pos] = -1
            
#     # find smallest price dif
#     diffList = sorted(diff.items(), key=lambda x: x[1], reverse=False)
#     # also sort alphabetically for differences that are the same
    
#     # print(diff)
#     # print(curr)
#     # print(diffList)
    
#     # drop smallest price dif guy
#     print(diffList)
#     for i in range(5):
#         if (diffList[i][1] != -1):
#             dropPos = diffList[i][0]
            
#             if curr[dropPos] < len(sal[dropPos]) -1:
#                 curr[dropPos] += 1
#                 break
    
#     budget = (sal['p'][curr['p']]['salary'] + 
#               sal['g'][curr['g']]['salary'] + 
#               sal['s'][curr['s']]['salary'] + 
#               sal['f'][curr['f']]['salary'] + 
#               sal['c'][curr['c']]['salary'])
    
# print(sal)
    
# for pos in positions:
#     print(sal[pos][curr[pos]]['name'])
#     # budget = max_budget