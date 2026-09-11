from inventory import inventory

def castle():
    print("Вы у ворот огромного замка. Ворота заперты.")
    print("1) Вернуться в горы")
    print("2) Открыть ворота ключом")

    choice = input()

    if choice == "1":
        return "mountains"
    elif choice == "2":
        if "ключ" in inventory:
            print("Ключ подошел! Вы входите в замок.")
            return "castle_hall"
        else:
            print("Ворота не поддаются. Нужен ключ.")
            return "castle"
    else:
        return "castle"


def castle_hall():
    print("Вы в главном зале замка. Перед вами высокая башня.")
    print("1) Выйти из замка")
    print("2) Подняться в башню")

    choice = input()

    if choice == "1":
        return "castle"
    elif choice == "2":
        return "tower"
    else:
        return "castle_hall"


def garden():
    print("Вы в прекрасном королевском саду.")
    print("1) Вернуться в деревню")
    print("2) Отдохнуть на скамейке")

    choice = input()

    if choice == "1":
        return "village"
    elif choice == "2":
        print("Вы отдохнули и полны сил.")
        return "garden"
    else:
        return "garden"


def dungeon():
    print("Вы в темном подземелье. Здесь очень страшно.")
    print("1) Вернуться в пещеру")
    print("2) Искать выход")

    choice = input()

    if choice == "1":
        return "cave"
    elif choice == "2":
        print("Вы нашли потайной ход на поверхность!")
        return "forest"
    else:
        return "dungeon"


def tower():
    print("Вы на вершине башни. Вид просто потрясающий!")
    print("1) Спуститься в зал")
    print("2) Завершить приключение")

    choice = input()

    if choice == "1":
        return "castle_hall"
    elif choice == "2":
        print("Поздравляем! Вы прошли квест!")
        return "end"
    else:
        return "tower"


def village():
    print("Вы в уютной деревне. Местный житель предлагает лодку в обмен на грибы.")
    print("1) Вернуться к реке")
    print("2) Обменять грибы на лодку")
    print("3) Пойти в сад")

    choice = input()

    if choice == "1":
        return "river"
    elif choice == "2":
        if "грибы" in inventory:
            print("Вы отдали грибы и получили лодку!")
            inventory.remove("грибы")
            inventory.append("лодка")
        else:
            print("У вас нет грибов для обмена.")
        return "village"
    elif choice == "3":
        return "garden"
    else:
        return "village"
