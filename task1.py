def my_div():
    '''Данная функция принимает два числа и выполняет их деление'''
    arg1 = float(input('Введите первое число: '))
    arg2 = float(input('Введите второе число: '))
    try:
        div = round(arg1 / arg2, 2)
    except ZeroDivisionError:
        print('Вы пытаетесь делить на ноль!!!')
        arg1 = float(input('Введите первое число: '))
        arg2 = float(input('Введите второе число: '))
        div = round(arg1 / arg2, 2)
        return div
        exit()
    return div

print(my_div())
