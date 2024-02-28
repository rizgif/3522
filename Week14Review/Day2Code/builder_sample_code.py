"""
Pattern example where a builder class builds an Omelette
"""

from enum import Enum


class BaseEnum(Enum):
    """
    The different base options for an Omelette
    """
    REGULAR = 0,
    WHOLE_EGG = 1,
    EGG_WHITES = 2


class ToppingEnum(Enum):
    """
    The different topping options for an Omelette
    """
    RED_ONION = 0,
    PEPPERS = 1,
    SPINACH = 2,
    MUSHROOM = 3,
    PEPPERONI = 4,
    CHICKEN = 5,
    BACON = 6,
    BEYOND_MEAT = 7,
    PINEAPPLE = 8


class CheeseEnum(Enum):
    """
    The different Cheese options for an Omelette
    """
    PARMESAN = 0,
    MOZZARELLA = 1,
    VEGAN_CHEESE = 2


class SauceEnum(Enum):
    """
    The different sauce options for an Omelette.
    """
    TOMATO = 0,
    ALFREDO = 1,
    BBQ = 2



class Omelette():
    """
    As a contrived example let's look at an Omelette. as a complex object
    the omelette can have multiple toppings, cheeses, a base
    """

    def __init__(self) -> None:
        self.base = None
        self.sauce = None
        self.toppings = []
        self.cheeses = []

    def __str__(self):
        """
        Format and create a string representation of a Omelette.
        :return: a string
        """
        toppings_str = [str(topping) for topping in self.toppings]
        cheeses_str = [str(cheese) for cheese in self.cheeses]

        toppings = ", ".join(toppings_str)
        cheeses = ", ".join(cheeses_str)
        return f"Omelette:\n" \
            f"------\n" \
            f"Base: {self.base}\n" \
            f"Sauce: {self.sauce}\n" \
            f"Toppings: {toppings}\n" \
            f"Cheeses: {cheeses}\n"


class OmeletteBuilder:
    """
    The Omelette builder is a special class where we can place all the
    creation code for creating a omelette object. Here we can provide a
    different method for each component that makes up a Omelette
    """

    def __init__(self):
        self._omelette = Omelette()

    def reset(self):
        """
        Reset the omelette being built to a new blank omelette.
        :return:
        """
        self._omelette = Omelette()

    @property
    def omelette(self):
        """
        A property that "builds" the omelette when it is accessed. This
        could also be a seperate build() method.
        :return: a Omelette
        """
        completed_omelette = self._omelette
        self.reset()
        return completed_omelette

    def add_topping(self, topping: ToppingEnum):
        """
        Add a topping component to the Omelette that is being built.
        :param topping: a ToppingEnum
        """
        self._omelette.toppings.append(topping)
        return self

    def add_cheese(self, cheese: CheeseEnum, half_num: int =0):
        """
        Add a cheese component to the Omelette that is being built.
        :param cheese: a CheeseEnum
        """
        self._omelette.cheeses.append(cheese)
        return self

    def add_sauce(self, sauce: SauceEnum):
        """
        Add a sauce component to the Omelette that is being built.
        :param sauce: a SauceEnum
        """
        self._omelette.sauce = sauce
        return self

    def add_base(self, base: BaseEnum):
        """
        Add a base component to the Omelette that is being built.
        :param base: a BaseEnum
        """
        self._omelette.base = base

class Menu:
    """
    The Menu class acts as a Director. It is only responsible for
    executing the building steps in a particular sequence. In this case,
    these sequences refer to the different common types of omelette being
    built.
    """

    def __init__(self) -> None:
        self.builder = OmeletteBuilder()

    """
    The Director can construct several product variations using the same
    building steps.
    """

    def prepare_cheese_omelette(self) -> None:
        """
        Executes the sequence of steps to create a cheese omelette
        """
        self.builder.add_sauce(SauceEnum.TOMATO)
        self.builder.add_cheese(CheeseEnum.MOZZARELLA)
        self.builder.add_cheese(CheeseEnum.MOZZARELLA)
        self.builder.add_cheese(CheeseEnum.PARMESAN)
        self.builder.add_cheese(CheeseEnum.PARMESAN)

    def prepare_pepperoni_omelette(self) -> None:
        """
        Executes the sequence of steps to create a pepperoni omelette
        """
        self.builder.add_sauce(SauceEnum.TOMATO)
        self.builder.add_cheese(CheeseEnum.MOZZARELLA)
        self.builder.add_topping(ToppingEnum.PEPPERONI)

    def prepare_vegetarian_omelette(self) -> None:
        """
        Executes the sequence of steps to create a vegan omelette
        """
        self.builder.add_sauce(SauceEnum.TOMATO)
        self.builder.add_cheese(CheeseEnum.VEGAN_CHEESE)
        self.builder.add_topping(ToppingEnum.BEYOND_MEAT)
        self.builder.add_topping(ToppingEnum.SPINACH)
        self.builder.add_topping(ToppingEnum.RED_ONION)
        self.builder.add_topping(ToppingEnum.PEPPERS)


def main():
    """
    The client code creates a builder object, passes it to the director and then
    initiates the construction process. The end result is retrieved from the
    builder object.
    """

    # We can access the builder directly
    # -------------------------
    print("Using Builder to manually build omelette step by step")
    builder = OmeletteBuilder()
    builder.add_base(BaseEnum.EGG_WHITES)
    builder.add_sauce(SauceEnum.ALFREDO)
    builder.add_sauce(SauceEnum.TOMATO)
    builder.add_cheese(CheeseEnum.MOZZARELLA)
    builder.add_cheese(CheeseEnum.VEGAN_CHEESE)
    builder.add_topping(ToppingEnum.SPINACH)
    builder.add_topping(ToppingEnum.BEYOND_MEAT)
    #omelette is complete!
    omelette = builder.omelette
    print(omelette)

    # We can access the Director class
    # ----------------
    print("Using Menu (director) to create preset pepperoni omelette")
    menu = Menu()
    menu.prepare_pepperoni_omelette()
    omelette = menu.builder.omelette
    print(omelette)


if __name__ == "__main__":
    main()

