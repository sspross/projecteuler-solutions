def nums(below):
    a, b = 3, 5
    while a < below or b < below:
        if a < b:
            yield a
            a += 3
        else:
            yield b
            b += 5


def func(below):
    return sum(set([num for num in nums(below)]))
