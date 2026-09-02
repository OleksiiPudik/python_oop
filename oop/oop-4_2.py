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
        return (self.name, self.price, self.weight) == (value.name, value.price, value.weight)


thing1 = Thing("some name", 12.34, 56.78)
thing2 = Thing("some name", 12.34, 56.78)
d = {}
d[thing1] = 1
d[thing2] = 2
# print(d)
# print(len(d))
# print(hash(thing1))
# print(hash(thing2))
# print(thing1 == thing2)
# print(thing1)
# print(thing2)
print(list(d.keys()))

