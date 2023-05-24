from random import randint


def random_queens_positions(size=4):
    """
    Заполняет рандомные места нахождения ферзей.
    Принимает на вход размер доски (не обязательно, по умолчанию 8)
    :return: [(0, 0), (1, 4), (2, 7), (3, 5), (4, 2), (5, 6), (6, 1), (7, 3)]
    """
    pos = [tuple(randint(0, size - 1) for i in range(2)) for j in range(size)]
    while len(set(pos)) != size:
        change_val_status = True
        change_val = ()
        while change_val_status is True:
            change_val = (randint(0, size - 1), randint(0, size - 1))
            if change_val not in pos:
                change_val_status = False
        for i in pos:
            if pos.count(i) > 1:
                pos[pos.index(i)] = change_val
    return pos


def check_horizontal_and_vertical(data: list[tuple[int, int]]) -> bool:
    """
    Данная функция принимает на вход список позиций фигур на шахматной доске, заданных координатами х и у.
    Далее попарно сравниваются координаты двух фигур, первой со второй, третьей и последующими,
    второй с третьей, четвертой и последующими и т.д.
    Если координаты х1 и х2 ИЛИ у1 и у2 совпадают (if x1 == x2 or y1 == y2) - фигуры находятся на одной линии.
    Далее сравнивается разница по модулю соответствующих координат двух фигур, первая со второй, третьей и последующими,
    вторая с третьей, четвертой и последующими и т.д.
    Если разница по модулю координат х равна разнице по модулю координат у (abs(x1 - x2) == abs(y1 - y1)) -
    фигуры расположены на одной диагонали.
    """
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i][0] == data[j][0] or data[i][1] == data[j][1]:
                # print("Совпадение найдено:", data[i], data[j])
                return False

    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if abs(data[i][0] - data[j][0]) == abs(data[i][1] - data[j][1]):
                # print("Совпадение найдено:", data[i], data[j])
                return False

    return True


def arrange_the_figures(position, size):
    chessboard = [['0' for x in range(size)] for y in range(size)]
    queens_positions = position
    for i in range(size):
        column, row = queens_positions[i]
        if chessboard[row][column] != 'X':
            chessboard[row][column] = 'X'
        else:
            continue

    return chessboard


def print_the_desk(desk_list, board_size):
    count = 0
    for i in desk_list:
        count += 1
        res = arrange_the_figures(i, board_size)
        print(f'\nВариант расстановки №{count}')
        for j in res:
            print(j)
