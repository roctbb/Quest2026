from inventory import inventory
import random

def forest():
    print("Вы в лесу. Перед вами пещера, а на востоке течет река.")
    print("1) Войти в пещеру")
    print("2) Пойти к реке")
    print("3) Собрать грибов")
    print("4) Остаться в лесу")

    if "грибы" in inventory:
        print("У вас есть грибы")
    else:
        print("У вас нет грибов")

    choice = input()

    if choice == "1":
        return "cave"
    elif choice == "2":
        return "river"
    elif choice == "3":
        if random.randint(0, 10) > 5:
            print("Вы нашли грибы!")
            if "грибы" not in inventory:
                inventory.append("грибы")
        else:
            print("Вы не нашли грибы.")
        return "forest"
    elif choice == "4":
        return "forest"
    else:
        print("Надо что-то выбрать! Вы остались в лесу.")
        return "forest"


def cave():
    print("Вы в глубокой пещере. Сзади вас выход в лес. В углу что-то блестит.")
    print("1) Пойти в лес")
    print("2) Осмотреть блестящий предмет")
    print("3) Спуститься глубже в подземелье")

    choice = input()

    if choice == "1":
        return "forest"
    elif choice == "2":
        if "ключ" not in inventory:
            print("Вы нашли старый ключ!")
            inventory.append("ключ")
        else:
            print("Здесь больше ничего нет.")
        return "cave"
    elif choice == "3":
        return "dungeon"
    else:
        print("Надо что-то выбрать! Вы остались в пещере.")
        return "cave"


def river():
    print("Вы на берегу бурной реки. На другом берегу видна деревня.")
    if "лодка" in inventory:
        print("У вас есть лодка, вы можете переправиться.")
    print("1) Вернуться в лес")
    print("2) Попробовать переплыть (нужна лодка)")
    print("3) Идти вдоль берега к горам")

    choice = input()

    if choice == "1":
        return "forest"
    elif choice == "2":
        if "лодка" in inventory:
            print("Вы успешно переправились в деревню!")
            return "village"
        else:
            print("Река слишком бурная, нужна лодка.")
            return "river"
    elif choice == "3":
        return "mountains"
    else:
        return "river"


def mountains():
    print("Вы высоко в горах. Отсюда виден замок и мрачное болото.")
    print("1) Вернуться к реке")
    print("2) Спуститься к болоту")
    print("3) Подняться к замку")

    choice = input()

    if choice == "1":
        return "river"
    elif choice == "2":
        return "swamp"
    elif choice == "3":
        return "castle"
    else:
        return "mountains"

def swamp():
    print("Вы на топком болоте. Здесь очень туманно.")
    print("1) Вернуться в горы")
    print("2) Идти на зов в тумане (к хижине)")

    choice = input()

    if choice == "1":
        return "mountains"
    elif choice == "2":
        print("Вы нашли хижину ведьмы, но она пуста. Пришлось вернуться.")
        return "swamp"
    else:
        return "swamp"