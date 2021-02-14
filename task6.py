with open('text7', encoding='utf-8') as f:
    subjekts = []
    hours = []
    for line in f:
        subjekts.append(line.split()[0])
        l = len(line)
        integ = []
        i = 0
        while i < l:
            s_int = ''
            a = line[i]
            while '0' <= a <= '9':
                s_int += a
                i += 1
                if i < l:
                    a = line[i]
                else:
                    break
            i += 1
            if s_int != '':
                integ.append(int(s_int))
        hours.append(sum(integ))
    time_table = dict(zip(subjekts,hours))
    print(time_table)

