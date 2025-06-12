import random
from User import User

class Character(User):
    def __init__(self, name, char_class):
        if char_class == "Воин":
            hp, mp, atk, dfs = 120, 20, 15, 10
        elif char_class == "Маг":
            hp, mp, atk, dfs = 80, 50, 10, 5
        elif char_class == "Вор":
            hp, mp, atk, dfs = 100, 30, 12, 8
        else:
            hp, mp, atk, dfs = 100, 20, 10, 5

        super().__init__(name, hp, mp, atk, dfs)

        self.char_class = char_class
        self.level = 1
        self.exp = 0
        self.potions = 2
        self.active_quests = []

    def attack_enemy(self, enemy):
        damage = random.randint(self.attack - 5, self.attack + 5)
        enemy.take_damage(damage)
        print(f"{self.name} атакует {enemy.name} на {damage} урона!")

    def cast_spell(self, enemy):
        if self.mp < 10:
            print("Недостаточно маны!")
            return
        self.mp -= 10
        damage = random.randint(15, 30)
        enemy.take_damage(damage)
        print(f"{self.name} использует заклинание на {enemy.name} и наносит {damage} урона!")

    def use_potion(self):
        if self.potions > 0:
            heal = random.randint(20, 40)
            self.hp = min(self.max_hp, self.hp + heal)
            self.potions -= 1
            print(f"{self.name} использует зелье и восстанавливает {heal} HP!")
        else:
            print("Зелья закончились!")

    def gain_exp(self, amount):
        self.exp += amount
        print(f"{self.name} получает {amount} опыта.")
        if self.exp >= 100:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.exp = 0
        self.max_hp += 10
        self.max_mp += 5
        self.attack += 2
        self.defense += 2
        self.hp = self.max_hp
        self.mp = self.max_mp
        print(f"\n{self.name} повышает уровень до {self.level}!")
        print(
            f"Параметры улучшены! HP: {self.max_hp}, MP: {self.max_mp}, Урон: {self.attack}, Защита: {self.defense}\n")