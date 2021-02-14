
with open('text4') as f:
    text=f.read()
    text = text.replace('One','Один' )
    text = text.replace('Two', 'Два')
    text = text.replace('Three', 'Три')
    text = text.replace('Four', 'Четыре')

with open('text5.txt', 'w') as f2:
    f2.write(text)



