def even_fibs(below):
    curr, next = 0, 1
    while curr < below:
        if curr % 2 == 0:
            yield curr
        curr, next = next, curr + next


def func(below):
    return sum(even_fibs(below))
