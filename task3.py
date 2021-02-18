class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)}

class Position(Worker):
    def get_ful_time(self):
        print(f'Полное имя сотрудника: {self.name} {self.surname}')
    def total_income(self):
        print(f'Доход с учётом премии равен : {self._income["wage"]+self._income["bonus"]} т.р.')

p1 = Position('Иван','Иванов', 'Инженер', 50, 20)
p1.get_ful_time()
p1.total_income()
p2 = Position('Семён','Сидоров', 'Сантехник', 30, 10)
p2.get_ful_time()
p2.total_income()

