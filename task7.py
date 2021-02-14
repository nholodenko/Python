import json
with open('text8', encoding='utf-8') as f:
    firms = []
    ownerships = []
    proceeds = []
    costs = []
    for line in f:
        firms.append(line.split()[0])
        ownerships.append(line.split()[1])
        proceeds.append(int(line.split()[2]))
        costs.append(int(line.split()[3]))
    i=0
    j=0
    profits = []
    while i<len(proceeds):
        profits.append(proceeds[i] - costs[j])
        i+=1
        j+=1
    print(profits)
    print(proceeds)
    print(costs)
    plus_profits = []
    for i in profits:
        if i>0:
            plus_profits.append(i)
    dict1 = {'average_profit': ((sum(plus_profits) / len(plus_profits)).__round__(1))}
    dict2 = dict(zip(firms,profits))
    dict3 = [dict2, dict1]
    print(dict3)
with open("my_file.json", "w") as write_f:
    json.dump(dict3, write_f)