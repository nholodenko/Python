
class Clothes():

    def __init__(self, param):
        self.param = param

class Coat(Clothes):
    @property
    def consumption(self):
        return (self.param / 6.5 + 0.5).__round__(2)

class Costume(Clothes):
    @property
    def consumption(self):
        return (2 * self.param + 0.3).__round__(2)




coat = Coat(46)
print(coat.consumption)
costume = Costume(55)
print(coat.consumption + costume.consumption)









