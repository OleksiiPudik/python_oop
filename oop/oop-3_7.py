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
from random import randint

class GamePole:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        
        return cls.__instance

    def __init__(self, N, M, total_mines):
        self.__N = N
        self.__M = M
        self.__total_mines = total_mines
        self.__pole_cells = None
    
    @property
    def pole(self):
        return self.__pole_cells
    
    def init_pole(self):
        self.__pole_cells = tuple(tuple(Cell() for _ in range(self.__M)) for _ in range(self.__N))

    


class Cell:
    def __init__(self):
        self.__is_mine = False
        self.__number = 0
        self.__is_open = False
    
    @property
    def is_mine(self):
        return self.__is_mine
    
    @is_mine.setter
    def is_mine(self, mine):
        if not isinstance(mine, bool):
            raise ValueError("недопустимое значение атрибута")
        
        self.__is_mine = mine
    
    @property
    def number(self):
        return self.__number
    
    @number.setter
    def number(self, num):
        if isinstance(num, bool) or not isinstance(num, int) or num < 0 or num > 8:
            raise ValueError("недопустимое значение атрибута")
        
        self.__number = num

    @property
    def is_open(self):
        return self.__is_open
    
    @is_open.setter
    def is_open(self, flag):
        if not isinstance(flag, bool):
            raise ValueError("недопустимое значение атрибута")
        
        self.__is_open = flag
    
    def __bool__(self):
        if self.__is_open:
            return False
        
        return True