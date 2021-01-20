from random import randint


def feeling_of_hunger_in_a_mammal(a, b):
    """
    considers a mammal to have a random desire

    :param a:
    :param b:
    :return:
    """
    hunger = randint(a, b)
    return hunger


def hare_hunger():
    """
    a random feeling of hunger for a hare

    :return:
    """
    hunger_hare = feeling_of_hunger_in_a_mammal(-10, 10)
    return hunger_hare


hunger_for_hare = hare_hunger()


def wolf_hunger():
    """
    a random feeling of hunger for a wolf

    :return:
    """
    hunger_wolf = feeling_of_hunger_in_a_mammal(-30, 30)
    return hunger_wolf


hunger_for_wolf = wolf_hunger()


def mammal_goes_to_eat(h1, h2):
    """
    in case of hunger in an animal, it goes to eat

    :return:
    """
    if h1 > 0 and h2 > 0:
        return 'Заяц отправился за едой, не подозревая, что где то охотится волк.'
    elif h1 > 0:
        return 'Волк, шумно принюхиваясь, крадется по лесу. '
    elif h2 > 0:
        return 'Слышно как где-то заяц хрустит корой.'
    else:
        return 'Тихо в лесу'
