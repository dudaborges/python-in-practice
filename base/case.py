numbers1 = [1, 2, 3]
numbers2 = [1, 4, 5]



def findNumber(number: int):
    """
    Esta função verifica se um número está presente em duas listas.

    Examples:
    >>> findNumber(1)
    Existe nas duas listas
    >>> findNumber(3)
    Existe apenas na primeira lista
    >>> findNumber(5)
    Existe apenas na segunda lista
    """
    match number in numbers1, number in numbers2:
        case True, True:
            print("Existe nas duas listas")

        case True, False:
            print("Existe apenas na primeira lista")

        case False, True:
            print("Existe apenas na segunda lista")

#comando para rodar os testes: pytest --doctest-modules case.py