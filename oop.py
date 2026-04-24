# -------------------------------------------------------
# Магический метод __call__. Функторы и классы-декораторы
# -------------------------------------------------------

# task 2
# import string, random
#
# psw_chars = string.ascii_lowercase + string.digits + "!@#$%*"
# min_length = 5
# max_length = 20
#
# class RandomPassword:
#     def __init__(self, chars, min_len, max_len):
#         self.__chars = chars
#         self.__min_len = min_len
#         self.__max_len = max_len
#
#     def __call__(self, *args, **kwargs):
#         n = random.randint(self.__min_len, self.__max_len)
#         return "".join(random.choice(self.__chars) for i in range(n))
#
#
# rnd = RandomPassword(psw_chars, min_length, max_length)
# lst_pass = list(rnd() for i in range(3))
# -------------------------------------------------------


# task 3
# class ImageFileAcceptor:
#     def __init__(self, extensions):
#         self.__extensions = extensions
#
#     def __call__(self, filename):
#         return filename.split(".")[-1] in self.__extensions
# -------------------------------------------------------


# task 4
from string import ascii_lowercase, digits

# class LoginForm:
#     def __init__(self, name, validators=None):
#         self.name = name
#         self.validators = validators
#         self.login = ""
#         self.password = ""
#
#     def post(self, request):
#         self.login = request.get('login', "")
#         self.password = request.get('password', "")
#
#     def is_validate(self):
#         if not self.validators:
#             return True
#
#         for v in self.validators:
#             if not v(self.login) or not v(self.password):
#                 return False
#
#         return True
#
#
# class LengthValidator:
#     def __init__(self, min_length, max_length):
#         self.__min_length = min_length
#         self.__max_length = max_length
#
#     def __call__(self, string):
#         return self.__min_length <= len(string) <= self.__max_length
#
#
# class CharsValidator:
#     def __init__(self, chars):
#         self.__chars = chars
#
#     def __call__(self, chars):
#         return all(i in self.__chars for i in chars)
# -------------------------------------------------------


# task 5
# class DigitRetrieve:
#     def __call__(self, string, *args, **kwargs):
#         try:
#             return int(string)
#         except ValueError:
#             return None
# -------------------------------------------------------


# task 6
# class RenderList:
#     def __init__(self, type_list):
#         self.__type_list = type_list
#
#     def __call__(self, lst_in, *args, **kwargs):
#         lst = "\n".join("<li>" + i + "</li>" for i in lst_in)
#         tag = self.__type_list if self.__type_list in ("ol", "ul") else "ul"
#         return f"<{tag}>\n{lst}\n</{tag}>"
#
# render = RenderList("ul")
# lst1 = ["qqqq1", "qqqq2", "qqqq3"]
# html = render(lst1)
# print(html)
# -------------------------------------------------------


# task 7
# class HandlerGET:
#     def __init__(self, func):
#         self.__fn = func
#
#     def __call__(self, request, *args, **kwargs):
#         if request.get("method", "GET") == "GET":
#             return self.get(self.__fn, request)
#         return None
#
#     def get(self, func, request, *args, **kwargs):
#         return f"GET: {func(request)}"
#
#
#
# @HandlerGet
# def contact(request):
#     return "Сергей Балакирев"
# -------------------------------------------------------


# task 8
# class Handler:
#     def __init__(self, methods):
#         self.__methods = methods
#
#     def __call__(self, func):
#         def wrapper(request, *args, **kwargs):
#             method = request.get("method", "GET")
#
#             if method not in self.__methods:
#                 return None
#
#             method = method.lower()
#             handler = self.__getattribute__(method)
#             return handler(func, request)
#
#         return wrapper
#
#     def get(self, func, request, *args, **kwargs):
#         return f"GET: {func(request)}"
#
#     def post(self, func, request, *args, **kwargs):
#         return f"POST: {func(request)}"
#
#
# @Handler(("GET", "POST"))
# def contact(request):
#     return "Сергей Балакирев"
# -------------------------------------------------------


# task 9
# class InputDigits:
#     def __init__(self, func):
#         self.__func = func
#
#     def __call__(self, *args, **kwargs):
#         return list(int(x) for x in self.__func().split())
#
#
# @InputDigits
# def input_dg():
#     return input()
#
# res = input_dg()
# print(res)
# -------------------------------------------------------


# task 10
class RenderDigit:
    def __call__(self, str_in, *args, **kwargs):
        try:
            return int(str_in)
        except ValueError:
            return None

class InputValues:
    def __init__(self, render):
        self.__render = render

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            return list(self.__render(x) for x in func().split())

        return wrapper


@InputValues(RenderDigit())
def input_dg():
    return input()