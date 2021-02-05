
goods = []
elements = []
for i in range(3):
    element = {
        'название': input('Введите название товара: '),
        'цена': int(input('Введите цену товара: ')),
        'количество': int(input('Введите количество товара: ')),
        'единицы': (input('Введите единицу товара: '))
    }
    good = (i+1, element)
    goods.append(good)
    elements.append(element)
print(goods)

name = []
for x in elements:
    name.append(x['название'])
cost = []
for x in elements:
    cost.append(x['цена'])
value = []
for x in elements:
    value.append(x['количество'])
units = []
for x in elements:
    units.append(x['единицы'])

sort = {'название': name, 'цена':cost, 'количество': value, 'единицы':units}

print(sort)
