def is_prime(num):
    if num < 2:
        return False
    for v in range(2, num):
        if num % v == 0:
            return False
    return True


def primes():
    counter = 0
    while True:
        if is_prime(counter):
            yield counter
        counter += 1


def func(num):
    for prim in primes():
        if num % prim == 0:
            num = num / prim
            if num <= 2:
                return prim
