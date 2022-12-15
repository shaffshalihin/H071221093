from abc import ABC, abstractmethod

class Character(ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name
        self.position = 0
    def isFinish(self):
        if self.position >=100:
            print(self.name, 'telah finish')
        else:
            print(self.name, 'belum finish')

class Rabbit(Character):
    def __init__(self, name):
        super().__init__(name)

    def getName(self):
        return self.name
    
    def run(self):
        self.position += 20

    def getposition(self):
        return self.position

    def attack(self, target):
        target.position -= 10

    def boost(self):
        self.position += 30



class Turtle(Character):
    def __init__(self, name):
        super().__init__(name)

    def getName(self):
        return self.name
    
    def run(self):
        self.position += 20

    def getposition(self):
        return self.position

    def attack(self, target):
        target.position -= 35

    def boost(self):
        self.position += 15


rabbit = Rabbit('bambang')
turtle = Turtle('adi')

for i in range(0,5):
    turtle.run()

turtle.attack(rabbit)

for i in range(0, 5):
    rabbit.run()

rabbit.attack(turtle)

turtle.boost()

print(turtle.getposition())
turtle.isFinish()

print(rabbit.getposition())
rabbit.isFinish()



