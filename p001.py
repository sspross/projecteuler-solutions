def func(below):
    return sum([v for v in range(below) if v % 3 == 0 or v % 5 == 0])
