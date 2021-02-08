def int_func_all():
    '''Данная функция переводит первую букву каждого слова в строке в верхний регистр'''
    def int_func(i):
        '''Данная функция переводит первую букву слова в верхний регистр'''
        #i.lower()
        r=[]
        kirill = ("абвгдежзийклмнопрстуфхцчшщьыъэюя")
        for s in i:
            if s in kirill:
                print('Вы ввели буквы из кириллицы в одно из слов! Оно не будет добавлено!')
                break
            else:
                try:
                    s = int(s)
                except:
                    r.append(s.lower())
        a = (''.join(r))
        return a.title()
    words = input('Введите список слов латинскими буквами, если присутствуют цифры - они будут удалены: ').split()
    line = []
    for i in words:
        line.append(int_func(i))
    print('Ваша строка: ', ' '.join(line))

int_func_all()
