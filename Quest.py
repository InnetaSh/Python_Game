class Quest:
    def __init__(self, title, description, is_complete=False, type_quest=None, bonus=0):
        self.title = title
        self.description = description
        self.is_complete = is_complete
        self.type_quest = type_quest
        self.bonus = bonus


    def complete(self, player):
        if not self.is_complete:
            self.is_complete = True
            if self.type_quest == "hp":
                player.max_hp += self.bonus
                player.hp += self.bonus
                print(f"{player.name} получает +{self.bonus} к жизни!")
            elif self.type_quest == "mp":
                player.max_mp += self.bonus
                player.mp += self.bonus
                print(f"{player.name} получает +{self.bonus} к мане!")
            elif self.type_quest == "attack":
                player.attack += self.bonus
                print(f"{player.name} получает +{self.bonus} к урону!")
            elif self.type_quest == "defense":
                player.defense += self.bonus
                print(f"{player.name} получает +{self.bonus} к защите!")
            elif self.type_quest == "potions":
                player.potions += self.bonus
                print(f"{player.name} получает +{self.bonus} к зелью!")
            else:
                player.attack += self.bonus
                print(f"{player.name} получает +{self.bonus} к урону!")

class NPC:
    def __init__(self, name, quest=None):
        self.name = name
        self.quest = quest

    def talk(self, player):
        print(f"\n{self.name}: Привет, {player.name}!")
        if self.quest and not self.quest.is_complete:
            print(f"У меня для тебя задание: {self.quest.title}")
            print(self.quest.description)
            if (self.quest.type_quest == "hp"):
                type_quest_str = "к жизни"
            elif (self.quest.type_quest == "mp"):
                type_quest_str = "к мане"
            elif (self.quest.type_quest == "attack"):
                type_quest_str = "к урону"
            elif (self.quest.type_quest == "potions"):
                type_quest_str = "к зелью"
            else:
                type_quest_str = "к защите"
            print(f"В благодарость ты получишь: {self.quest.bonus}  {type_quest_str}")
            choice = input("Принять квест? (да - 1/нет - 2): ").lower()
            if choice == "1":
                print("Квест принят!")
                return 1
            else:
                print("Может в другой раз.")
                return 2
        elif self.quest and self.quest.is_complete:
            print("Спасибо, что выполнил задание!")
        else:
            print("Мне нечего тебе предложить.")
