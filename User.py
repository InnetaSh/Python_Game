import random

class User:
    def __init__(self, name, hp, mp, attack, defense):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.mp = mp
        self.max_mp = mp
        self.attack = attack
        self.defense = defense
        self.is_defending = False

    def take_damage(self, amount):
        if self.is_defending:
            amount = max(0, amount - self.defense * 2)
        else:
            amount = max(0, amount - self.defense)
        self.hp -= amount
        print(f"{self.name} получает {amount} урона!")

    def reset_turn(self):
        self.is_defending = False

    def defend(self):
        self.is_defending = True
        print(f"{self.name} встает в защитную стойку.")