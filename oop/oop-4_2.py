# class SmartPhone:
#     pass


# class IPhone(SmartPhone):
#     pass


# phone = IPhone()
# print(issubclass(phone, SmartPhone))


# -------------------------------

class ListInteger(list):
    def __init__(self, iterable):
        for i in iterable:
            self.append(i)

    def append(self, object):
        if isinstance(object, bool) or not isinstance(object, int):
            raise TypeError("можно передавать только целочисленные значения")
        
        return super().append(object)

    def __setitem__(self, key, value):
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("можно передавать только целочисленные значения")
        
        return super().__setitem__(key, value)


s = ListInteger((1, 2, 3))
s[1] = 20
print(s)