with open('text3', 'r') as f:
    c = []
    count =0
    employee = []
    for line in f:
        l=line.split()
        count+=1
        for i in l:
            try:
                num = int(i)
                c.append(num)
                if num<20:
                    employee.append(l[0])
            except ValueError:
                continue
    print('Средняяя заработная плата равна', (sum(c)/count).__round__(1), 'т.р.')
    print('Список сотрудников с заработной платой менее 20 т.р.:', employee)
