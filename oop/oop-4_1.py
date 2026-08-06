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


class Table:
    def __init__(self, model, color):
        self.model = model
        self. color = color
        


class RoundTable(Table):
    def __init__(self, model, color, radius, height):
        super().__init__(model, color)
        self.radius = radius
        self.height = height
        


class SquareTable(Table):
    def __init__(self, model, color, side, height):
            super().__init__(model, color)
            self.side = side
            self.height = height
            print(hash(self))


rt = RoundTable("qqq", "red", 5, 10)
rs = SquareTable("aaa", "green", 5, 10)