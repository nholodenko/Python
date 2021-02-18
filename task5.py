class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'{self.title}.Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'{self.title}.Запуск отрисовки ручкой')


class Pencil(Stationery):
    def draw(self):
        print(f'{self.title}.Запуск отрисовки карандашом')


class Handle(Stationery):
    def draw(self):
        print(f'{self.title}.Запуск отрисовки маркером')

pen = Pen('Скетч ручкой')
pen.draw()
pencil = Pencil('Скетч карандашем')
pencil.draw()
handle = Handle('Скетч маркером')
handle.draw()