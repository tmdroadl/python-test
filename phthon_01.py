class Rectangle:
    def __init__(self,garo,sero):
        self.garo = garo
        self.sero = sero

    def getArea(self):
        result1 = (self.garo * self.sero)
        return result1


    def getRound(self):
        result2 = (self.garo + self.sero) * 2
        return result2


class Triangle:
    def __init__(self,nop2,nulbe):
        self.num1 = nop2
        self.num2 = nulbe

    def getArea(self):
        result = (self.num1 * self.num2) / 2
        return result

class Foursquare:
    def __init__(self,garosero):
        self.garosero = garosero
    
    def getRound(self):
        result = self.garosero * 4
        return result

    def getArea(self):
        result = self.garosero**2
        return result


t = Triangle(5,10)
print(t.getArea())

r = Rectangle(5,10)
print(r.getRound())
print(r.getArea())

f = Foursquare(5)
print(f.getRound())
print(f.getArea())