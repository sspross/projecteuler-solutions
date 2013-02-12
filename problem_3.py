def is_prim(num):
    if num < 2:
        return False
    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            return False 
    return True

def prims_inverse(start):
    num = start
    while True:
        if is_prim(num):
            yield num
        num -= 1

def func(num):
    if num < 2:
        return None
    for prim in prims_inverse(int(num ** 0.5) + 1):
        if num % prim == 0:
            return prim
