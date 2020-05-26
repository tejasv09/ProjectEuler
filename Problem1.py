
def a():
    return sum(i for i in range(1, 1000) if (i % 3 or i % 5))

print(a())


