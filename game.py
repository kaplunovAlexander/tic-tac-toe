from gameparts import Board
# from inspect import getsource
from gameparts.exceptions import FieldIndexError, CellOccupiedError


def save_result(result):
    with open('results.txt', 'a') as file:
        file.write(f'{result}\n')


def main():
    # Создать игровое поле - объект класса Board.
    game = Board()
    current_player = 'X'
    running = True
    # Отрисовать поле в терминале.
    game.display()
    while running:
        while True:
            try:
                # Тут пользователь вводит координаты ячейки.
                row = int(input('Введите номер строки: '))
                # Если введённое значение меньше нуля или больше или равно
                # field_size (это значение равно трём, оно хранится в модуле
                # parts.py)...
                if row < 0 or row >= game.field_size:
                    # ...выбросить исключение FieldIndexError.
                    raise FieldIndexError
                column = int(input('Введите номер столбца: '))
                if column < 0 or column >= game.field_size:
                    # ...выбросить исключение FieldIndexError.
                    raise FieldIndexError
                if game.board[row][column] != ' ':
                    # Вот тут выбрасывается новое исключение.
                    raise CellOccupiedError
            except FieldIndexError:
                print(
                    'Значение должно быть неотрицательным и меньше '
                    f'{game.field_size}.'
                )
                print('Пожалуйста, введите значения для строки и столбца заново.')
                continue
            except CellOccupiedError:
                print('Ячейка занята')
                print('Введите другие координаты.')
                continue
            except ValueError:
                print('Буквы вводить нельзя. Только числа.')
                print('Пожалуйста, введите значения для строки и столбца заново.')
                continue
            except Exception as e:
                print(f'Возникла ошибка: {e}')
            else:
                break
        # В метод make_move передаются те координаты, которые ввёл пользователь.
        game.make_move(row, column, current_player)
        print('Ход сделан!')
        game.display()
        if game.check_win(current_player):
            result = f'Победили {current_player}!'
            print(result)
            save_result(result)
            running = False
        elif game.is_board_full():
            result = 'Ничья!'
            print(result)
            save_result(result)
            running = False

        current_player = 'O' if current_player == 'X' else 'X'
        # print(getsource(Board))
        # print(Board.__doc__)


if __name__ == '__main__':
    main()
