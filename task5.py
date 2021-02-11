from functools import reduce  # Функция для свёрки последовательности
from operator import mul  # Функция, перемножающая 2 числа

spisok = [el for el in range(100,1001) if el%2==0]  # Исходный список
result = reduce(mul, spisok)
print(result)