class Parent:
    lst = [1, 2, 2]


class Inheritor1(Parent):
    pass


class Inheritor2(Parent):
    pass


a = Inheritor1()
b = Inheritor2()
a.lst.append(99)

print(Inheritor1.__mro__)