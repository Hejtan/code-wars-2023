#   Szymon Anikiej
#   Plik zawiera funkcje do konkursu CodeWars: material(speceship: list[int]) -> int
#   W pliku również znajduje się funkcja brute-force przeznaczona tylko do testowania: brute_material(spaceship: list[int]) -> int

import collections

def material(spaceship: list[int]) -> int:
    """ Funkcja konkursowa """
    result = 0
    left_max_list = collections.deque()
    right_max_list = collections.deque()
    left_max_temp = 0
    right_max_temp = 0

    for i in range(len(spaceship)):
        left_max_list.append(left_max_temp)
        if spaceship[i] > left_max_temp:
            left_max_temp = spaceship[i]
        right_max_list.appendleft(right_max_temp)
        if spaceship[-i-1] > right_max_temp:
            right_max_temp = spaceship[-i-1]
    
    for i in range(len(spaceship)):
        lr_min = min(left_max_list.popleft(), right_max_list.popleft())
        result += max(0, lr_min - spaceship[i])

    return result


def brute_material(spaceship: list[int]) -> int:
    """ Funkcja brute-force do testowania """
    result = 0
    maxh = 0
    for i in range(len(spaceship)):
        if spaceship[i] > maxh:
            maxh = spaceship[i]
    for j in range(maxh+1):
        tab = []
        for i in range(len(spaceship)):
            if spaceship[i] >= j:
                tab.append(i)
        for i in range(len(tab)-1):
            result += tab[i+1] - tab[i] - 1
    return result