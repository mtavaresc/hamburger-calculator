from dataclasses import dataclass
from math import ceil
from typing import ClassVar


@dataclass(frozen=True)
class Ingredient:
    count: int
    weight_kg: ClassVar[float]

    @property
    def portion_size(self):
        return self.weight_kg * self.count


class Meat(Ingredient):
    weight_kg = 0.120

    @property
    def lean(self):
        return self.portion_size * 0.8

    @property
    def fat(self):
        return self.portion_size * 0.2


class Cheese(Ingredient):
    weight_kg = 0.030


class Fries(Ingredient):
    weight_kg = 0.080


class BurgerBun(Ingredient):
    portion_pack: ClassVar[int] = 6

    @property
    def portion_size(self):
        return ceil(self.count / self.portion_pack)
