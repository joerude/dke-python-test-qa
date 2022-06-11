# 1
import math

print(math.factorial(5))


# 2
# def factorial(n):
#     return [base if base == 1 else base * i for i in range(n, 0, -1)][0]
# print(factorial(5))


# 3

def factorial3(n):
    base = 1
    for i in range(n, 0, -1):
        base = base * i
    return base


print(factorial3(5))


def factorial4(n, total=1):
    while True:
        if n == 1:
            return total
        n, total = n - 1, total * n


print(factorial4(5))
