# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False
        if kwargs.get('ignore_case') == True:
            self.ignore_case = True
        else:
            self.ignore_case = False
        self.data = iter(items)
        self.res = set()
        pass

    def __next__(self):
        # Нужно реализовать __next__
        while True:
                item = self.data.__next__()
                if self.ignore_case:
                    new_item = str(item).lower()
                else:
                    new_item = item
                if new_item not in self.res:
                    self.res.add(new_item)
                    return item
        pass

    def __iter__(self):
        return self
