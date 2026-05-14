# tasc 2
# import sys

# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
    
#     def __str__(self):
#         return f"Книга: {self.title}; {self.author}; {self.pages}"

# lst_in = list(map(str.strip, sys.stdin.readlines()))
# book = Book(lst_in[0], lst_in[1], lst_in[2])
# print(book)

# ------------------------------------------------------------------------
# tasc 3
# class Model:
#     def __init__(self):
#         self.data = {}

#     def query(self, **kwargs):
#         self.data = kwargs
    
#     def __str__(self):
#         if self.data == {}:
#             return "Model"
        
#         return f"Model: {', '.join(f'{key} = {value}' for key, value in self.data.items())}"

# model = Model()
# model.query(id=1, fio="Sergey", age=50)
# print(model)

# ------------------------------------------------------------------------
# tasc 4
# class WordString:
#     def __init__(self, string=""):
#         self.__string = string
#         self.__lst = [] if self.__string == "" else self.__string.split()
    
#     @property
#     def string(self):
#         return self.__string
    
#     @string.setter
#     def string(self, value):
#         self.__string = value
#         self.__lst = self.__string.split()
    
    
#     # def __setattr__(self, name, value):
#     #     if name == "string":
#     #         self.lst = value.split()
#     #         object.__setattr__(self, name, value)
#     #     else:
#     #         object.__setattr__(self, name, value)

#     def __call__(self, indx, *args, **kwds):
#         return self.__lst[indx]
    
#     def __len__(self):
#         return len(self.__lst)

# words = WordString()
# words.string = "Python course OOP"
# n = len(words)
# first = "" if n == 0 else words(0)
# print(words.string)
# print(f"Num words: {n}; first word: {first}")

# ------------------------------------------------------------------------

# tasc 5
# class ObjList:
#     def __init__(self, data):
#         self.__data = data
#         self.__prev = None
#         self.__next = None
    
#     @property
#     def prev(self):
#         return self.__prev
    
#     @prev.setter
#     def prev(self, prev):
#         self.__prev = prev

#     @property
#     def next(self):
#         return self.__next
    
#     @next.setter
#     def next(self, next):
#         self.__next = next
    
#     @property
#     def data(self):
#         return self.__data


# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.size = 0
            
#     def add_obj(self, obj):
#         if self.size == 0:
#             self.head = self.tail = obj
#         else:
#             obj.prev = self.tail
#             self.tail.next = obj
#             self.tail = obj
#         self.size += 1
    
#     def remove_obj(self, indx):
#         if self.size == 1:
#             self.head = self.tail = None
#         else:
#             current = self.head
#             for i in range(indx):
#                 current = current.next
            
#             if current.prev is not None:
#                 current.prev.next = current.next
#             else:
#                 self.head = current.next
            
#             if current.next is not None:
#                 current.next.prev = current.prev
#             else:
#                 self.tail = current.prev
            
        
#         self.size -= 1
    
#     def __call__(self, indx, *args, **kwds):
#         current = self.head
#         for i in range(indx):
#             current = current.next
        
#         return current.data
    
#     def __len__(self):
#         return self.size

# ------------------------------------------------------------------------

# tasc 6
# import math

# class Complex:
#     def __init__(self, real, img):
#         if type(real) not in (int, float) or type(img) not in (int, float):
#             raise ValueError("Неверный тип данных")
#         self.__real = real
#         self.__img = img
    
#     @property
#     def real(self):
#         return self.__real
    
#     @real.setter
#     def real(self, real):
#         if type(real) not in (int, float):
#             raise ValueError("Неверный тип данных")
#         self.__real = real
    
#     @property
#     def img(self):
#         return self.__img
    
#     @img.setter
#     def img(self, img):
#         if type(img) not in (int, float):
#             raise ValueError("Неверный тип данных")
#         self.__img = img
    
#     def __abs__(self):
#         return math.sqrt(self.__real**2 + self.__img**2)

# cmp = Complex(7, 8)
# cmp.real = 3
# cmp.img = 4
# c_abs = abs(cmp)
# print(c_abs)

# ------------------------------------------------------------------------

# tasc 7
# import math

# class RadiusVector:
#     def __init__(self, *args):
#         if len(args) == 1:
#             self.__coords = [0 for i in range(args[0])]
#         else:
#             self.__coords = [*args]

#     def get_coords(self):
#         return tuple(self.__coords)
    
#     def set_coords(self, *args):
#         for i in range(min(len(self.__coords), len(args))):
#             self.__coords[i] = args[i]
    
#     def __len__(self):
#         return len(self.__coords)
    
#     def __abs__(self):
#         return math.sqrt(sum(i**2 for i in self.__coords))

# ------------------------------------------------------------------------

# tasc 8
# class Clock:
#     def __init__(self, hours, minutes, seconds):
#         self.__hours = hours
#         self.__minutes = minutes
#         self.__seconds = seconds
    
#     def get_time(self):
#         return self.__hours * 3600 + self.__minutes * 60 + self.__seconds
    

# class DeltaClock:
#     def __init__(self, clock1, clock2):
#         self.__clock1 = clock1
#         self.__clock2 = clock2
    
#     def __str__(self):
#         dif = self.__clock1.get_time() - self.__clock2.get_time()
#         h = dif // 3600
#         m = (dif % 3600) // 60
#         s = dif - h * 3600 - m * 60
#         return "00: 00: 00" if dif <= 0 else f"{h:02d}: {m:02d}: {s:02d}"
    
#     def __len__(self):
#         dif = self.__clock1.get_time() - self.__clock2.get_time()
#         return 0 if dif <= 0 else dif

# ------------------------------------------------------------------------

# tasc 9
# class Ingredient:
#     def __init__(self, name, volume, measure):
#         self.__name = name
#         self.__volume = volume
#         self.__measure = measure
    
#     def __str__(self):
#         return f"{self.__name}: {self.__volume}, {self.__measure}"


# class Recipe:
#     def __init__(self, *args):
#         self.__ingredients = [*args]
    
#     def add_ingredient(self, ing):
#         self.__ingredients.append(ing)
    
#     def remove_ingredient(self, ing):
#         self.__ingredients.remove(ing)
    
#     def get_ingredients(self):
#         return tuple(self.__ingredients)
    
#     def __len__(self):
#         return len(self.__ingredients)

# ------------------------------------------------------------------------

# tasc 10
class PolyLine:
    def __init__(self, *args):
        self.__coords = list(args)
    
    def add_coord(self, x, y):
        self.__coords.append((x, y))
    
    def remove_coord(self, indx):
        del self.__coords[indx]
    
    def get_coords(self):
        return self.__coords
