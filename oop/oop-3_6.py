# tasc 4
# class Rect:
#     def __init__(self, x, y, width, height):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
    
#     # def __eq__(self, other):
#     #     return self.width == other.width and self.height == other.height
    
#     def __hash__(self):
#         return hash((self.width, self.height))

# r1 = Rect(10, 5, 100, 50)
# r2 = Rect(-10, 4, 100, 50)
# h1, h2 = hash(r1), hash(r2)
# print(h1 == h2)
# print(h1, h2, sep="\n")

# ----------------------------------------------
# tasc 6
# import sys
# class ShopItem:
#     def __init__(self, name, weight, price):
#         self.name = name
#         self.weight = weight
#         self.price = price
    
#     def __hash__(self):
#         return hash((self.name.lower(), self.weight, self.price))
    
#     def __eq__(self, other):
#         return (self.name.lower(), self.weight, self.price) == (other.name.lower(), other.weight, other.price)


# lst_in = list(map(str.strip, sys.stdin.readlines()))

# lst_1 = []
# for i in lst_in:
#     name, numbers = i.split(":")
#     name = name.strip()
#     weight, price = map(float, numbers.split())
#     lst_1.append([name, weight, price])

# shop_items = {}
# for i in lst_1:
#     item = ShopItem(*i)
#     if item not in shop_items:
#         shop_items[item] = [item, 1]
#     else:
#         shop_items[item][1] += 1

# print(shop_items)


# ----------------------------------------------
# tasc 7
# import sys
# class DataBase:
#     def __init__(self, path):
#         self.path = path
#         self.dict_db = {}
    
#     def write(self, record):
#         if record in self.dict_db:
#             self.dict_db[record].append(record)
#         else:
#             self.dict_db[record] = [record]

#     def read(self, pk):
#         for value in self.dict_db.values():
#             for obj in value:
#                 if pk == obj.pk:
#                     return obj
        
#         return None


# class Record:
#     PK = 1

#     def __init__(self, fio, descr, old):
#         self.fio = fio
#         self.descr = descr
#         self.old = old
#         self.pk = Record.PK
#         Record.PK += 1
    
#     def __hash__(self):
#         return hash((self.fio.lower(), self.old))
    
#     def __eq__(self, other):
#         return (self.fio.lower(), self.old) == (other.fio.lower(), other.old)
    

# lst_in = list(map(str.strip, sys.stdin.readlines()))

# db = DataBase("some path")

# for i in lst_in:
#     fio_in, descr_in, old_in = i.split(";")
#     fio_in, descr_in, old_in = fio_in.strip(), descr_in.strip(), int(old_in.strip())
#     db.write(Record(fio_in, descr_in, old_in))


# ----------------------------------------------
# tasc 8
# import sys
# class BookStudy:
#     def __init__(self, name, author, year):
#         self.name = name
#         self.author = author
#         self.year = year
    
#     def __hash__(self):
#         return hash((self.name.lower(), self.author.lower()))
    
#     def __eq__(self, other):
#         return (self.name.lower(), self.author.lower()) == (other.name.lower(), other.author.lower())


# lst_in = list(map(str.strip, sys.stdin.readlines()))

# lst_bs = []
# for i in lst_in:
#     name_in, author_in, year_in = i.split(";")
#     name_in, author_in, year_in = name_in.strip(), author_in.strip(), int(year_in.strip())
#     lst_bs.append(BookStudy(name_in, author_in, year_in))

# s = set()
# for i in lst_bs:
#     s.add(i)

# unique_books = len(s)

# print(s)
# print(unique_books)

# ----------------------------------------------
# tasc 9
# class Dimensions:
#     def __init__(self, a, b, c):
#         if a <= 0 or b <= 0 or c <= 0:
#             raise ValueError("Габаритные размеры должны быть положительными числами")
#         self.a = a
#         self.b = b
#         self.c = c
    
#     def __eq__(self, other):
#         return (self.a, self.b, self.c) == (other.a, other.b, other.c)
    
#     def __hash__(self):
#         return hash((self.a, self.b, self.c))
    


# str_in = input()
# lst_dims = []
# for i in str_in.split(";"):
#     a_in, b_in, c_in = i.split()
#     a_in, b_in, c_in = float(a_in.strip()), float(b_in.strip()), float(c_in.strip())
#     lst_dims.append(Dimensions(a_in, b_in, c_in))

# lst_dims.sort(key=hash)
# print(lst_dims)
# for i in lst_dims:
#     print(i.a, i.b, i.c)

# ----------------------------------------------
# tasc 10
import math
class Side:
    
    def __set_name__(self, owner, name):
        self.name = "_" + name
 
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
 
    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("длины сторон треугольника должны быть положительными числами")
        instance.__dict__[self.name] = value


class Triangle:
    a = Side()
    b = Side()
    c = Side()

    def __init__(self, a, b, c):
        if a >= b + c or b >= c + a or c >= a + b:
            raise ValueError("с указанными длинами нельзя образовать треугольник")
        self.a = a
        self.b = b
        self.c = c
    
    def __len__(self):
        return int(self.a + self.b + self.c)
    
    def __call__(self, *args, **kwds):
        p = (self.a + self.b + self.c) / 2
        s = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        return s
