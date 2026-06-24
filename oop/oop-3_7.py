# tasc 4
# import sys

# class Player:
#     def __init__(self, name, old, score):
#         self.name = name
#         self.old = old
#         self.score = score
    
#     def __bool__(self):
#         return self.score > 0

# lst_in = list(map(str.strip, sys.stdin.readlines()))

# players = []
# for i in lst_in:
#     name_in, old_in, score_in = i.split(";")
#     name_in, old_in, score_in = name_in.strip(), int(old_in.strip()), int(score_in.strip())
#     players.append(Player(name_in, old_in, score_in))

# players_filtered = list(filter(bool, players))
# print(players, players_filtered, sep="\n")

# --------------------------------------------
# tasc 5
# import sys
# class MailBox:
#     def __init__(self):
#         self.inbox_list = []
    
#     def receive(self):
#         lst_in = list(map(str.strip, sys.stdin.readlines()))
        
#         for indx, i in enumerate(lst_in):
#             mail_from_in, title_in, content_in = i.split(";")
#             mail_from_in, title_in, content_in = mail_from_in.strip(), title_in.strip(), content_in.strip()
#             item = MailItem(mail_from_in, title_in, content_in)
#             self.inbox_list.append(item)
#             if indx in (0, len(lst_in) - 1):
#                 item.set_read(True)
        
#         return self.inbox_list


# class MailItem:
#     def __init__(self, mail_from, title, content):
#         self.mail_from = mail_from
#         self.title = title
#         self.content = content
#         self.is_read = False

#     def set_read(self, fl_read):
#         self.is_read = fl_read
    
#     def __bool__(self):
#         return self.is_read


# mail = MailBox()
# inbox_list_filtered = list(filter(bool, mail.receive()))
# print(inbox_list_filtered)

# --------------------------------------------
# tasc 6
# import math

# class Line:
#     def __init__(self, x1, y1, x2, y2):
#         self.x1 = x1
#         self.y1 = y1
#         self.x2 = x2
#         self.y2 = y2
    
#     def __len__(self):
#         return math.floor(math.dist((self.x1, self.y1), (self.x2, self.y2)))
        
# --------------------------------------------
# tasc 7
# class Ellipse:
#     def __init__(self, x1=None, y1=None, x2=None, y2=None):
#         self.x1 = x1
#         self.y1 = y1
#         self.x2 = x2
#         self.y2 = y2

#     def __bool__(self):
#         if None in (self.x1, self.y1, self.x2, self.y2):
#             return False
        
#         return True

#     def get_coords(self):
#         if not self:
#             raise AttributeError("нет координат для извлечения")

#         return (self.x1, self.y1, self.x2, self.y2)
        

# lst_geom = [Ellipse(), Ellipse(), Ellipse(1, 2, 3, 4), Ellipse(5, 6, 7, 8)]

# for i in lst_geom:
#     if i:
#         i.get_coords()

# ---------------------------------------------
# tasc 8
# from random import randint

# class GamePole:
#     __instance = None

#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             cls.__instance = super().__new__(cls)
        
#         return cls.__instance

#     def __init__(self, N, M, total_mines):
#         self.__N = N
#         self.__M = M
#         self.__total_mines = total_mines
#         self.__pole_cells = None
    
#     @property
#     def pole(self):
#         return self.__pole_cells
    
#     def init_pole(self):
#         self.__pole_cells = tuple(tuple(Cell() for _ in range(self.__M)) for _ in range(self.__N))
#         mines = 0
#         while mines < self.__total_mines:
#             x = randint(0, self.__N - 1)
#             y = randint(0, self.__M - 1)
#             if not self.__pole_cells[x][y].is_mine:
#                 self.__pole_cells[x][y].is_mine = True
#                 mines += 1
        
#         for i in range(self.__N):
#             for j in range(self.__M):
#                 if self.__pole_cells[i][j].is_mine:
#                     continue

#                 num_mines = 0
#                 for r_cell in range(i - 1, i + 2):
#                     if r_cell < 0 or r_cell > (self.__N - 1):
#                         continue
#                     for c_cell in range(j - 1, j + 2):
#                         if c_cell < 0 or c_cell > (self.__M - 1) or (r_cell, c_cell) == (i, j):
#                             continue

#                         if self.__pole_cells[r_cell][c_cell].is_mine:
#                             num_mines += 1
                    
#                 self.__pole_cells[i][j].number = num_mines
    
#     def open_cell(self, i, j):
#         if isinstance(i, bool) or isinstance(j, bool) or not isinstance(i, int) or not isinstance(j, int) or i < 0 or j < 0 or i >= self.__N or j >= self.__M:
#             raise IndexError("некорректные индексы i, j клетки игрового поля")
        
#         self.__pole_cells[i][j].is_open = True
    
#     def show_pole(self):
#         for i in self.__pole_cells:
#             for j in i:
#                 if j.is_mine:
#                     print("*", end=" ")
#                 else:
#                     print(j.number, end=" ")
            
#             print("")


# class Cell:
#     def __init__(self):
#         self.__is_mine = False
#         self.__number = 0
#         self.__is_open = False
    
#     @property
#     def is_mine(self):
#         return self.__is_mine
    
#     @is_mine.setter
#     def is_mine(self, mine):
#         if not isinstance(mine, bool):
#             raise ValueError("недопустимое значение атрибута")
        
#         self.__is_mine = mine
    
#     @property
#     def number(self):
#         return self.__number
    
#     @number.setter
#     def number(self, num):
#         if isinstance(num, bool) or not isinstance(num, int) or num < 0 or num > 8:
#             raise ValueError("недопустимое значение атрибута")
        
#         self.__number = num

#     @property
#     def is_open(self):
#         return self.__is_open
    
#     @is_open.setter
#     def is_open(self, flag):
#         if not isinstance(flag, bool):
#             raise ValueError("недопустимое значение атрибута")
        
#         self.__is_open = flag
    
#     def __bool__(self):
#         if self.__is_open:
#             return False
        
#         return True

# pole = GamePole(10, 10, 35)
# pole.init_pole()
# pole.show_pole()

# -----------------------------------------------
# tasc 9
class Vector:
    def __init__(self, *args):
        self.coords = list(args)
    
    def eq_list(self, oth_list):
        return len(self.coords) == len(oth_list.coords)
    
    def __add__(self, other):
        if not self.eq_list(other):
            raise ArithmeticError("размерности векторов не совпадают")
            
        return Vector(*(a + b for a, b in zip(self.coords, other.coords)))
    
    def __iadd__(self, other):
        if isinstance(other, (int, float)):
            for i in range(len(self.coords)):
                self.coords[i] += other
        else:
            if not self.eq_list(other):
                raise ArithmeticError("размерности векторов не совпадают")
            
            for i in range(len(self.coords)):
                self.coords[i] += other.coords[i]
        
        return self
        
    def __sub__(self, other):
        if not self.eq_list(other):
            raise ArithmeticError("размерности векторов не совпадают")
        
        return Vector(*(a - b for a, b in zip(self.coords, other.coords)))
    
    def __isub__(self, other):
        if isinstance(other, (int, float)):
            for i in range(len(self.coords)):
                self.coords[i] -= other
        else:
            if not self.eq_list(other):
                raise ArithmeticError("размерности векторов не совпадают")
            
            for i in range(len(self.coords)):
                self.coords[i] -= other.coords[i]
        
        return self
    
    def __mul__(self, other):
        if not self.eq_list(other):
            raise ArithmeticError("размерности векторов не совпадают")
        
        return Vector(*(a * b for a, b in zip(self.coords, other.coords)))
    
    def __eq__(self, other):
        return self.coords == other.coords
    
a = Vector(1, 2, 3)
b = Vector(1, 2, 4)
print(a != b)