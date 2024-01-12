def sumN(n):
    if n == 0:
        return 0
    return n + sumN(n - 1)


def SumNOdd(n):
    if n == 0:
        return 0
    return 2 * n - 1 + SumNOdd(n - 1)


def SumNEven(n):
    if n == 0:
        return 0
    return 2 * n + SumNEven(n - 1)


def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)


def squar(n):
    if n == 1:
        return 1
    return n * n + squar(n - 1)


print(squar(5))
