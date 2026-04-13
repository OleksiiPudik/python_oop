# Task 5
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



# Task 6
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


# Task 7
class Picture:
    def __init__(self, name, author, descr):
        self.name = name
        self.author = author
        self.descr = descr

    def get_info_exhibit(self):
        return f"Описание экспоната {self.name}: {self.descr}"


class Mummies:
    def __init__(self, name, location, descr):
        self.name = name
        self.locatio = location
        self.descr = descr

    def get_info_exhibit(self):
        return f"Описание экспоната {self.name}: {self.descr}"

class Papyri:
    def __init__(self, name, date, descr):
        self.name = name
        self.date = date
        self.descr = descr

    def get_info_exhibit(self):
        return f"Описание экспоната {self.name}: {self.descr}"


class Museum:
    def __init__(self, name):
        self.name = name
        self.exhibits = []

    def add_exhibit(self, obj):
        self.exhibits.append(obj)

    def remove_exhibit(self, obj):
        self.exhibits.remove(obj)

    def get_info_exhibit(self, indx):
        return self.exhibits[indx].get_info_exhibit()