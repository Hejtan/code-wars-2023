#   Szymon Anikiej
#   Plik służy do testowania funkcji material z pliku code_wars_function.py, zawierającego funkcję konkursową material(spaceship: list[int]) -> int
#   Lista tests zawiera dwa testy bazujące na przykładach z zadania, oraz 4 testy ode mnie
#   Funkcja gen_random_test() generuje losowy test
#   W celu przeprowadzenia testu na wszystkich przygotowanych testach i określonej liczbie testów losowych należy wywołać funkcję test_all(silent=False, nr_of_random_tests=10)
#   Zalecam ustawić wartość argumentu silent na True w przypadku dużej liczby testów losowych.
#       Wtedy funkcja wypisze tylko liczbę testów, dla których material() i brute_material() zwróciły inne wyniki
#   Przy silent o wartości False, dla każdego testu zostanie wypisany spaceship, wynik obu funkcji oraz informacja, czy test został zaliczony

from code_wars_function import material, brute_material
import random

tests = [
    [6, 4, 2, 0, 3, 2, 0, 3, 1, 4, 5, 3, 2, 7, 5, 3, 0, 1, 2, 1, 3, 4, 6, 8, 1, 3],
    [6,2,1,1,8,0,5,5,0,1,8,9,6,9,4,8,0,0],
    [],
    [3, 3, 3],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5, 4, 3, 2]
]

def gen_random_test() -> list[int]:
    return [random.randint(0, 100) for _ in range(random.randint(0, 1000))]

def test_material(test, silent=False):
    res1 = material(test)
    res2 = brute_material(test)
    if not silent:
        print(f"Test: {test}")
        print(f"Smart result: {res1}")
        print(f"Brute result: {res2}")
        print(f"Test passed: {res1 == res2}")
    return res1 == res2

def test_all(silent=False, nr_of_random_tests=10):
    mistakes = 0
    for i in range(nr_of_random_tests):
        tests.append(gen_random_test())
    for test in tests:
        if not silent:
            print("=====================================")
        x = test_material(test, silent)
        if not x:
            mistakes += 1
    print("=====================================\n=====================================\nTotal mistakes: ", mistakes)

if __name__ == "__main__":
    #     Przykłady użycia:
    # print("Testing material function:")
    # test_all(False, 4)
    # print("\n\nTesting material function (silent):")
    # test_all(True, 1000)

    sil = input("Silent (Write True or False): ")
    if sil == "True":
        sil = True
    else:
        sil = False
    n = int(input("Number of random tests: "))
    print("\nTesting material function:")
    test_all(sil, n)
