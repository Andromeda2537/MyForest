from random import randint
from mammals import hare_hunger, wolf_hunger, mammal_goes_to_eat


def mountain_forest():
    return 'Горный лес.'


def wind_speed():
    """ counts a random increase in wind speed
 """
    increased_wind_speed = randint(-10, 10)
    return increased_wind_speed


def forest_reaction():
    """the forest reacts to the changed wind speed in a certain way
"""
    if sped_increased_by > 0:
        return 'Поднялся ветер, деревья шумят листвой.'
    else:
        return 'Ветер стих и лес вслед за ним.'


def bird_reaction():
    """bird response to changes in wind speed
"""
    if sped_increased_by > 0:
        return 'Птицы, испугавшись ветра улетают.'
    else:
        return 'Птицы вьют гнезда, охотяться и болтают с сородичами.'


if __name__ == '__main__':
    while True:
        sped_increased_by = wind_speed()
        hunger_for_hare = hare_hunger()
        hunger_for_wolf = wolf_hunger()
        print(forest_reaction(), bird_reaction(), mammal_goes_to_eat(hunger_for_wolf, hunger_for_hare))
