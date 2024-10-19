from gameparts import Board


def main():
    # Создать игровое поле - объект класса Board.
    game = Board()
    # Отрисовать поле в терминале.
    game.display()
    # Разместить на поле символ по указанным координатам - сделать ход.
    game.make_move(1, 1, 'X')
    print('Ход сделан!')
    game.make_move(0, 1, 'O')
    # Перерисовать поле с учётом сделанного хода.
    game.display()


if __name__ == '__main__':
    main()
