MyList = []
Ask = input("Введите список чисел через запятую: ").split(',')
for i in Ask:
  MyList.append(int(i))
j=0
for i in range(int(len(MyList)/2)):
    MyList[j], MyList[j+1]=MyList[j+1], MyList[j]
    j+=2
print('Поменяем местами соседние элементы последовательности:', MyList)
