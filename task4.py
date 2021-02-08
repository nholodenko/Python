def my_func():
    '''Эта функция возводит введенное число в отрицательную степень'''
    def input_var():
        '''Эта функция проверяет что введенное число целое'''
        try:
            var = int(input())
        except ValueError:
            print("Введенное значение не целое")
            var = int(input("Введите число: "))
        return var
    print('Введите целое положительное число')
    x = input_var()
    if x < 0:
         print("Введенное число не положительно, повторите ввод")
         x = input_var()
    if x == 0:
        print("Введенное число не положительно, повторите ввод")
        x = input_var()
    print('Введите целую отрицательную степень')
    y = input_var()
    if y > 0:
        print("Введенное число не отрицательно, повторите ввод")
        y = input_var()
    invert_y = y * (-1)
    z = []
    for i in range(invert_y):
        z.append(x)
    power = 1
    for i in z:
        power *= i
    result = 1/power
    return result
print(my_func())