from Enemy import Enemy
from Character import Character
from Quest import Quest
from Quest import NPC

import random


def battle(player, enemy):
    print(f"\n️ Битва начинается: {player.name} против {enemy.name}!\n")
    print("-" * 50)
    while player.hp > 0 and enemy.hp > 0:
        print(f"\n{player.name} — Health : {player.hp}/{player.max_hp}, Mana : {player.mp}/{player.max_mp}")
        print(f"{enemy.name} — Health: {enemy.hp}")
        print("\nВыберите действие:")
        print("1. Атака\n2. Защита\n3. Заклинание\n4. Зелье")

        choice = input("> ")
        player.reset_turn()
        enemy.reset_turn()
        match choice:
            case "1":
                player.attack_enemy(enemy)
            case "2":
                player.defend()
            case "3":
                player.cast_spell(enemy)
            case "4":
                player.use_potion()
            case _:
                print("Неверный выбор. Пропуск хода.")

        if enemy.hp <= 0:
            print(f"\n {enemy.name} побежден!")
            player.gain_exp(50)
            return True

        enemy.attack_player(player)

    if player.hp <= 0:
        print("\n Вы проиграли...")
        return False
    else:
        print(f" Победа над {enemy.name}!")
        exp_gained = (enemy.hp + enemy.attack * 5 + enemy.defense * 3) // 10
        player.gain_exp(exp_gained)
        return True


def main():
    print("Добро пожаловать в Битву Героев!\nВыберите класс:")
    print("1. Воин\n2. Маг\n3. Вор")
    class_choice = input("> ")
    match  class_choice:
        case "1":
            char_class = "Воин"
        case "2":
            char_class = "Маг"
        case "3":
            char_class = "Вор"
        case _:
            print("Неверный выбор. Назначен класс Воин.")
            char_class = "Воин"

    name = input("Введите имя вашего героя: ")
    player = Character(name, char_class)
    player.active_quests = []


# --------------------------------------------------------------------------------------
    quests_data = [
        (Quest("Убить Гоблина", "Победи гоблина, который терроризирует деревню.", False,"hp", 20),
         NPC("Старейшина", None),
         Enemy("Гоблин", 80, 12, 5)),
        (Quest("Победить Орка", "Орк блокирует путь в лес. Победи его!", False,"attack", 10),
         NPC("Охотник", None),
         Enemy("Орк", 120, 18, 8)),
        (Quest("Спасти деревню", "Победи огнедышащего дракона и спаси деревню!", False,"mp", 50),
         NPC("Мудрый Волшебник", None),
         Enemy("Дракон", 200, 25, 15)),
        (Quest("Найти потерянный амулет", "Верни амулет Старейшине, найденный в пещере.", False,"defense", 20),
         NPC("Старейшина", None),
         Enemy("Пещерный Тролль", 90, 15, 7)),
        (Quest("Собрать травы для зелья", "Собери 3 редкие травы в лесу для Волшебника.", False," potions", 20),
         NPC("Волшебник", None),
         Enemy("Лесной Волк", 70, 14, 6)),
        (Quest("Защитить караван", "Защити караван от разбойников на дороге.", False,"hp", 20),
         NPC("Караванщик", None),
         Enemy("Разбойник", 110, 17, 9)),
    ]


    while quests_data:
        quest, npc, enemy = random.choice(quests_data)

        npc.quest = quest
        quest_choise = npc.talk(player)
        if (quest_choise == 1):
            won = battle(player, enemy)

            if won and quest in player.active_quests:
                quest.complete(player)
            else:
                return

            quests_data.remove((quest, npc, enemy))
            print("-" * 50)
        else:
            print("-" * 50)

    # --------------------------------------------------------------------------------------


    print("\nСтатус квестов:")
    for q in player.active_quests:
        status = "Выполнен" if q.is_complete else "В процессе"
        print(f"- {q.title}: {status}")


if __name__ == "__main__":
    main()