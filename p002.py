def fibs(maxval):
    curr, next = 0, 1
    while curr < maxval:
        yield curr
        curr, next = next, curr + next


def func(maxval):
    return sum([v for v in fibs(maxval) if v % 2 == 0])
