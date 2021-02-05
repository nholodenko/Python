UserTime = int(input('Введите время в секундах: '))
hour = UserTime//3600
minn = (UserTime%3600)//60
sec = (UserTime%3600)%60
print('Ваше время в часах: ','{:02}:{:02}:{:02}'.format(hour, minn, sec))
