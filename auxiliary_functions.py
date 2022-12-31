import sys
import os
from constnts import *
from random import randint, choice


def get_result():
    with open(RESULTS) as file:
        max_result = max([int(x) for x in file])
    return max_result


def write_result(spider):
    with open(RESULTS, "a", encoding="utf8") as file:
        file.write(str(spider.points) + "\n")


def terminate():
    pygame.quit()
    sys.exit()


def load_image(name, colorkey=None):
    fullname = os.path.join(DIRECTORY, name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def choose_hint():
    with open(HINTS, "r", encoding="utf8") as file:
        hints = [s[:-1] for s in file]
    return choice(hints)
