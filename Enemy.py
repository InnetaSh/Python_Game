import random
from User import User

class Enemy(User):
    def __init__(self, name, hp, attack, defense):
        super().__init__(name, hp, 0, attack, defense)

    def attack_player(self, player):
        damage = random.randint(self.attack - 5, self.attack + 5)
        player.take_damage(damage)
        print(f"{self.name} атакует {player.name} на {damage} урона!")

