import random

class Cell:
    def __init__(self):
        self.value = 0

    def __bool__(self):
        return self.value == 0


class TicTacToe:
    FREE_CELL = 0      # свободная клетка
    HUMAN_X = 1        # крестик (игрок - человек)
    COMPUTER_O = 2     # нолик (игрок - компьютер)
    INCORRECT_INDX_HUMAN = "Некоректно введены индексы. Индексов должно быть 2, их значение должно быть от 0 до 2."

    def __init__(self):
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))

    def __check_index(self, *args):
        for i in args:
            if isinstance(i, bool) or not isinstance(i, int) or i < 0 or i > 2:
                raise IndexError("некорректно указанные индексы")
        
    def __getitem__(self, key):
        row, col = key
        self.__check_index(row, col)
        return self.pole[row][col].value

    def __setitem__(self, key, value):
        row, col = key
        self.__check_index(row, col)
        self.pole[row][col].value = value

    def _rows_cols_diags(self):
        return [[self.pole[i][k].value for k in range(3)] for i in range(3)] + [[self.pole[k][j].value for k in range(3)] for j in range(3)] + [[self.pole[k][k].value for k in range(3)]] + [[self.pole[k][2-k].value for k in range(3)]]

    @property
    def is_human_win(self):
        return any(all(j == self.HUMAN_X for j in line) for line in self._rows_cols_diags())

    @property
    def is_computer_win(self):
        return any(all(j == self.COMPUTER_O for j in line) for line in self._rows_cols_diags())

    @property
    def is_draw(self):
        return all(all(not cell for cell in line) for line in self.pole) and not self.is_human_win and not self.is_computer_win

    def __bool__(self):
        return not self.is_human_win and not self.is_computer_win and not self.is_draw

    def init(self):
        for line in self.pole:
            for cell in line:
                cell.value = self.FREE_CELL

    def show(self):
        for line in self.pole:
            for cell in line:
                if cell.value == self.FREE_CELL:
                    print("#", end=" ")
                elif cell.value == self.HUMAN_X:
                    print("X", end=" ")
                elif cell.value == self.COMPUTER_O:
                    print("0", end=" ")

            print()

        print("----------")

    def human_go(self):
        correct_input = False

        while not correct_input:
            indx_in = input("Введите индексы клетки через запятую: ")
            indx_lst = [i.strip() for i in indx_in.split(",")]
            if len(indx_lst) == 2 and all((i.isdigit() for i in indx_lst)):
                row, col = (int(i) for i in indx_lst)
                if row > 2 or col > 2:
                    print(self.INCORRECT_INDX_HUMAN)
                elif not self.pole[row][col]:
                    print("Клетка занята, выберете другую")
                else:
                    correct_input = True
            else:
                print(self.INCORRECT_INDX_HUMAN)

        self[row, col] = self.HUMAN_X

    def computer_go(self):
        free_cells = []

        for row in range(3):
            for col in range(3):
                if self.pole[row][col]:
                    free_cells.append([row, col])

        row, col = random.choice(free_cells)
        self[row, col] = self.COMPUTER_O




game = TicTacToe()
game.init()
step_game = 0
while game:
    game.show()

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()

    step_game += 1


game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")

