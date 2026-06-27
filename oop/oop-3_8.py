class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
    
    def __getitem__(self, key):
        if isinstance(key, bool) or not isinstance(key, int) or key < 0 or key >= len(self.__dict__):
            raise IndexError("неверный индекс поля")
        
        lst_temp = list(self.__dict__.values())

        return lst_temp[key]
    
    def __setitem__(self, key, value):
        if isinstance(key, bool) or not isinstance(key, int) or key < 0 or key >= len(self.__dict__):
            raise IndexError("неверный индекс поля")
        
        lst_temp = list(self.__dict__.keys())

        self.__dict__[lst_temp[key]] = value

a = Record(aaa=111, bbb=222, ccc=333)
print(a.bbb)