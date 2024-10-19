# Объявить класс.
class Board:
    """ Класс, который описывает игровое поле."""

    f_size = 3

    def __init__(self):
        self.board = [
            [' ' for _ in range(self.f_size)] for _ in range(self.f_size)
        ]

    # Метод, который обрабатывает ходы игроков.
    def make_move(self, row, col, player):
        self.board[row][col] = player

    # Метод, который отрисовывает игровое поле.
    def display(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def __str__(self):
        return (
            'Объект игрового поля размером '
            f'{self.f_size}x{self.f_size}'
        )
