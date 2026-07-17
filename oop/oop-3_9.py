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
class Person:
    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job
    
    def _check_index(self, key):
        length = len([v for k, v in self.__dict__.items() if k != "i"])

        if isinstance(key, bool) or not isinstance(key, int) or key < 0 or key >= length:
            raise IndexError("неверный индекс")
    
    def __getitem__(self, key):
        lst_temp = [v for k, v in self.__dict__.items() if k != "i"]

        self._check_index(key)
        
        return lst_temp[key]
    
    def __setitem__(self, key, value):
        lst_temp = [k for k, v in self.__dict__.items() if k != "i"]

        self._check_index(key)
        
        self.__dict__[lst_temp[key]] = value
    
    def __iter__(self):
        self.i = 0
        return self
    
    def __next__(self):
        lst_temp = [v for k, v in self.__dict__.items() if k != "i"]

        if self.i < len(lst_temp):
            value = lst_temp[self.i]
            self.i += 1
            return value
        else:
            raise StopIteration


        
    

pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
pers[0] = 'Балакирев С.М.'
for v in pers:
    print(v)
pers[5] = 123
