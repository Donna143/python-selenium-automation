# O(1)

def swap_two_variables(a, b):
    print(f'a = {a}, b = {b}')

    # Solution 1
    # swap = a
    # a = b
    # b = swap

    # Solution 2
    # a, b = b, a

    # Solution 3
    a = a + b
    b = a - b
    a = a - b
    print(f'a = {a}, b = {b}')


swap_two_variables(4,17)

