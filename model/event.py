from math import ceil

from model.ingredients import BurgerBun
from model.ingredients import Cheese
from model.ingredients import Fries
from model.ingredients import Meat


class HamburgerDay:
    def __init__(self, guests: int, portion_size: float = 2):
        self.guests = guests
        self.portion_size = portion_size

        self.__hamburgers = ceil(self.guests * self.portion_size)
        self.__meat = Meat(self.__hamburgers)
        self.__cheese = Cheese(self.__hamburgers)
        self.__fries = Fries(self.__hamburgers)
        self.__burger_bun = BurgerBun(self.__hamburgers)

    @property
    def count_hamburger(self):
        return self.__hamburgers

    @property
    def count_meat(self):
        return self.__meat.portion_size

    @property
    def count_lean_meat(self):
        return self.__meat.lean

    @property
    def count_fat_meat(self):
        return self.__meat.fat

    @property
    def count_cheese(self):
        return self.__cheese.portion_size

    @property
    def count_fries(self):
        return self.__fries.portion_size

    @property
    def count_burger_bun(self):
        return self.__burger_bun.portion_size
