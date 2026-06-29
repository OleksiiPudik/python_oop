# tasc 2
# class Record:
#     def __init__(self, **kwargs):
#         self.__dict__.update(kwargs)
    
#     def __getitem__(self, key):
#         if isinstance(key, bool) or not isinstance(key, int) or key < 0 or key >= len(self.__dict__):
#             raise IndexError("неверный индекс поля")
        
#         lst_temp = list(self.__dict__.values())

#         return lst_temp[key]
    
#     def __setitem__(self, key, value):
#         if isinstance(key, bool) or not isinstance(key, int) or key < 0 or key >= len(self.__dict__):
#             raise IndexError("неверный индекс поля")
        
#         lst_temp = list(self.__dict__.keys())

#         self.__dict__[lst_temp[key]] = value

# a = Record(aaa=111, bbb=222, ccc=333)
# print(a.bbb)

# ---------------------------------------------------------
# tasc 3
# class Track:
#     def __init__(self, start_x, start_y):
#         self.start_x = start_x
#         self.start_y = start_y
#         self.route = []
    
#     def add_point(self, x, y, speed):
#         self.route.append([(x, y), speed])
    
#     def __getitem__(self, key):
#         if isinstance(key, bool) or not isinstance(key, int) or key < 0 or key >= len(self.route):
#             raise IndexError("некорректный индекс")
        
#         return self.route[key]
    
#     def __setitem__(self, key, value):
#         if isinstance(key, bool) or not isinstance(key, int) or key < 0 or key >= len(self.route):
#             raise IndexError("некорректный индекс")
        
#         self.route[key][1] = value

# tr = Track(1, 2)
# tr.add_point(3, 4, 10)
# tr.add_point(13, 14, 20)
# tr[1] = 30
# c, s = tr[1]
# print(s)

# -----------------------------------------------------------
# tasc 4
class Array:
    def __init__(self, max_length, cell):
        self.cell = cell
        self.arr = []


class Integer:
    def __init__(self, start_value):
        self.__value = start_value
    
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, val):
        if isinstance(val, bool) or not isinstance(val, int):
            raise ValueError("должно быть целое число")
        
        self.__value = val
