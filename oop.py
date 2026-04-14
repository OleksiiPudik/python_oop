# Task 4
# class Shop:
#     def __init__(self, name):
#         self.name = name
#         self.goods = []
#
#     def add_product(self, product):
#         self.goods.append(product)
#
#     def remove_product(self, product):
#         self.goods.remove(product)
#
#
# class Product:
#     __id = 0
#
#     def __init__(self, name, weight, price):
#         Product.__id += 1
#         self.id = Product.__id
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     def __setattr__(self, key, value):
#         if key == "name" and not isinstance(value, str):
#             raise TypeError("Неверный тип присваиваемых данных.")
#         elif key in ("weight", "price") and not isinstance(value, (int, float)):
#             raise TypeError("Неверный тип присваиваемых данных.")
#         elif key == "id" and not isinstance(value, int):
#             raise TypeError("Неверный тип присваиваемых данных.")
#         else:
#             object.__setattr__(self, key, value)
#
#     def __delattr__(self, item):
#         if item == "id":
#             raise AttributeError("Атрибут id удалять запрещено.")
import time
from itertools import count
from typing import Any


# Task 5
# class Course:
#     def __init__(self, name):
#         self.name = name
#         self.modules = []
#
#     def add_module(self, module):
#         self.modules.append(module)
#
#     def remove_module(self, indx):
#         del self.modules[indx]
#
#
# class Module:
#     def __init__(self, name):
#         self.name = name
#         self.lessons = []
#
#     def add_lesson(self, lesson):
#         self.lessons.append(lesson)
#
#     def remove_lesson(self, indx):
#         del self.lessons[indx]
#
#
# class LessonItem:
#     def __init__(self, title, practices, duration):
#         self.title = title
#         self.practices = practices
#         self.duration = duration
#
#     def __setattr__(self, key, value):
#         if key == "title" and not isinstance(value, str):
#             raise TypeError("Неверный тип присваиваемых данных.")
#         elif key in ("practices", "duration") and not isinstance(value, int):
#             raise TypeError("Неверный тип присваиваемых данных.")
#         else:
#             object.__setattr__(self, key, value)
#
#     def __getattr__(self, item):
#         return False
#
#     def __delattr__(self, item):
#         if item in ("title", "practices", "duration"):
#             raise AttributeError(f"Атрибут {item} удалять запрещено.")


# Task 6
# class Picture:
#     def __init__(self, name, author, descr):
#         self.name = name
#         self.author = author
#         self.descr = descr
#
#     def get_info_exhibit(self):
#         return f"Описание экспоната {self.name}: {self.descr}"
#
#
# class Mummies:
#     def __init__(self, name, location, descr):
#         self.name = name
#         self.locatio = location
#         self.descr = descr
#
#     def get_info_exhibit(self):
#         return f"Описание экспоната {self.name}: {self.descr}"
#
# class Papyri:
#     def __init__(self, name, date, descr):
#         self.name = name
#         self.date = date
#         self.descr = descr
#
#     def get_info_exhibit(self):
#         return f"Описание экспоната {self.name}: {self.descr}"
#
#
# class Museum:
#     def __init__(self, name):
#         self.name = name
#         self.exhibits = []
#
#     def add_exhibit(self, obj):
#         self.exhibits.append(obj)
#
#     def remove_exhibit(self, obj):
#         self.exhibits.remove(obj)
#
#     def get_info_exhibit(self, indx):
#         return self.exhibits[indx].get_info_exhibit()



# Task 7
# class SmartPhone:
#     def __init__(self, model):
#         self.model = model
#         self.apps = []
#
#     def add_app(self, app):
#         if not any(type(a) == type(app) for a in self.apps):
#             self.apps.append(app)
#         else:
#             print("This app is already in Phone")
#
#     def remove_app(self, app):
#         self.apps.remove(app)
#
#
# class AppVK:
#     def __init__(self, name="ВКонтакте"):
#         self.name = name
#
#
# class AppYouTube:
#     def __init__(self, memory_max=0, name="YouTube"):
#         self.memory_max = memory_max
#         self.name = name
#
#
# class AppPhone:
#     def __init__(self, phone_list=None, name="Phone"):
#         self.phone_list = phone_list if phone_list is not None else {}
#         self.name = name



# Task 8
# class Circle:
#     def __init__(self, x, y, radius):
#         self.__x = x
#         self.__y = y
#         self.__radius = radius
#
#     @property
#     def x(self):
#         return self.__x
#
#     @property
#     def y(self):
#         return self.__y
#
#     @property
#     def radius(self):
#         return self.__radius
#
#     @x.setter
#     def x(self, value):
#         if isinstance(value, (int, float)):
#             self.__x = value
#         elif not isinstance(value, (int, float)):
#             raise TypeError("Неверный тип присваиваемых данных")
#
#     @y.setter
#     def y(self, value):
#         if isinstance(value, (int, float)):
#             self.__y = value
#         else:
#             raise TypeError("Неверный тип присваиваемых данных")
#
#     @radius.setter
#     def radius(self, value):
#         if isinstance(value, (int, float)) and value > 0:
#             self.__radius = value
#         elif not isinstance(value, (int, float)):
#             raise TypeError("Неверный тип присваиваемых данных")
#
#
#     def __getattr__(self, item):
#         return False



# Task 9
# class Dimensions:
#     MIN_DIMENSION = 10
#     MAX_DIMENSION = 1000
#
#     @classmethod
#     def __validation(cls, value):
#         return isinstance(value, (int, float)) and cls.MIN_DIMENSION <= value <= cls.MAX_DIMENSION
#
#     def __init__(self, a, b, c):
#         self.__a = self.__b = self.__c = None
#         self.a = a
#         self.b = b
#         self.c = c
#
#     @property
#     def a(self):
#         return self.__a
#
#     @a.setter
#     def a(self, value):
#         if self.__validation(value):
#             self.__a = value
#
#     @property
#     def b(self):
#         return self.__b
#
#     @b.setter
#     def b(self, value):
#         if self.__validation(value):
#             self.__b = value
#
#     @property
#     def c(self):
#         return self.__c
#
#     @c.setter
#     def c(self, value):
#         if self.__validation(value):
#             self.__c = value
#
#     def __setattr__(self, key, value):
#         if key in ("MIN_DIMENSION", "MAX_DIMENSION"):
#             raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
#         super().__setattr__(key, value)



# Task 10
import time

class GeyserClassic:
    MAX_DATE_FILTER = 100

    def __init__(self):
        self.__slots = {1: None, 2: None, 3: None}
        self.__filters = {1: Mechanical, 2: Aragon, 3: Calcium}


    def add_filter(self, slot_num, filter):
        if slot_num in (1, 2, 3) and type(filter) == self.__filters[slot_num] and self.__slots[slot_num] is None:
            self.__slots[slot_num] = filter

    def remove_filter(self, slot_num):
        self.__slots[slot_num] = None

    def get_filters(self):
        return tuple(self.__slots[i] for i in (1, 2, 3))

    def water_on(self):
        return all(self.__slots[i] is not None for i in (1, 2, 3)) and all((0 <= time.time() - self.__slots[i].date <= self.MAX_DATE_FILTER) for i in (1, 2, 3))


class Filter:
    def __init__(self, date):
        self.__date = None
        self.date = date

    @classmethod
    def validation(cls, value):
        return isinstance(value, float) and value > 0

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value):
        if self.__date is None and self.validation(value):
            self.__date = value


class Mechanical(Filter):
    pass

class Aragon(Filter):
    pass

class Calcium(Filter):
    pass




# class Mechanical:
#     def __init__(self, date):
#         self.__date = None
#         self.date = date
#
#     @classmethod
#     def validation(cls, value):
#         return isinstance(value, float) and value > 0
#
#     @property
#     def date(self):
#         return self.__date
#
#     @date.setter
#     def date(self, value):
#         if self.__date is None and self.validation(value):
#             self.__date = value
#
#
# class Aragon:
#     def __init__(self, date):
#         self.__date = None
#         self.date = date
#
#     @classmethod
#     def validation(cls, value):
#         return isinstance(value, float) and value > 0
#
#     @property
#     def date(self):
#         return self.__date
#
#     @date.setter
#     def date(self, value):
#         if self.__date is None and self.validation(value):
#             self.__date = value
#
#
# class Calcium:
#     def __init__(self, date):
#         self.__date = None
#         self.date = date
#
#     @classmethod
#     def validation(cls, value):
#         return isinstance(value, float) and value > 0
#
#     @property
#     def date(self):
#         return self.__date
#
#     @date.setter
#     def date(self, value):
#         if self.__date is None and self.validation(value):
#             self.__date = value


