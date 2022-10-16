class Animal:
    def __init__(self, name):
        self.name = name
    def cry(self):
        print()
        

class Cat(Animal):
    def cry(self):
        print('야옹')

class Dog(Animal):
    def cry(self):
        print('왈왈')


def 동물_울기(animal : Animal): 
    animal.cry()


동물_울기(Cat('미미')) # 야옹이 출력된다.