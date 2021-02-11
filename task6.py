from itertools import count
user_number = int(input('Введите число начала остчёта (от нуля до десяти): '))
for el in count(user_number):
    if el > 10:
        break
    else:
        print(el)
print('-'*15)

from itertools import cycle
my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
c=0
for el in cycle(my_list):
    if c > len(my_list[1:]):
        break
    print(el)
    c+=1