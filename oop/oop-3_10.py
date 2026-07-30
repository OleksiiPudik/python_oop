class Cell:
    def __init__(self):
        self.value = 0

    def __bool__(self):
        return self.value == 0


class TicTacToe:
    FREE_CELL = 0      # свободная клетка
    HUMAN_X = 1        # крестик (игрок - человек)
    COMPUTER_O = 2     # нолик (игрок - компьютер)

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

    def _check_list(self):
        return [[self.pole[i][k].value for k in range(3)] for i in range(3)] + [[self.pole[k][j].value for k in range(3)] for j in range(3)] + [[self.pole[k][k].value for k in range(3)]] + [[self.pole[k][2-k].value for k in range(3)]]

game = TicTacToe()
game[0, 2] = 1
game[1, 1] = 1
game[2, 0] = 1
res = game._check_list()
print(res)