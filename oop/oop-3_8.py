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
# task 4
# class Array:
#     def __init__(self, max_length, cell):
#         self.max_length = max_length
#         self.arr = [cell(0) for _ in range(max_length)]
    
#     def __getitem__(self, key):
#         if isinstance(key, bool) or not isinstance(key, int) or key < 0 or key >= self.max_length:
#             raise IndexError("неверный индекс для доступа к элементам массива")
        
#         return self.arr[key].value
    
#     def __setitem__(self, key, val):
#         if isinstance(key, bool) or not isinstance(key, int) or key < 0 or key >= self.max_length:
#             raise IndexError("неверный индекс для доступа к элементам массива")
        
#         self.arr[key].value = val


# class Integer:
#     def __init__(self, start_value):
#         self.value = start_value
    
#     @property
#     def value(self):
#         return self.__value
    
#     @value.setter
#     def value(self, val):
#         if isinstance(val, bool) or not isinstance(val, int):
#             raise ValueError("должно быть целое число")
        
#         self.__value = val

# ----------------------------------------------------------

# task 5
class IntegerValue:
    def __set_name__(self, owner, name):
        self.name = "_" + name
    
    def __get__(self, instance, owner):
        return getattr(instance, self.name)
    
    def __set__(self, instance, value):
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError("возможны только целочисленные значения")
        
        setattr(instance, self.name, value)


class CellInteger:
    value = IntegerValue()

    def __init__(self, start_value=0):
        self.value = start_value

class TableValues:
    def __init__(self, rows, cols, cell=None):
        if cell is None:
            raise ValueError("параметр cell не указан")
        else:
            self.cells = tuple(tuple(cell() for _ in range(cols)) for _ in range(rows))
    
    def __getitem__(self, key):
        r, c = key
        return self.cells[r][c].value
    
    def __setitem__(self, key, val):
        r, c = key
        self.cells[r][c].value = val


tb = TableValues(1, 2, CellInteger)
tb[0, 0] = 3.5
print(tb[0, 0])
        
        
