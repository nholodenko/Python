path = int(input('Введите продолжительность Вашей пробежки на сегодняшний день в км. : '))
desired_path = int(input('Введите желаемую продолжительность Вашей пробежки в км. : '))
count = 1
while desired_path > path:
    path = path + path*10/100
    count+=1
print('На',count,"- ой день Вы достигните своей цели!")
