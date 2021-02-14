with open("text.txt", 'w') as f:
    text = input('Введите текст строки: ')
    while len(text) != 0:
        f.write(text + '\n')
        text = input('Введите текст строки: ')


