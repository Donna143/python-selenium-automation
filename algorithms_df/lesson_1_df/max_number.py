# O(1)
# Find max number from 3 values.
# Example: 124, 21, 32. Result = 124.

def max_number(a, b, c):
    maximum = a
    if b > maximum:
        maximum = b
        if c > maximum:
            maximum = c
    return maximum


result = max_number(124, 21, 32)
print(result)
