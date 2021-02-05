my_list = [7,5,3,3,2]
a=min(my_list)
for j in range(4):
    val = int(input('Введите значение рейтинга: '))

    if val < a:
        my_list.append(val)
    else:
        for i in my_list:
         if val>=i:
            my_list.insert(my_list.index(i),val)
            break

    print(my_list)




