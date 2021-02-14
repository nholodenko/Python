with open('text6', 'w') as f:
    f.write('1 5 6 9 8 7 5 6')
with open('text6') as f:
    c = []
    for line in f:
        l=line.split()
        for i in l:
            try:
                num = int(i)
                c.append(num)
            except ValueError:
                continue
    print('Сумма чисел равна', sum(c))

