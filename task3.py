class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        return self.quantity + other.quantity

    def __sub__(self, other):
        sub = self.quantity - other.quantity
        return sub if sub > 0 else 'Не достаточно ячеек в первой клетке!'

    def __truediv__(self, other):
        return self.quantity // other.quantity

    def __mul__(self, other):
        return self.quantity * other.quantity

    def make_order(self, row):
        for i in range(self.quantity//row):
            print('*'*row)
        print(self.quantity%row*'*' if self.quantity%row!=0 else '')




cell = Cell(20)
cell2 = Cell(25)
print(cell + cell2)
print(cell - cell2)
print(cell / cell2)
print(cell * cell2)
cell2.make_order(7)