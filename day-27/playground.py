"""args demo"""
def add(*args):
    """Sum the args passed in"""
    total = 0
    for num in args:
        total += num
    return total


print(add(1, 2, 3, 4, 5))
