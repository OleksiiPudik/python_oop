# class SmartPhone:
#     pass


# class IPhone(SmartPhone):
#     pass


# phone = IPhone()
# print(issubclass(phone, SmartPhone))


# -------------------------------

# tasc 3

# class ListInteger(list):
#     def __init__(self, iterable):
#         for i in iterable:
#             self.append(i)

#     def append(self, object):
#         if isinstance(object, bool) or not isinstance(object, int):
#             raise TypeError("можно передавать только целочисленные значения")
        
#         return super().append(object)

#     def __setitem__(self, key, value):
#         if isinstance(value, bool) or not isinstance(value, int):
#             raise TypeError("можно передавать только целочисленные значения")
        
#         return super().__setitem__(key, value)


# s = ListInteger((1, 2, 3))
# s[1] = 20
# print(s)

# ----------------------------------------

# tasc 4

class Thing:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __hash__(self):
        return hash((self.name, self.price, self.weight))

    def __eq__(self, value):
        if not isinstance(value, Thing):
            return False
        
        return (self.name, self.price, self.weight) == (value.name, value.price, value.weight)


class DictShop(dict):
    def __init__(self, iterable={}):
        if not isinstance(iterable, dict):
            raise TypeError("аргумент должен быть словарем")

        for i in iterable.keys():
            if not isinstance(i, Thing):
                raise TypeError("ключами могут быть только объекты класса Thing")
        
        super().__init__(iterable)
        
# на следующий раз нужно подумать как не дублировать проверку в __setitem__, нужно посмотреть что общего в ините и сетитеме


    

thing1 = Thing("name_1", 1, 2)
thing2 = Thing("name_2", 3, 4)
dict_things = DictShop({thing1: thing1, thing2: thing2})

# d = {}
# # print(Thing.__hash__)
# d[thing1] = thing1
# d[thing2] = thing2
# print(len(d))
# print("abc" == 5)
# print([1, 2] == 5)
# print((1, 2) == 5)

# class A:
#     pass


# obj = A()
# obj.bb = 5
# print(obj.__dict__)
# obj.__dict__['bb'] = 6
# print(obj.__dict__)
# print(obj.bb)

# class C(dict):
#     x = 1
#     pass


# obj = C()
# obj.dd = 7
# obj['dd'] = 5
# print(obj.__dict__)
# print(obj)
# print(obj.x)
# obj['x'] = 2
# print(obj['x'])


# class E(dict):
#     def __setitem__(self, key, value):
#         print("call func Setitem")
#         return super().__setitem__(key, value)
    

# obj_e = E({3: 3, 4: 4})
# obj_e[1] = 1
# obj_e[2] = 2
# print(obj_e)
# Вывод для DictShop: проверка в __setitem__ не защищает словарь который передается при создании экземпляра. 
# при создании экземпляра отрабатывает __init__ который обходит __setitem__. поэтому проверку нужно писать две проверки
# одну в __init__ а другую в __setitem__.