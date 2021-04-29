def print_b(var):
    print(var)
    print('B')
    var = var + 100
    return var

def print_a():
    var = 1
    var = print_b(var)
    print(var)
    print('A')

# print_a()

def print_self(n):
    if n == 0:
        return

    print(n)
    print_self(n - 1)
    return

print_self(3)