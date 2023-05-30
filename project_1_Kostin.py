import random

# Відображення ігрової дошки
def display_board(board):
    print("-------------")
    for i in range(3):
        print("|", board[i][0], "|", board[i][1], "|", board[i][2], "|")
        print("-------------")

# Функція для отримання ходу від гравця
def get_player_move(board):
    while True:
        try:
            move = int(input("Введіть клітинку (1-9): "))
            if move < 1 or move > 9:
                print("Номер клітинки має бути від 1 до 9.")
            else:
                row = (move - 1) // 3
                col = (move - 1) % 3
                if board[row][col] != " ":
                    print("Цей клітинка вже зайнята. Виберіть іншу.")
                else:
                    return row, col
        except ValueError:
            print("Введено некоректне значення. Спробуйте ще раз.")

# Отримання випадкового ходу від комп'ютера
def get_computer_move(board):
    available_moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                available_moves.append((i, j))
    return random.choice(available_moves)

# Перевірка переможця
def check_win(board, player):
    # Перевірка горизонтальних комбінацій
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
    # Перевірка вертикальних комбінацій
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    # Перевірка діагональних комбінацій
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False


# Основа гри
def play_game():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    current_player = "X"  # Комп'ютер завжди ходить першим
    display_board(board)

    while True:
        if current_player == "X":
            # Хід комп'ютера
            print("Ходить комп'ютер (X):")
            row, col = get_computer_move(board)
        else:
            # Хід гравця
            print("Ви ходите (O):")
            row, col = get_player_move(board)

        # Оновлення дошки
        board[row][col] = current_player
        display_board(board)

        # Перевірка результату гри
        if check_win(board, current_player):
            print("Гравець", current_player, "виграв!")
            break
        elif all(board[i][j] != " " for i in range(3) for j in range(3)):
            print("Гра закінчилася нічиєю!.")
            break

        # Зміна активного гравця
        current_player = "O" if current_player == "X" else "X"

# Запуск гри
play_game()