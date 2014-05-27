def func(size):
    # http://mathworld.wolfram.com/LatticePath.html
    if not size:
        return 0
    return binomial_coefficient(size + size, size)


def binomial_coefficient(n, k):
    return factorial(n) / (factorial(n - k) * factorial(k))


def factorial(num):
    if num == 0:
        return 1
    result = 1
    for i in range(1, num + 1):
        result = result * i
    return result


# def binomialCoeff(n, k):
#     result = 1
#     for i in range(1, k + 1):
#         result = result * (n - i + 1) / i
#     return result


# (0,0) (0,1) (0,2)
# (1,0) (1,1) (1,2)
# (2,0) (2,1) (2,2)


# def func(size):
#     if not size:
#         return 0
#     return trace(0, 0, size)


# def trace(x, y, size):
#     if x == size and y == size:
#         return 1
#     else:
#         endpoints = 0
#         if x < size:
#             endpoints += trace(x + 1, y, size)
#         if y < size:
#             endpoints += trace(x, y + 1, size)
#         return endpoints
