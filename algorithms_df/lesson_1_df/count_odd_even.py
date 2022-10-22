# O(n)
# Count odd and even numbers. Count odd and even digits of the whole number.
# Example: number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5).


def count_odd_even(n):
    odd_count = 0
    even_count = 0
    for i in str(n):
        if int(i) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return odd_count, even_count


def count_odd_even2(n):
    odds = 0
    evens = 0
    while n > 0:
        current_digit = n % 10
        if current_digit % 2:
            odds = odds + 1
        else:
            evens = evens + 1
        n = n // 10
    return [odds, evens]


print(count_odd_even2(34560))
print(count_odd_even(34560))


