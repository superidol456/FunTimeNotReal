import random
import time
from data import *

def fight(current_enemy):
    round = random.randint(1, 2)
    enemy = enemies[current_enemy]
    enemy_hp = enemies[current_enemy]["hp"]
    print(f'Противник {enemy["name"]}: {enemy["script"]}')
    input("Нажмите Enter, чтобы продолжить")
    print()
    while player ["hp"] > 0 and enemy_hp > 0:
        if round % 2 == 1:
            print(f'{player["name"]} атакует {enemy["name"]}')
            crit = random.randint(1, 100)
            if crit < player["luck"]:
                enemy_hp -= player["attack"] * 3
            else:
                enemy_hp -= player["attack"]
            time.sleep(1)
            print(f'''{player["name"]} - {player["hp"]}\n{enemy["name"]} - {enemy_hp}.''')
            print()
            time.sleep(1)
        else:
            print(f'{enemy["name"]} атакует {player["name"]}')
            player["hp"] -= enemy["attack"] * player["armor"]
            time.sleep(1)
            print(f'''{player["name"]} - {player["hp"]}\n{enemy["name"]} - {enemy_hp}.''')
            print()
            time.sleep(1)
        round += 1

    if player["hp"] > 0:
        print(f'Противник - {enemy["name"]}: {enemy["win"]}')
        current_enemy += 1
    else:
        print(f'Противник - {enemy["name"]}: {enemy["loss"]}')
    player["hp"] = 20
    return current_enemy

def training(training_type):
    skip = "2"
    if items["2"]["name"] in player["inventory"]:
        skip = input("Желаете пропустить тренировку? 1 - да, 2- нет ")
    if skip == "2":
        for i in range(0, 101, 20):
            print(f'Тренировка завершена на {i}%')
            time.sleep(1.5)
    if training_type == '1':
        player['attack'] += 2
        print(f'Тренировка окончена! Теперь ты бьешь на {player["attack"]}')
    elif training_type == '2':
        player['armor'] -= .09
        print(f'Тренировка окончена! Теперь броня стопит {100 - player["armor"] * 100}% урона')
    print()
    
def display_player():
    print(f'Игрок - {player["name"]}')
    print(f'Величина атаки - {player["attack"]}. Шанс критического урона ({player["attack"]}ед.) равен {player["luck"]}')
    print(f'Броня поглощает {(1 - player["armor"]) * 100}% урона')


def display_enemy(current_enemy):
    enemy = enemies[current_enemy]
    print(f'Противник - {enemy["name"]}')
    print(f'Веилична атаки - {enemy["attack"]}')
    print(f'Здоровье - {enemy["hp"]}')

def display_inventory():
    print("У вас есть ")
    for value in player["inventory"]:
        print(value)
    print(f"У вас {player['money']} монет на балике")
    print()
    if "Зелье черепашьей мощи" in player ["inventory"]:
        potion = input("Желаете выпить зелье черепашьей мощи? 1 - да, 2 - нет ")
        if potion == "1":
            player["luck"] += 7
            print(f"Готово, теперь шанс нанести криты равен {player['luck']}%")
            player["inventory"].remove("Зелье черепашьей мощи")
    if "Фулл незер броня" in player ["inventory"]:
        nether = input("Желаете экипировать незерку? 1 - да, 2 - нет ")
        if nether == "1":
            player["armor"] += 100
            print(f"Готово, теперь ваша защита состовляет {player['armor']}")
            player["inventory"].remove("Фулл незер броня")
    if "Фулл алмазная броня" in player ["inventory"]:
        diamond = input("Желаете экипировать алмазку? 1 - да, 2 - нет ")
        if diamond == "1":
            player["armor"] += 50
            print(f"Готово, теперь ваша защита состовляет {player['armor']}")
            player["inventory"].remove("Фулл алмазная броня")
    if "Чарка" in player ["inventory"]:
        apple = input("Желаете скушать чарку? 1 - да, 2 - нет ")
        if apple == "1":
            player["hp"] += 100
            print(f"Готово, теперь ваше хп состовляет {player['hp']}")
            player["inventory"].remove("Чарка")



def shop():
    print("Добро пожаловать, путник, что хочешь приобрести?")
    print(f"У тебя есть {player['money']} монет")
    for key, value in items.items():
        print(f"{key} - {value['name']}: {value['price']}")
    
    item = input()
    if item in player["inventory"]:
        print(f"У тебя уже есть {items[item]['name']}")
    elif player['money'] >= items[item]['price']:
        print(f"Ты успешно приобрёл {items[item]['name']}")
        player['inventory'].append(items[item]['name'])
        player['money'] -= items[item]["price"]
    else:
        print("Не хватает монет :(")
    print()
    print("Буду ждать тебя снова, путник!")
    print()

def earn():
    casino = input("Добро пожаловать в казик! У тебя есть 67% шанс заработать и соответственно 33% шанс - проиграть, сколько ставишь? ")
    if player["money"] <= int(casino):
        print("У тебя таких денег нет")
    else: 
        result = random.randint(1, 100)
        time.sleep(1.5)
        print("Результат...")
        time.sleep(1.5)
        print("Страшно?")
        time.sleep(1.5)
        if result < 67:
            print("Вы выиграли!!!")
            player['money'] += int(casino)
        else:
            print("Выпал тнт, минус косарь")
            player["money"] -= int(casino)
        print()
        print(f"Осталось монет: {player['money']}")
        print()
