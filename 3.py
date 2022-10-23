from __future__ import annotations
class Object:
    def __init__(self, name, HP, attack_damage):
        self.name = name
        self.HP = HP        #선언같은건가 
        self.attack_damage = attack_damage
        
    def attack(self): # 공격했을때 데미지가 들어가는거
        self.HP -= self.attack_damage

class Player(Object): # 마법데미지 50을 말하는거
    def Magic_Attack(self, target : Object):
        target.HP -= 50
        

class Monster(Object): # 몬스터들 기본 정보들
    def Mini_Goblin(self):
        self.HP = 10
        self.attack_damage = 10
    def Goblin(self):
        self.HP = 30
        self.attack_damage = 30
    def Super_Goblin(self):
        self.HP = 50
        self.attack_damage = 50
    def heal(self):
        self.HP += 10
        print(f"{self.name}가 자신의 체력을 10만큼 회복했다.")
    def stay(self):
        print(f"{self.name}가 대기했습니다.")
#print(f"Mini Goblin HP = {self.HP} Goblin HP = {self.HP} Super Goblin = {self.HP} \n Mini Goblin Damage = {self.attack_damage}")