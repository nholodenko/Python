def my_func(*args):
    '''Принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов'''
    vars = []
    for i in range(3):
     i = int(input("Введите первое число: "))
     vars.append(i)
    vars.remove(min(vars))
    return sum(vars)
print("Сумма наибольших чисел равна: ", my_func())