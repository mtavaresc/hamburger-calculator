from model.event import HamburgerDay


def calculate(guests: int, portion_size: float = 2):
    """
    Calculate the portions to buy
    :param guests: Number of guests invited
    :param portion_size: Portion for each guest
    :return: portions to buy
    """
    event = HamburgerDay(guests, portion_size)

    return {
        "count_hamburgers": event.count_hamburger,
        "weight_meat": event.count_meat,
        "weight_lean_meat": event.count_lean_meat,
        "weight_fat_meat": event.count_fat_meat,
        "weight_cheese": event.count_cheese,
        "weight_french_fries": event.count_fries,
        "count_burger_bun": event.count_burger_bun
    }


if __name__ == '__main__':
    calculate(20, 2)
