class Object:
    def __init__(self, name, HP, attack_damage):
        self.name = name
        self.HP = HP
        self.attack_damage = attack_damage
    def attack(self):
        self.HP -= self.attack_damage

class Player(Object):
    def Magic_Attack(self, target):
        print(f"Mini Goblin HP = {self.HP} Goblin HP = {self.HP} Super Goblin = {self.HP} \n Mini Goblin Damage = {self.attack_damage}")
        print("누구를 공격하시겠습니까?")
        

class Monster(Object):
    def Mini_Goblin(self):
        self.HP = 10
        self.attack_damage = 10
    def Goblin(self):
        self.HP = 30
        self.attack_damage = 30
    def Super_Goblin(self):
        self.HP = 50
        self.attack_damage = 50
