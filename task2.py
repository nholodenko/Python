class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_calculation(self):
        mass = self._length*self._width*25*5
        print(f'Масса асфальта на длину дорожного полотна {self._length} м '
              f'и ширину {self._width} м, равна {(mass/1000).__round__()}кг')


r = Road(20, 5000)
r.mass_calculation()
