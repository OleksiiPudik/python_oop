# class Parent:
#     lst = [1, 2, 2]


# class Inheritor1(Parent):
#     pass


# class Inheritor2(Parent):
#     pass


# a = Inheritor1()
# b = Inheritor2()
# a.lst.append(99)

# print(Inheritor1.__mro__)


# class Table:
#     def __init__(self, model, color):
#         self.model = model
#         self. color = color
        


# class RoundTable(Table):
#     def __init__(self, model, color, radius, height):
#         super().__init__(model, color)
#         self.radius = radius
#         self.height = height
        


# class SquareTable(Table):
#     def __init__(self, model, color, side, height):
#             super().__init__(model, color)
#             self.side = side
#             self.height = height
#             print(hash(self))


# rt = RoundTable("qqq", "red", 5, 10)
# rs = SquareTable("aaa", "green", 5, 10)


# -----------------------------------------------


# tasc 4

# class Animal:
#     def __init__(self, name, old):
#         self.name = name
#         self.old = old


# class Cat(Animal):
#     def __init__(self, name, old, color, weight):
#         super().__init__(name, old)
#         self.color = color
#         self.weight = weight

#     def get_info(self):
#         return f"{self.name}: {self.old}, {self.color}, {self.weight}"


# class Dog(Animal):
#     def __init__(self, name, old, breed, size):
#         super().__init__(name, old)
#         self.breed = breed
#         self.size = size

#     def get_info(self):
#         return f"{self.name}: {self.old}, {self.breed}, {self.size}"


# c = Cat("mur", 5, "brown", 7)
# d  =Dog("wow", 7, "borza", (400, 600))
# print(d.get_info())


# ------------------------------------

# tasc 5

class Thing:
    ID = 1

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.id = self.ID
        


th1 = Thing("aaa", 1)
th2 = Thing("bbb", 2)
print(th1.id)
print(th2.id)