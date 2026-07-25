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
# class IterColumn:
#     def __init__(self, lst, column):
#         self.lst = lst
#         self.column = column
    
#     def __iter__(self):
#         self.row = 0
#         self.col = self.column
#         return self
    
#     def __next__(self):
#         if self.row >= len(self.lst):
#             raise StopIteration
        
#         value = self.lst[self.row][self.col]

#         self.row += 1

#         return value

# lst_in = [[1, 2, 3], [5, 6, 7], [8, 9, 10]]
# it = IterColumn(lst_in, 2)
# # for i in it:
# #     print(i)

# it_iter = iter(it)
# print(next(it_iter))
# print(next(it_iter))
# print(next(it_iter))
# print(next(it_iter))

# ------------------------------------------------

# tasc 8
# class StackObj:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class Stack:
#     def __init__(self):
#         self.top = None
            
#     def push_back(self, obj):
#         if self.top is None:
#             self.top = obj
#         else:
#             cur_obj = self.top
#             while cur_obj.next is not None:
#                 cur_obj = cur_obj.next
            
#             cur_obj.next = obj
                
#     def push_front(self, obj):
#         if self.top is None:
#             self.top = obj
#         else:
#             obj.next, self.top = self.top, obj
            
#     def __len__(self):
#         length = 0
#         cur_obj = self.top

#         while cur_obj is not None:
#             length += 1
#             cur_obj = cur_obj.next
        
#         return length
    
#     def _check_index(self, indx):
#         if isinstance(indx, bool) or not isinstance(indx, int) or indx < 0 or indx >= len(self):
#             raise IndexError("неверный индекс")
    
#     def __getitem__(self, key):
#         self._check_index(key)
#         cur_obj = self.top

#         for i in range(key):
#             cur_obj = cur_obj.next
        
#         return cur_obj.data
    
#     def __setitem__(self, key, value):
#         self._check_index(key)
#         cur_obj = self.top
        
#         for i in range(key):
#             cur_obj = cur_obj.next
        
#         cur_obj.data = value
    
#     def __iter__(self):
#         self.cur = self.top
#         return self
    
#     def __next__(self):
#         if self.cur is None:
#             raise StopIteration
        
#         value = self.cur
#         self.cur = self.cur.next
#         return value
        

# st = Stack()
# st.push_back(StackObj("data1"))
# st.push_back(StackObj("data2"))
# st.push_front(StackObj("data3"))

# for obj in st:
#     print(obj.data)
# st[3] = "new_data"
# print(st[5])

# ----------------------------------------

# tasc 9
# class Cell:
#     def __init__(self, data):
#         self.__data = data
    
#     @property
#     def data(self):
#         return self.__data
    
#     @data.setter
#     def data(self, data):
#         self.__data = data

# class TableValues:
#     def __init__(self, rows, cols, type_data=int):
#         self.rows = rows
#         self.cols = cols
#         self.type_data = type_data
#         self.table = [[Cell(0) for _ in range(self.cols)] for _ in range(self.rows)]
    
#     def _check_data(self, d):
#         if type(d) != self.type_data:
#             raise TypeError("неверный тип присваиваемых данных")
    
#     def _check_index(self, r, c):
#         if isinstance(r, bool) or isinstance(c, bool) or not isinstance(r, int) or not isinstance(c, int) or r < 0 or c < 0 or r >= self.rows or c >= self.cols:
#             raise IndexError("неверный индекс")
    
#     def __getitem__(self, key):
#         row, col = key
#         self._check_index(row, col)

#         return self.table[row][col].data
    
#     def __setitem__(self, key, value):
#         row, col = key
#         self._check_data(value)
#         self._check_index(row, col)

#         self.table[row][col].data = value
    
#     def __iter__(self):
#         self.cur_row = 0
#         return self
    
#     def __next__(self):
#         if self.cur_row >= self.rows:
#             raise StopIteration
        
#         value = [c.data for c in self.table[self.cur_row]]
#         self.cur_row += 1

#         return value

# table = TableValues(3, 3)

# class Cell:
#     def __init__(self, data):
#         self.__data = data
    
#     @property
#     def data(self):
#         return self.__data
    
#     @data.setter
#     def data(self, data):
#         self.__data = data


# class TableValues:
#     def __init__(self, rows, cols, type_data=int):
#         self.rows = rows
#         self.cols = cols
#         self.type_data = type_data
#         self.table = [[Cell(0) for _ in range(self.cols)] for _ in range(self.rows)]
    
#     def _check_data(self, d):
#         if type(d) != self.type_data:
#             raise TypeError("неверный тип присваиваемых данных")
    
#     def _check_index(self, r, c):
#         if isinstance(r, bool) or isinstance(c, bool) or not isinstance(r, int) or not isinstance(c, int) or r < 0 or c < 0 or r >= self.rows or c >= self.cols:
#             raise IndexError("неверный индекс")
    
#     def __getitem__(self, key):
#         row, col = key
#         self._check_index(row, col)

#         return self.table[row][col].data
    
#     def __setitem__(self, key, value):
#         row, col = key
#         self._check_index(row, col)
#         self._check_data(value)

#         self.table[row][col].data = value
    
#     def __iter__(self):
#         return TableIterator(self.table)
    
    
# class TableIterator:
#     def __init__(self, table):
#         self.table = table
#         self.cur_row = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.cur_row >= len(self.table):
#             raise StopIteration
        
#         value = [c.data for c in self.table[self.cur_row]]
#         self.cur_row += 1

#         return value


# table = TableValues(3, 3)
# table[0, 0] = 1
# table[1, 1] = 2
# for i in table:
#     print(i, end=" ")

# ----------------------------------------------------

# tasc 10
class Matrix:
    def _check_nums(self, *args):
        r, c, f_v = args
        if isinstance(r, bool) or not isinstance(r, int) or r <= 0:
            raise TypeError("аргументы rows, cols - целые числа; fill_value - произвольное число")

        if isinstance(c, bool) or not isinstance(c, int) or c <= 0:
            raise TypeError("аргументы rows, cols - целые числа; fill_value - произвольное число")

        if isinstance(f_v, bool) or not isinstance(f_v, (int, float)):
            raise TypeError("аргументы rows, cols - целые числа; fill_value - произвольное число")

    def _check_list(self, lst_check):
        for i in lst_check:
            if len(i) != len(lst_check[0]):
                raise TypeError("список должен быть прямоугольным, состоящим из чисел")

            for j in i:
                if isinstance(j, bool) or not isinstance(j, (int, float)):
                    raise TypeError("список должен быть прямоугольным, состоящим из чисел")

    def __init__(self, *args):
        if len(args) == 3:
            self.rows, self.cols, self.fill_value = args
            self._check_nums(self.rows, self.cols, self.fill_value)
            self.matrix = [[self.fill_value for _ in range(self.cols)] for _ in range(self.rows)]
        elif len(args) == 1:
            self._check_list(args[0])
            self.matrix = [list(row) for row in args[0]]
            self.rows = len(self.matrix)
            self.cols = len(self.matrix[0])

    def _check_index(self, row_indx, col_indx):
        if isinstance(row_indx, bool) or isinstance(col_indx, bool) or not isinstance(row_indx, int) or not isinstance(col_indx, int) or row_indx < 0 or col_indx < 0 or row_indx >= self.rows or col_indx >= self.cols:
            raise IndexError("недопустимые значения индексов")

    def __getitem__(self, key):
        row, col = key
        self._check_index(row, col)
        return self.matrix[row][col]

    def _check_value(self, row_val, col_val, val_val):
        self._check_index(row_val, col_val)

        if isinstance(val_val, bool) or not isinstance(val_val, (int, float)):
            raise TypeError("значения матрицы должны быть числами")

    def __setitem__(self, key, value):
        row, col = key
        self._check_value(row, col, value)

        self.matrix[row][col] = value

    def _check_len_matrix(self, other_matrix):
        if self.rows != other_matrix.rows or self.cols != other_matrix.cols:
            raise ValueError("операции возможны только с матрицами равных размеров")

    def __add__(self, other):
        if isinstance(other, (int, float)):
            lst = [list(j + other for j in i) for i in self.matrix]
            return Matrix(lst)
        else:
            self._check_len_matrix(other)
            lst = [list(self.matrix[i][j] + other.matrix[i][j] for j in range(self.cols)) for i in range(self.rows)]
            return Matrix(lst)

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            lst = [list(j - other for j in i) for i in self.matrix]
            return Matrix(lst)
        else:
            self._check_len_matrix(other)
            lst = [list(self.matrix[i][j] - other.matrix[i][j] for j in range(self.cols)) for i in range(self.rows)]
            return Matrix(lst)

    
    
            

m1 = Matrix(2, 2, 3)
m2 = Matrix([[1, 1], [1, 1]])
print(m1.matrix)
print(m2.matrix)
print(m1[0, 0])
m2[0, 0] = True





