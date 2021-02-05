UserVar = (input("Введите целое положительное число: "))
mistake = '.' in UserVar or ',' in UserVar or '-' in UserVar
while mistake:
    print('Не подходящее число!')
    UserVar = (input("Введите целое положительное число: "))
    mistake = '.' in UserVar or ',' in UserVar or '-' in UserVar
UserVar = int(UserVar)
listNumber =[]
while UserVar//10>10:
    listNumber.append(UserVar%10)
    UserVar = UserVar//10
listNumber.append(UserVar//10)
listNumber.append(UserVar%10)

print('Максимальная цифра в Вашем числе: ', max(listNumber))





