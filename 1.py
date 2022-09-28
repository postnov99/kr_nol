print(
    "ЭТО ИГРА КРЕСТИКИ-НОЛИКИ. ПОБЕЖДАЕТ ТОТ, КТО ПЕРВЫМ УСПЕЛ ЗАНЯТЬ ПОЛНОСТЬЮ ДИАГОНАЛЬ ИЛИ ЛИНИЮ.\nВыбор делается,"
    " как в морском бою(например, a1 или с3)")
c = [['      1 ', ' 2 ', ' 3 '], [' a ', " * ", ' * ', ' * '], [' b ', " * ", ' * ', ' * '],
     [' c ', " * ", ' * ', ' * ']]


def game():
    print(str(c[0][0]), str(c[0][1]), str(c[0][2]), '\n', str(c[1][0]), str(c[1][1]), str(c[1][2]),
          str(c[1][3]), '\n', str(c[2][0]), str(c[2][1]), str(c[2][2]), str(c[2][3]), '\n', str(c[3][0]), str(c[3][1]),
          str(c[3][2]), str(c[3][3]))


def parse_coord(str_coord: str) -> ():
    if not str_coord[0].isalpha():
        return None
    if not str_coord[1].isnumeric():
        return None
    if len(str_coord) != 2:
        return None
    x_letter_mapping = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    x = x_letter_mapping.index(str_coord[0]) + 1
    y = int(str_coord[1])
    return x, y


def check_victory():
    if c[1][1] == c[1][2] == c[1][3] != " * " or c[2][1] == c[2][2] == c[2][3] != " * " or c[3][1] == c[3][2] == \
            c[3][3] != " * " or c[1][1] == c[2][1] == c[3][1] != " * " or c[1][2] == c[2][2] == c[3][2] != " * " or \
            c[1][3] == c[2][3] == c[3][3] != " * " or c[1][1] == c[2][2] == c[3][3] != " * " or c[1][3] == c[2][
        2] == c[3][1] != " * ":
        print("ПОБЕДА!")
        return True


game()

current_player = " + "


def switch_player():
    global current_player
    if current_player == " + ":
        current_player = " o "
    else:
        current_player = " + "


def validate_input(coord: ()) -> bool:
    if not coord:
        return False
    x, y = coord
    if c[x][y] == " * ":
        return True
    return False


while True:
    parse_res = None
    while not parse_res:
        parse_res = parse_coord(input(f"Текущий игрок:{current_player}. Ваш ход: "))
        if not validate_input(parse_res):
            print("Неверный ввод, повторите попытку.")
            parse_res = None

    x, y = parse_res
    c[x][y] = current_player
    game()
    if check_victory():
        break
    switch_player()
