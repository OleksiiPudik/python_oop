# task 3
# import math

# class Track:
#     def __init__(self, start_x, start_y):
#         if not isinstance(start_x, (int, float)) or not isinstance(start_y, (int, float)):
#             raise TypeError("Координаты должны быть заданы целым или вещественным числом")
        
#         self.start_x = start_x
#         self.start_y = start_y
#         self.tracks = []
    
#     def add_track(self, tr):
#         self.tracks.append(tr)

#     def get_tracks(self):
#         return tuple(self.tracks)
    
#     def __len__(self):
#         len_track = 0
#         for i in range(len(self.tracks)):
#             if i == 0:
#                 begin_x, begin_y = self.start_x, self.start_y
#             else:
#                 begin_x, begin_y = self.tracks[i-1].to_x, self.tracks[i-1].to_y
            
#             end_x, end_y = self.tracks[i].to_x, self.tracks[i].to_y

#             len_track += math.hypot(end_x - begin_x, end_y - begin_y)
        
#         return int(len_track)
    
#     def __eq__(self, other):
#         return len(self) == len(other)
    
#     def __gt__(self, other):
#         return len(self) > len(other)
    
#     def __lt__(self, other):
#         return len(self) < len(other)


# class TrackLine:
#     def __init__(self, to_x, to_y, max_speed):
#         if not isinstance(to_x, (int, float)) or not isinstance(to_y, (int, float)) or not isinstance(max_speed, int):
#             raise TypeError("Координаты должны быть заданы целым или вещественным числом, а скорость целым")
        
#         self.to_x = to_x
#         self.to_y = to_y
#         self.max_speed = max_speed


# track1 = Track(0, 0)
# line_1_1 = TrackLine(2, 4, 100)
# line_1_2 = TrackLine(5, -4, 100)
# track1.add_track(line_1_1)
# track1.add_track(line_1_2)
# track2 = Track(0, 1)
# line_2_1 = TrackLine(3, 2, 90)
# line_2_2 = TrackLine(10, 8, 90)
# track2.add_track(line_2_1)
# track2.add_track(line_2_2)

# res_eq = track1 == track2
# print(res_eq)

# --------------------------------------------------------

# tasc 4
# class Dimensions:
#     MIN_DIMENSION = 10
#     MAX_DIMENSION = 10000

#     def __init__(self, a, b, c):
#         self.__a = a
#         self.__b = b
#         self.__c = c
    
#     @property
#     def a(self):
#         return self.__a
    
#     @a.setter
#     def a(self, a):
#         if self.MIN_DIMENSION <= a <= self.MAX_DIMENSION:
#             self.__a = a
    
#     @property
#     def b(self):
#         return self.__b
    
#     @b.setter
#     def b(self, b):
#         if self.MIN_DIMENSION <= b <= self.MAX_DIMENSION:
#             self.__b = b
    
#     @property
#     def c(self):
#         return self.__c
    
#     @c.setter
#     def c(self, c):
#         if self.MIN_DIMENSION <= c <= self.MAX_DIMENSION:
#             self.__c = c
    
#     def volume(self):
#         vol = self.__a * self.__b * self.__c
#         return vol
    
#     def __lt__(self, other):
#         return self.volume() < other.volume()
    
#     def __le__(self, other):
#         return self.volume() <= other.volume()
    
#     def __gt__(self, other):
#         return self.volume() > other.volume()
    
#     def __ge__(self, other):
#         return self.volume() >= other.volume()


# class ShopItem:
#     def __init__(self, name, price, dim):
#         self.name = name
#         self.price = price
#         self.dim = dim


# lst_shop = [
#     ShopItem("кеды", 1024, Dimensions(40, 30, 120)),
#     ShopItem("зонт", 500.24, Dimensions(10, 20, 50)),
#     ShopItem("холодильник", 40000, Dimensions(2000, 600, 500)),
#     ShopItem("табуретка", 2000.99, Dimensions(500, 200, 200))
#     ]

# lst_shop_sorted = sorted(lst_shop, key=lambda d: d.dim.volume())

# print(lst_shop_sorted)

# --------------------------------------------------------

# tasc 5
# stich = ["Я к вам пишу - чего же боле?",
#          "Что я могу еще сказать?",
#          "Теперь, я знаю, в вашей воле",
#          "Меня презреньем наказать.",
#          "Но вы, к моей несчастной доле",
#          "Хоть каплю жалости храня,",
#          "Вы не оставите меня."]

# class StringText:
#     def __init__(self, lst_words):
#         self.lst_words = lst_words

#     def __len__(self):
#         return len(self.lst_words)
    
#     def __gt__(self, other):
#         return len(self) > len(other)
    
#     def __ge__(self, other):
#         return len(self) >= len(other)
    
#     def __lt__(self, other):
#         return len(self) < len(other)
    
#     def __le__(self, other):
#         return len(self) <= len(other)

# lst_text = []
# for line in stich:
#     lst_words = [x.strip("-?!,.;") for x in line.split() if x.strip("-?!,.;")]
#     lst_text.append(StringText(lst_words))

# lst_text_sorted = sorted(lst_text, key=len, reverse=True)

# lst_text_sorted = [" ".join(st.lst_words) for st in lst_text_sorted]

# print(lst_text_sorted)

# s1 = "Я к вам пишу - чего же боле?"
# s2 = "Теперь, я знаю, в вашей воле"

# s1 = s1.split()
# s1 = [x.strip("-?!,.;") for x in s1 if x.strip("-?!,.;") != ""]
# print(s1)

# --------------------------------------------------------

# tasc 6
# class Morph:
#     def __init__(self, *words):
#         self.words = list(words)
    
#     def add_word(self, word):
#         if word.lower() not in self.words:
#             self.words.append(word.lower())
    
#     def get_words(self):
#         return tuple(self.words)
    
#     def __eq__(self, other):
#         if not isinstance(other, str):
#             return NotImplemented
#         return other.lower() in self.words
    
    


# svyaz = Morph("связь", "связи", "связью", "связей", "связям", "связями", "связях")
# formula = Morph("формула", "формулы", "формуле", "формулу", "формулой", "формулам", "формулами", "формулах")
# vektor = Morph("вектор", "вектора", "вектору", "вектором", "векторе", "векторы", "векторов", "векторам", "векторами", "векторах")
# effekt = Morph("эффект", "эффекта", "эффекту", "эффектом", "эффекте", "эффекты", "эффектов", "эффектам", "эффектами", "эффектах")
# den = Morph("день", "дня", "дню", "днем", "дне", "дни", "дням", "днями", "днях")

# dict_words = [svyaz, formula, vektor, effekt, den]

# text = input()

# text_lst = [i.lower().strip(".,!?-") for i in text.split()]

# res = 0

# for word_in in text_lst:
#     for words_d in dict_words:
#         if words_d == word_in:
#             res += 1

# print(res)


# --------------------------------------------------------

# tasc 7
# class FileAcceptor:
#     def __init__(self, *extensions):
#         self.extensions = [x.lower() for x in extensions]
    
#     def __call__(self, filename, *args, **kwds):
#         ext = filename.rpartition(".")[-1].lower()
#         return ext in self.extensions
    
#     def __add__(self, other):
#         ext = list(set(self.extensions) | set(other.extensions))
#         return FileAcceptor(*ext)


# acc_imj = FileAcceptor("jpg", "png")
# acc_docs = FileAcceptor("txt", "doc")
# filenames = ["qqq.jpg", "www.xlsx", "eee.png", "rrr_1.rtf", "ttt.txt"]
# filenames = list(filter(acc_imj + acc_docs, filenames))
# print(filenames)

# a = ("jpg", "pdf", "wxo")
# b = ("jpg", "bmp")
# print(list(set(a) | set(b)))


# --------------------------------------------------------

# tasc 8
# class MoneyR:
#     __currency = "rub"

#     def __init__(self, volume=0):
#         self.__volume = volume
#         self.__cb = None
    
#     @property
#     def volume(self):
#         return self.__volume
    
#     @volume.setter
#     def volume(self, volume):
#         self.__volume = volume
    
#     @property
#     def cb(self):
#         return self.__cb
    
#     @cb.setter
#     def cb(self, cb):
#         self.__cb = cb
    
#     @property
#     def currency(self):
#         return self.__currency
    
    
#     def __eq__(self, other):
#         if self.__cb is None or other.cb is None:
#             raise ValueError("Неизвестен курс валют.")
        
#         wal_self = self.__volume * self.__cb.rates[self.__currency]
#         wal_other = other.volume * other.cb.rates[other.currency]
#         return wal_self == wal_other
    
#     def __lt__(self, other):
#         if self.__cb is None or other.cb is None:
#             raise ValueError("Неизвестен курс валют.")
        
#         wal_self = self.__volume * self.__cb.rates[self.__currency]
#         wal_other = other.volume * other.cb.rates[other.currency]
#         return wal_self < wal_other
    
#     def __le__(self, other):
#         if self.__cb is None or other.cb is None:
#             raise ValueError("Неизвестен курс валют.")
        
#         wal_self = self.__volume * self.__cb.rates[self.__currency]
#         wal_other = other.volume * other.cb.rates[other.currency]
#         return wal_self <= wal_other
    
#     def __gt__(self, other):
#         if self.__cb is None or other.cb is None:
#             raise ValueError("Неизвестен курс валют.")
        
#         wal_self = self.__volume * self.__cb.rates[self.__currency]
#         wal_other = other.volume * other.cb.rates[other.currency]
#         return wal_self > wal_other
    
#     def __ge__(self, other):
#         if self.__cb is None or other.cb is None:
#             raise ValueError("Неизвестен курс валют.")
        
#         wal_self = self.__volume * self.__cb.rates[self.__currency]
#         wal_other = other.volume * other.cb.rates[other.currency]
#         return wal_self >= wal_other


# class MoneyD:
#     __currency = "dollar"

#     def __init__(self, volume=0):
#         self.__volume = volume
#         self.__cb = None
    
#     @property
#     def volume(self):
#         return self.__volume
    
#     @volume.setter
#     def volume(self, volume):
#         self.__volume = volume
    
#     @property
#     def cb(self):
#         return self.__cb
    
#     @cb.setter
#     def cb(self, cb):
#         self.__cb = cb
    
#     @property
#     def currency(self):
#         return self.__currency
    
    
#     def __eq__(self, other):
#         if self.__cb is None or other.cb is None:
#             raise ValueError("Неизвестен курс валют.")
        
#         wal_self = self.__volume * self.__cb.rates[self.__currency]
#         wal_other = other.volume * other.cb.rates[other.currency]
#         return wal_self == wal_other
    
#     def __lt__(self, other):
#         if self.__cb is None or other.cb is None:
#             raise ValueError("Неизвестен курс валют.")
        
#         wal_self = self.__volume * self.__cb.rates[self.__currency]
#         wal_other = other.volume * other.cb.rates[other.currency]
#         return wal_self < wal_other
    
#     def __le__(self, other):
#         if self.__cb is None or other.cb is None:
#             raise ValueError("Неизвестен курс валют.")
        
#         wal_self = self.__volume * self.__cb.rates[self.__currency]
#         wal_other = other.volume * other.cb.rates[other.currency]
#         return wal_self <= wal_other
    
#     def __gt__(self, other):
#         if self.__cb is None or other.cb is None:
#             raise ValueError("Неизвестен курс валют.")
        
#         wal_self = self.__volume * self.__cb.rates[self.__currency]
#         wal_other = other.volume * other.cb.rates[other.currency]
#         return wal_self > wal_other
    
#     def __ge__(self, other):
#         if self.__cb is None or other.cb is None:
#             raise ValueError("Неизвестен курс валют.")
        
#         wal_self = self.__volume * self.__cb.rates[self.__currency]
#         wal_other = other.volume * other.cb.rates[other.currency]
#         return wal_self >= wal_other


# class MoneyE:
#     __currency = "euro"

#     def __init__(self, volume=0):
#         self.__volume = volume
#         self.__cb = None
    
#     @property
#     def volume(self):
#         return self.__volume
    
#     @volume.setter
#     def volume(self, volume):
#         self.__volume = volume
    
#     @property
#     def cb(self):
#         return self.__cb
    
#     @cb.setter
#     def cb(self, cb):
#         self.__cb = cb
    
#     @property
#     def currency(self):
#         return self.__currency
    
    
#     def __eq__(self, other):
#         if self.__cb is None or other.cb is None:
#             raise ValueError("Неизвестен курс валют.")
        
#         wal_self = self.__volume * self.__cb.rates[self.__currency]
#         wal_other = other.volume * other.cb.rates[other.currency]
#         return wal_self == wal_other
    
#     def __lt__(self, other):
#         if self.__cb is None or other.cb is None:
#             raise ValueError("Неизвестен курс валют.")
        
#         wal_self = self.__volume * self.__cb.rates[self.__currency]
#         wal_other = other.volume * other.cb.rates[other.currency]
#         return wal_self < wal_other
    
#     def __le__(self, other):
#         if self.__cb is None or other.cb is None:
#             raise ValueError("Неизвестен курс валют.")
        
#         wal_self = self.__volume * self.__cb.rates[self.__currency]
#         wal_other = other.volume * other.cb.rates[other.currency]
#         return wal_self <= wal_other
    
#     def __gt__(self, other):
#         if self.__cb is None or other.cb is None:
#             raise ValueError("Неизвестен курс валют.")
        
#         wal_self = self.__volume * self.__cb.rates[self.__currency]
#         wal_other = other.volume * other.cb.rates[other.currency]
#         return wal_self > wal_other
    
#     def __ge__(self, other):
#         if self.__cb is None or other.cb is None:
#             raise ValueError("Неизвестен курс валют.")
        
#         wal_self = self.__volume * self.__cb.rates[self.__currency]
#         wal_other = other.volume * other.cb.rates[other.currency]
#         return wal_self >= wal_other


# class CentralBank:
#     def __new__(cls):
#         return None
    
#     rates = {"rub": 72.5, "dollar": 1.0, "euro": 1.15}

#     wallets = []
    
#     @classmethod
#     def register(cls, money):
#         cls.wallets.append(money)
#         money.cb = cls


# --------------------------------------------------------

# tasc 9
# class Body:
#     def __init__(self, name, ro, volume):
#         if not isinstance(name, str) or not isinstance(ro, (int, float)) or not isinstance(volume, (int, float)):
#             raise TypeError("Переменные должны быть формата: 'name' - string, 'ro' и 'volume' - int or float")
#         self.name = name
#         self.ro = ro
#         self.volume = volume
    
#     @property
#     def weight(self):
#         return self.ro * self.volume
    
#     def _get_weight(self, value):
#         if not isinstance(value, (int, float, Body)):
#             raise TypeError("Сравниваемое значение должно быть int or float or Body")
    
#         return value if isinstance(value, (int, float)) else value.weight
        
    
#     def __eq__(self, other):
#         return self.weight == self._get_weight(other)
    
#     def __lt__(self, other):
#         return self.weight < self._get_weight(other)
    
#     def __gt__(self, other):
#         return self.weight > self._get_weight(other)


# body1 = Body("b1", 2, 3)
# body2 = Body("b2", 2, 3)
# print(body1 == 0)

# --------------------------------------------------------

# tasc 10
class Box:
    def __init__(self):
        self.things = []
    
    def add_thing(self, obj):
        self.things.append(obj)
    
    def get_things(self):
        return self.things
    
    def __eq__(self, other):
        if len(self.things) != len(other.things):
            return False
        
        lst_temp = list(other.things)
        for i in self.things:
            if i in lst_temp:
                lst_temp.remove(i)
            else:
                return False
        
        return True
                    


class Thing:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass
    
    def __eq__(self, other):
        return self.name.lower() == other.name.lower() and self.mass == other.mass
    

b1 = Box()
b2 = Box()

b1.add_thing(Thing("мел", 100))
b1.add_thing(Thing("тряпка", 200))
b1.add_thing(Thing("доска", 2000))

b2.add_thing(Thing("тряпка", 200))
b2.add_thing(Thing("доска", 2000))
b2.add_thing(Thing("мел", 100))
# b2.add_thing(Thing("мелe", 500))

print(b1 == b2)