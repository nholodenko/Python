class Car:
    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        print(f'Машина поехала!')

    def stop(self):
        print(f'Машина остановилась!')

    def turn(self, direction):
        self.direction = direction
        print(f'Машина повернула {self.direction}')

    def show_speed(self, current_speed):
        self.current_speed = current_speed
        print(f'текущая скорость равна:  {self.current_speed}')


class TownCar(Car):
    def show_speed(self, current_speed):
        self.current_speed = current_speed
        print(f'текущая скорость равна:  {self.current_speed}')
        if self.current_speed > 60:
            print('Скорость превышена!')


class WorkCar(Car):
    def show_speed(self, current_speed):
        self.current_speed = current_speed
        print(f'текущая скорость равна:  {self.current_speed}')
        if self.current_speed > 40:
            print('Скорость превышена!')


class SportCar(Car):
    color = 'желтый'


class PoliceCar(Car):
    def __init__(self, name, speed, color, is_police=True):
        super().__init__(self, name, speed, color)
        self.is_police = is_police


c = Car('Mazda', 200, 'красный')
print(c.name)
print(c.color)
print(c.speed)
print(c.is_police)
c.show_speed(180)
c.go()
c.stop()
c.turn('налево')
print('-'*100)

sc = SportCar('Lambo', 300, 'желтый')
print(sc.color)
print('-'*100)

pc = PoliceCar('Lada', 200, 'белый')
print(pc.is_police)
print('-'*100)

tc = TownCar('Pezo', 120, 'синий')
tc.show_speed(200)
print('-'*100)

wc = WorkCar('Zil', 60, 'синий')
wc.show_speed(50)
print('-'*100)

