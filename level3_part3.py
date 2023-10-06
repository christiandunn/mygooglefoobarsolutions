from math import log, floor


def isPowerOf2(n):
    return floor(log(n,2)) == log(n,2)


def factors_after_2(n):
    while n % 2 == 0:
        n = n // 2
    return n


def level3part3(n):
    operations = 0
    n = int(n)
    while n > 1:
        if isPowerOf2(n):
            return operations + int(log(n,2))
        else:
            if n % 2 == 0:
                n = n / 2
            else:
                if factors_after_2(n+1) < factors_after_2(n-1):
                    n = n + 1
                else:
                    n = n - 1
            operations += 1
    return operations
