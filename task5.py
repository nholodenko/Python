proceeds = int(input('Введите значение выручки в руб. : '))
costs = int(input('Введите значение издержек в руб. : '))
if proceeds > costs:
    profit = proceeds - costs
    profitability = profit/costs*100
    print('Рентабельность Вашей фирмы составляет: ', profitability, ' %')
    numbers_staff = int(input('Введите колличество сотрудников Вашей фирмы: '))
    print('Прибыль Вашей фирмы в расчете на одного сотрудника составила: ', profit/numbers_staff, 'руб.')
else:
    print('К сожалению, Ваша фирма не рентабельна')