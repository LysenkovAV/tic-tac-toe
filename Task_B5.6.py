GAME_FIELD_SIZE = 3 # Размер игрового поля

# Состояние игры
# Игрок 1 - имя 1-го игрока, можно будет доработать ввод имени
# Игрок 2 - имя 2-го игрока, можно будет доработать ввод имени
# Ход - показывает чей ход (варианты: Игрок 1 или Игрок 2)
# Символ - показывает текущий символ (варианты: X или O)
# Победитель - показывает кто победитель (варианты: в процессе, ничья, игрок 1, игрок 2)
game_state = {"Игрок 1": "Петсон",
              "Игрок 2": "Финдус",
              "Ход": "Петсон",
              "Символ": "X",
              "Победитель": "В процессе"}

# Игрокове поле - массив (варианты содержимого ячейки: -, X, O)
game_field = [["-" for j in range(GAME_FIELD_SIZE)] for i in range(GAME_FIELD_SIZE)]

# Вывод приветствия
def welcome():
    print("***********************")
    print("*   КРЕСТИКИ-НОЛИКИ   *")
    print("***********************")
    print("*  Формат ввода: х y  *")
    print("*  x - номер строки   *")
    print("*  y - номер столбца  *")
    print("***********************")
    print("*         1 2 3       *")
    print("*       1 - - -       *")
    print("*       2 - - -       *")
    print("*       3 - - -       *")
    print("***********************")
    print()

# Вывод игрового поля
def print_game_field(field):
#    global game_field
    for i in range(len(field)):
        print("        ", end='')
        for j in range(len(field)):
            print(field[i][j], end=' ')
        print()
    print()
    return field

# Функция проверки выигрыша
def check_win(field, symbol):
    temp_list = [symbol for j in range(len(field))]
    for i in range(len(field)):
        if field[i] == temp_list:  # Проверка строк
            return True
        if [field[j][i] for j in range(len(field))] == temp_list:   # Проверка столбцов
            return True
    if [field[d][d] for d in range(len(field))] == temp_list:   # Проверка 1-й диагонали
        return True
    if [field[d][len(field)-d-1] for d in range(len(field))] == temp_list:   # Проверка 2-й диагонали
        return True
    return False

# Функция проверки заполненности поля: True - есть возможность для хода, False - поле заполнено
def check_not_full (field):
    for i in range(len(game_field)):
        for j in range(len(game_field)):
            if field[i][j] == "-":
                return True
    return False

# Игровой цикл
# Завершается после победы одного из игроков или невозможности сделать следующий ход (нет пустых полей)
while True:
    field_row, field_col = None, None # Координаты клетки поля
    welcome()  # Ввывод приветствия
    #----------------ТЕСТОВЫЕ ВАРИАНТЫ ПОЛЕЙ ДЛЯ ОТЛАДКИ---------------
    # game_field = [["X", "-", "O"], ["-", "X", "O"], ["-", "-", "-"]]
    # game_field = [["X", "O", "O"], ["-", "O", "-"], ["X", "-", "X"]]
    # game_field = [["O", "-", "X"], ["O", "X", "-"], ["-", "-", "-"]]
    #------------------------------------------------------------------
    print_game_field(game_field)  # Ввывод игрового поля

    # Играк продолжается пока кто-нибудь не выиграл или пока есть пустые клетки на поле
    while game_state["Победитель"] == "В процессе":
        # Цикл получения координат поля от пользователя и проверки их корректности
        while True:
            try:
                field_row, field_col = map(int, list(input(f"""Ход игрока {game_state["Ход"]}: """).split(' ')))
            # Если введены не числа
            except ValueError:
                print("Неверные координаты, попробуйте ещё раз!")
                field_row, field_col = None, None
            if type(field_row) == int and type(field_col) == int:
                # Если введены числа, но выходящие за диапазон поля
                if field_row < 1 or field_row > GAME_FIELD_SIZE or field_col < 1 or field_col > GAME_FIELD_SIZE:
                    print("Координаты выходят за диапазон, попробуйте ещё раз!")
                    field_row, field_col = None, None
                # Если введены числа, но поле уже занято
                elif game_field[field_row-1][field_col-1] != "-":
                    print("Поле уже занято, попробуйте ещё раз!")
                    field_row, field_col = None, None
                else: break

        # Координаты введены верно, помещение на игровое поле символа соответствующего игрока
        game_field[field_row - 1][field_col - 1] = game_state["Символ"]

        print_game_field(game_field) # Вывод игрового поля с новым символом

        # Проверка выигрыша
        if check_win(game_field, game_state["Символ"]):
            print(f"""Победил {game_state["Ход"]}!""")
            game_state["Победитель"] = game_state["Ход"]    # Победил игрок, сделавший последний ход
        elif not check_not_full(game_field):
            print("Ничья, все клетки заполнены!")
            game_state["Победитель"] = "Ничья"  # Игра закончена без победителя
        else:   # Переход хода к другому игроку
            if game_state["Ход"] == game_state["Игрок 1"]:
                game_state["Ход"] = game_state["Игрок 2"]
                game_state["Символ"] = "O"
            else:
                game_state["Ход"] = game_state["Игрок 1"]
                game_state["Символ"] = "X"

    repeat_game = input("Начать игру заново? (Выход - N; Повторить - любой символ): ")
    if repeat_game == "N":
        break

    #Возврат к начальным настройкам
    game_state = {"Игрок 1": "Петсон",
                  "Игрок 2": "Финдус",
                  "Ход": "Петсон",
                  "Символ": "X",
                  "Победитель": "В процессе"}
    game_field = [["-" for j in range(GAME_FIELD_SIZE)] for i in range(GAME_FIELD_SIZE)]