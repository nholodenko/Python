
ingredients = input('Введите начинки для пиццы через пробел : ').split()
for i in ingredients:
    print(ingredients.index(i)+1, i[:10])
