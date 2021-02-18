from time import sleep
class TrafficLight:
    __color = {0:'Стойте!!!', 1:'Приготовьтесь', 2:'Движение разрешено'}
    def running(self):
        for i in range(3):
            print(TrafficLight.__color[i])
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(5)


t = TrafficLight()
t.running()

