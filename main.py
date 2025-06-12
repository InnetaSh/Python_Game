from Enemy import Enemy
from Character import Character
from Quest import Quest
from Quest import NPC

import random
import json



filePath_user = "Character.txt"


def load_file(path, cls):
    try:
        with open(path, "r", encoding="utf-8") as myfile:
            data = myfile.read()
            if data:
                data_dict = json.loads(data)
                return cls.from_dict(data_dict)
            else:
                return None
    except FileNotFoundError:
        return None
    except Exception as ex:
        print(f"Ошибка при загрузке: {ex}")
        return None


def save_file(obj, path):
    try:
        with open(path, "w", encoding="utf-8") as myfile:
            json.dump(obj.to_dict(), myfile, ensure_ascii=False, indent=4)
    except Exception as ex:
        print(f"Ошибка при сохранении: {ex}")




def battle(player, enemy):
    print(f"\n️ Битва начинается: {player.name} против {enemy.name}!\n")
    print("-" * 50)
    while player.hp > 0 and enemy.hp > 0:
        print(f"\n{player.name} — Health : {player.hp}/{player.max_hp}, Mana : {player.mp}/{player.max_mp}, Зелье: {player.potions}")
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

def new_player():
    print("Выберите класс:")
    print("1. Воин\n2. Маг\n3. Вор")
    class_choice = input("> ")
    match class_choice:
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
    print("-" * 50)
    print(
        f"Рад знакомству {player.name} \n( Health : {player.hp}/{player.max_hp}, Mana : {player.mp}/{player.max_mp}, Зелье: {player.potions})")
    print("-" * 50)
    return player


def main():
    save_player = load_file(filePath_user, Character)


    print("Добро пожаловать в Битву Героев!")
    if (save_player):
        print("Выберите:")
        print("1. Загрузить игру\n2. Новая игра")
        class_choice = input("> ")
        match class_choice:
            case "1":
                player = save_player
                print("-" * 50)
                print( f"Давно не виделись {player.name} \n( Health : {player.hp}/{player.max_hp}, Mana : {player.mp}/{player.max_mp}, Зелье: {player.potions})")
                print("-" * 50)
            case "2":
                player = new_player()
            case _:
                print("Неверный выбор. Начинаем новую игру.")
                player = new_player()
    else:
        player = new_player()


# --------------------------------------------------------------------------------------
    quests_data = {
        0: (Quest("Убить Гоблина", "Победи гоблина, который терроризирует деревню.", False,"hp", 20),
         NPC("Старейшина", None),
         Enemy("Гоблин", 80, 12, 5)),
        1:(Quest("Победить Орка", "Орк блокирует путь в лес. Победи его!", False,"attack", 10),
         NPC("Охотник", None),
         Enemy("Орк", 120, 18, 8)),
        2:(Quest("Спасти деревню", "Победи огнедышащего дракона и спаси деревню!", False,"mp", 50),
         NPC("Мудрый Волшебник", None),
         Enemy("Дракон", 200, 25, 15)),
        3:(Quest("Найти потерянный амулет", "Верни амулет Старейшине, найденный в пещере.", False,"defense", 20),
         NPC("Старейшина", None),
         Enemy("Пещерный Тролль", 90, 15, 7)),
        4:(Quest("Собрать травы для зелья", "Собери 3 редкие травы в лесу для Волшебника.", False," potions", 5),
         NPC("Волшебник", None),
         Enemy("Лесной Волк", 70, 14, 6)),
        5:(Quest("Защитить караван", "Защити караван от разбойников на дороге.", False,"hp", 20),
         NPC("Караванщик", None),
         Enemy("Разбойник", 110, 17, 9)),
    }


    while quests_data:
        quest_id = random.choice(list(quests_data.keys()))
        quest, npc, enemy = quests_data[quest_id]

        npc.quest = quest
        quest_choise = npc.talk(player)
        if (quest_choise == 1):
            won = battle(player, enemy)

            if won:

                if quest_id not in player.active_quests:
                    player.active_quests.append(quest_id)
                quest.complete(player)
                del quests_data[quest_id]
                save_file(player, filePath_user)
            else:
                return

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