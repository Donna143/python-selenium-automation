# O(n)
# Compute the sum of digits in all numbers from 1 to n.
# When a function gets a number n, find the sum of digits in all numbers from 1 to n.
# Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15

def sum_of_numbers(n):
    result = 0
    for i in range(1, n+1):
        result += i
    return result


def sum_to_n(n):
    result = (n*(n+1))/2
    return result


print(sum_of_numbers(5))
print(sum_to_n(5))

