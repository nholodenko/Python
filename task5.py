def summ_var():
    '''Данная функция производит наращивание суммы, до момента ввода любой буквы'''
    z=[]
    while True:
        try:
            el = []
            var = input('Введите числа через пробел, для остановки введите любую букву: ').split()
            for i in var:
                i = float(i)
                el.append(i)
                summ = sum(el)
        except ValueError:
            print('Вы остановили сложение, Ваша сумма: ')
            print(sum(z)+sum(el))
            break
        z.append(summ)
        print(sum(z))
summ_var()
