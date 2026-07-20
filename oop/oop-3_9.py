# class Counter:
#     def __init__(self, count):
#         self.count = count
        
    
#     # def __iter__(self):
#     #     self.cur_count = 1
#     #     return self
    
#     def __next__(self):
#         if self.cur_count <= self.count:
#             temp_count = self.cur_count
#             self.cur_count += 1
#             return temp_count
#         else:
#             raise StopIteration

# r = Counter(5)
# for i in r:
#     print(i)

# --------------------------------------
# tasc 5
# class Person:
#     def __init__(self, fio, job, old, salary, year_job):
#         self.fio = fio
#         self.job = job
#         self.old = old
#         self.salary = salary
#         self.year_job = year_job
    
#     def _values(self):
#         return [v for k, v in self.__dict__.items() if k != "i"]
    
#     def _check_index(self, key):
#         length = len(self._values())

#         if isinstance(key, bool) or not isinstance(key, int) or key < 0 or key >= length:
#             raise IndexError("неверный индекс")
    
#     def __getitem__(self, key):
#         lst_temp = self._values()

#         self._check_index(key)
        
#         return lst_temp[key]
    
#     def __setitem__(self, key, value):
#         lst_temp = [k for k, v in self.__dict__.items() if k != "i"]

#         self._check_index(key)
        
#         self.__dict__[lst_temp[key]] = value
    
#     def __iter__(self):
#         self.i = 0
#         return self
    
#     def __next__(self):
#         lst_temp = self._values()

#         if self.i < len(lst_temp):
#             value = lst_temp[self.i]
#             self.i += 1
#             return value
#         else:
#             raise StopIteration


        
    

# pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
# pers[0] = 'Балакирев С.М.'
# for v in pers:
#     print(v)
# pers[5] = 123
# ---------------------------------------------------
# tasc 6
# class TriangleListIterator:
#     def __init__(self, lst):
#         self.lst = lst
    
#     def __iter__(self):
#         self.row = 0
#         self.col = 0
#         return self
    
#     def __next__(self):
#         if self.row >= len(self.lst):
#             raise StopIteration
        
#         value = self.lst[self.row][self.col]

#         if self.col < self.row:
#             self.col += 1
#         else:
#             self.row += 1
#             self.col = 0
        
#         return value

# lst = [[1], [2, 3], [4]]   # строке 2 нужно 3 элемента, а там 1
# it = TriangleListIterator(lst)
# for x in it:
#     print(x, end=' ')

# -------------------------------------------------

# tasc 7
class IterColumn:
    def __init__(self, lst, column):
        self.lst = lst
        self.column = column
    
    def __iter__(self):
        self.row = 0
        self.col = self.column
        return self
    
    def __next__(self):
        if self.row >= len(self.lst):
            raise StopIteration
        
        value = self.lst[self.row][self.col]

        self.row += 1

        return value

lst_in = [[1, 2, 3], [5, 6, 7], [8, 9, 10]]
it = IterColumn(lst_in, 2)
# for i in it:
#     print(i)

it_iter = iter(it)
print(next(it_iter))
print(next(it_iter))
print(next(it_iter))
print(next(it_iter))