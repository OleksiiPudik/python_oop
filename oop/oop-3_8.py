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
# class IntegerValue:
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
    
#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)
    
#     def __set__(self, instance, value):
#         if isinstance(value, bool) or not isinstance(value, int):
#             raise ValueError("возможны только целочисленные значения")
        
#         setattr(instance, self.name, value)


# class CellInteger:
#     value = IntegerValue()

#     def __init__(self, start_value=0):
#         self.value = start_value

# class TableValues:
#     def __init__(self, rows, cols, cell=None):
#         if cell is None:
#             raise ValueError("параметр cell не указан")
#         else:
#             self.cells = tuple(tuple(cell() for _ in range(cols)) for _ in range(rows))
    
#     def __getitem__(self, key):
#         r, c = key
#         return self.cells[r][c].value
    
#     def __setitem__(self, key, val):
#         r, c = key
#         self.cells[r][c].value = val


# tb = TableValues(1, 2, CellInteger)
# tb[0, 0] = 3.5
# print(tb[0, 0])
        
# ---------------------------------------------------------------------
# task 6
class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None
    
    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self, next):
        self.__next = next
    
    @property
    def data(self):
        return self.__data


class Stack:
    def __init__(self):
        self.top = None
        self.stack_count = 0
    
    def push(self, obj):
        if self.top is None:
            self.top = obj
            self.stack_count += 1
        else:
            cur_stack = self.top
                       
            while cur_stack.next is not None:
                cur_stack = cur_stack.next
            
            cur_stack.next = obj
            self.stack_count += 1
    
    def pop(self):
        if self.stack_count == 0:
            return self.top
        elif self.stack_count == 1:
            pop_obj = self.top
            self.top = None
            self.stack_count = 0
            return pop_obj
        else:
            prev_stack = self.top
            cur_stack = self.top.next

            while cur_stack.next is not None:
                prev_stack, cur_stack = prev_stack.next, cur_stack.next
            
            prev_stack.next = None
            self.stack_count -= 1

            return cur_stack
    
    def __getitem__(self, key):
        if isinstance(key, bool) or not isinstance(key, int) or key < 0 or key >= self.stack_count:
            raise IndexError("неверный индекс")
        elif key == 0:
            return self.top
        else:
            get_obj = self.top
            for i in range(key):
                get_obj = get_obj.next
            
            return get_obj
    
    def __setitem__(self, key, value):
        if isinstance(key, bool) or not isinstance(key, int) or key < 0 or key >= self.stack_count:
            raise IndexError("неверный индекс")
        elif key == 0:
            value.next, self.top = self.top.next, value
            # next_obj = self.top.next
            # self.top = value
            # self.top.next = next_obj
        else:
            prev_obj = self.top
            cur_obj = self.top.next
            next_obj = cur_obj.next

            for i in range(1, key):
                prev_obj, cur_obj, next_obj = prev_obj.next, cur_obj.next, next_obj.next
            
            cur_obj = value
            prev_obj.next, cur_obj.next = cur_obj, next_obj


