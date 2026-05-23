# tasc 4
# class NewList:
#     def __init__(self, lst=None):
#         self.__lst = [] if lst is None else lst
    
#     def get_list(self):
#         return self.__lst
        
#     def __sub__(self, other):
#         if not isinstance(other, (list, NewList)):
#             raise TypeError("Правый операнд должен быть типом list или объектом NewList")
                
#         if isinstance(other, list):
#             lst = list(other)
#         else:
#             lst = list(other.get_list())
        
#         lst_new = []
        
#         for i in self.__lst:
#             if i not in lst:
#                 lst_new.append(i)
#             else:
#                 lst.remove(i)

#         return NewList(lst_new)
    
#     def __rsub__(self, other):
#         return NewList(other).__sub__(list(self.__lst))




# a = NewList()
# b = NewList()
# a.get_list().append(99)
# print(b.get_list())
# print(a.get_list() is b.get_list())

# -------------------------------------------------------------------

# tasc 5
# class ListMath:
#     def __init__(self, lst_math=None):
#         if lst_math == None:
#             self.lst_math = []
#         else:
#             self.lst_math = list(i for i in lst_math if type(i) in (int, float))
    
#     def get_lst_math(self):
#         return self.lst_math

#     def __add__(self, other):
#         new_lst = list(i + other for i in self.lst_math)
#         return ListMath(new_lst)
    
#     def __radd__(self, other):
#         new_lst = list(i + other for i in self.lst_math)
#         return ListMath(new_lst)
    
#     def __iadd__(self, other):
#         for i in range(len(self.lst_math)):
#             self.lst_math[i] += other
#         return self
    
#     def __sub__(self, other):
#         new_lst = list(i - other for i in self.lst_math)
#         return ListMath(new_lst)
    
#     def __rsub__(self, other):
#         new_lst = list(other - i for i in self.lst_math)
#         return ListMath(new_lst)
    
#     def __isub__(self, other):
#         for i in range(len(self.lst_math)):
#             self.lst_math[i] -= other
#         return self
    
#     def __mul__(self, other):
#         new_lst = list(i * other for i in self.lst_math)
#         return ListMath(new_lst)
    
#     def __rmul__(self, other):
#         new_lst = list(other * i for i in self.lst_math)
#         return ListMath(new_lst)
    
#     def __imul__(self, other):
#         for i in range(len(self.lst_math)):
#             self.lst_math[i] *= other
#         return self
    
#     def __truediv__(self, other):
#         new_lst = list(i / other for i in self.lst_math)
#         return ListMath(new_lst)
    
#     def __rtruediv__(self, other):
#         new_lst = list(other / i for i in self.lst_math)
#         return ListMath(new_lst)
    
#     def __itruediv__(self, other):
#         for i in range(len(self.lst_math)):
#             self.lst_math[i] /= other
#         return self

# a = ListMath([1, 2, 3])
# a += 10
# print(a.lst_math)

# -------------------------------------------------------------------

# tasc 6
# class StackObj:
#     def __init__(self, data):
#         self.__data = data
#         self.__next = None
    
#     @property
#     def next(self):
#         return self.__next
    
#     @next.setter
#     def next(self, next):
#         self.__next = next
    
#     @property
#     def data(self):
#         return self.__data


# class Stack:
#     def __init__(self):
#         self.__top = None
#         self.__size = 0
    
#     def push_back(self, obj):
#         if self.__size == 0:
#             self.__top = obj
#         else:
#             current = self.__top
#             for i in range(self.__size - 1):
#                 current = current.next
            
#             current.next = obj
        
#         self.__size += 1
    
#     def pop_back(self):
#         if self.__size == 0:
#             return
#         elif self.__size == 1:
#             self.__top = None
#         else:
#             current = self.__top
#             for i in range(self.__size - 2):
#                 current = current.next
            
#             current.next = None
        
#         self.__size -= 1
    
#     def __add__(self, other):
#         self.push_back(other)
#         return self
    
#     def __mul__(self, other):
#         for i in other:
#             self.push_back(StackObj(i))
        
#         return self

# -------------------------------------------------------------------

# tasc 7
# class Book:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year


# class Lib:
#     def __init__(self):
#         self.book_list = []
    
#     def __add__(self, other):
#         self.book_list.append(other)
#         return self
    
#     def __sub__(self, other):
#         if isinstance(other, Book):
#             self.book_list.remove(other)
#         elif isinstance(other, int):
#             del self.book_list[other]
        
#         return self
    
#     def __len__(self):
#         return len(self.book_list)

# -------------------------------------------------------------------

# tasc 8
# class Item:
#     def __init__(self, name, money):
#         self.name = name
#         self.money = money
    
#     def __add__(self, other):
#         return self.money + other.money
    
#     def __radd__(self, other):
#         return self.money + other


# class Budget:
#     def __init__(self):
#         self.cons = []
    
#     def add_item(self, it):
#         self.cons.append(it)
    
#     def remove_item(self, indx):
#         del self.cons[indx]

#     def get_items(self):
#         return self.cons

    
# it1 = Item("it1", 10)
# it2 = Item("it2", 20)
# it3 = Item("it3", 30)
# s = it1 + it2 + it3
# print(s)

# -------------------------------------------------------------------

# tasc 9
# class Box3D:
#     def __init__(self, width, height, depth):
#         self.width = width
#         self.height = height
#         self.depth = depth
    
#     def __add__(self, other):
#         return Box3D(self.width + other.width, self.height + other.height, self.depth + other.depth)
    
#     def __mul__(self, other):
#         return Box3D(self.width * other, self.height * other, self.depth * other)
    
#     def __rmul__(self, other):
#         return Box3D(self.width * other, self.height * other, self.depth * other)
    
#     def __sub__(self, other):
#         return Box3D(self.width - other.width, self.height - other.height, self.depth - other.depth)
    
#     def __floordiv__(self, other):
#         return Box3D(self.width // other, self.height // other, self.depth // other)
    
#     def __mod__(self, other):
#         return Box3D(self.width % other, self.height % other, self.depth % other)
    

# -------------------------------------------------------------------

# tasc 10
class MaxPooling:
    def __init__(self, step=(2, 2), size=(2, 2)):
        self.step = step
        self.size = size
    
    def __call__(self, matrix, *args, **kwds):
        len_1 = len(matrix[0])
        for i in matrix:
            if len(i) != len_1:
                raise ValueError("Неверный формат для первого параметра matrix.")
            
            for j in i:
                if not isinstance(j, (int, float)):
                    raise ValueError("Неверный формат для первого параметра matrix.")
        
        res_main = []
        for i in range(0, len(matrix), self.step[0]):
            res_cur = []

            for j in range(0, len(matrix[0]), self.step[1]):
                window = [row[j : j + self.size[1]] for row in matrix[i : i + self.size[0]]]
                if i + self.size[0] <= len(matrix) and j + self.size[1] <= len(matrix[0]):
                    res_cur.append(max(max(row) for row in window))
            
            if res_cur:
                res_main.append(res_cur)
        
        return res_main


# window = [row[0 : 2] for row in matrix[0 : 2]]

