def printN(n):
    if n > 0:
        printN(n - 1)
        print(n, end=" ")


def printNreverse(n):
    if n > 0:
        print(n, end=" ")
        printNreverse(n - 1)


def printodd(n):
    if n > 0:
        printodd(n - 1)
        print(2 * n - 1, end=" ")


def printeven(n):
    if n > 0:
        printeven(n - 1)
        print(2 * n, end=" ")


def printoddreverse(n):
    if n > 0:
        print(2 * n - 1, end=" ")
        printodd(n - 1)


def printevenreverse(n):
    if n > 0:
        print(2 * n, end=" ")
        printeven(n - 1)


printoddreverse(10)
print("")
printevenreverse(10)
