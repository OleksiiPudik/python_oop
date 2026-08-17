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

# class Thing:
#     id = 0

#     def __init__(self, name, price, weight=None, dims=None, memory=None, frm=None):
#         self.name = name
#         self.price = price
#         self.weight = weight
#         self.dims = dims
#         self.memory = memory
#         self.frm = frm
#         Thing.id += 1
#         self.id = Thing.id

#     def get_data(self):
#         return (self.id, self.name, self.price, self.weight, self.dims, self.memory, self.frm)


# class Table(Thing):
#     def __init__(self, name, price, weight, dims):
#         super().__init__(name, price, weight, dims)


# class ElBook(Thing):
#     def __init__(self, name, price, memory, frm):
#         super().__init__(name, price, memory=memory, frm=frm)
        

# table = Table("round", 1024, 812.55, (700, 750, 700))
# book = ElBook("Python OOP", 2000, 2048, "pdf")
# # print(*table.get_data())
# # print(*book.get_data())
# table2 = Table("square", 111, 222, 333)
# book2 = ElBook("some book", 444, 555, "jpg")
# print(table.id, book.id, table2.id, book2.id)


# ---------------------------------------------
# tasc 6

class GenericView:
    def __init__(self, methods=('GET',)):
        self.methods = methods

    def get(self, request):
        return ""

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass


class DetailView(GenericView):
    def __init__(self, methods=('GET',)):
        super().__init__(methods)

    def render_request(self, request, method):
        if method not in self.methods:
            raise TypeError("данный запрос не может быть выполнен")

        method = method.lower()

        return getattr(self, method)(request)

    def get(self, request):
        if type(request) is not dict:
            raise TypeError("request не является словарем")
        elif "url" not in request:
            raise TypeError("request не содержит обязательного ключа url")
        
        return f"url: {request['url']}"
        


dv = DetailView()
html = dv.render_request({"url": "https://site.ua/home"}, "GET")
print(html)