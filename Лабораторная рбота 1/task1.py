# TODO Написать 3 класса с документацией и аннотацией типов
from typing import Union

class Bottle:
    def __init__(self, Bottle_wine: int, Bottle_winecost: int):
        if not Bottle_wine > 0:
            raise ValueError
        self.Bottle_wine = Bottle_wine

        if Bottle_winecost < 0:
            raise ValueError
        if Bottle_winecost < Bottle_wine:
            raise ValueError
        self.Bottle_winecost = Bottle_winecost

    def is_Bottle(self) -> bool:
        """
        Функция которая проверяет является ли бутылка бутылкой
        :return: Является ли объект стаканом или нет
        """
        ...
    def add_wine_to_pool(self, wine: int) -> int:
        """
        Возврат вина в резерв.
        Если количество добавляемого вина превышает доступное место,
        то возвращается количество непоместившейся жидкости
        :param water: Объем добавляемого вина
        :return: Объем непоместившегося вина
        """
        ...
class Glass:
    def __init__(self, Glass_tea: int, Glass_teacost: int):
        if not Glass_tea > 0:
            raise ValueError
        self.Glass_tea = Glass_tea

        if Glass_teacost < 0:
            raise ValueError
        if Glass_teacost < Glass_tea:
            raise ValueError
        self.Glass_teacost = Glass_teacost

    def is_Glass(self) -> bool:
        """
        Функция которая проверяет является ли бокал бокалом
        :return: Является ли объект стаканом или нет
        """
        ...

    def add_tea_to_pool(self, tea: int) -> int:
        """
        Возврат чвя в резерв.
        Если количество добавляемого чая превышает доступное место,
        то возвращается количество непоместившейся жидкости
        :param water: Объем добавляемого чая
        :return: Объем непоместившийся чай
        """
        ...


class Jar:
    def __init__(self, Jar_compote: int, Jar_compotecost: int):
        if not Jar_compote > 0:
            raise ValueError
        self.Jar_compote = Jar_compote

        if Jar_compotecost < 0:
            raise ValueError
        if Jar_compotecost < Jar_compote:
            raise ValueError
        self.Jar_compotecost = Jar_compotecost

    def is_Jar(self) -> bool:
        """
        Функция которая проверяет является ли банка банкой
        :return: Является ли объект стаканом или нет
        """
        ...

    def add_compote_to_pool(self, compote: int) -> int:
        """
        Возврат компота в резерв.
        Если количество добавляемого компота превышает доступное место,
        то возвращается количество непоместившейся жидкости
        :param water: Объем добавляемого компота
        :return: Объем непоместившегося компота
        """
        ...

if __name__ == "__main__":
    Bottle1 = Bottle(750, 800)
    Glass1 = Glass(250, 300)
    Jar1 = Jar(3, 4)
    # TODO работоспособность экземпляров класса проверить с помощью doctest

    print(Bottle1.Bottle_wine, Bottle1.Bottle_winecost)
    print(Glass1.Glass_tea, Glass1.Glass_teacost)
    print(Jar1.Jar_compote, Jar1.Jar_compotecost)
    pass