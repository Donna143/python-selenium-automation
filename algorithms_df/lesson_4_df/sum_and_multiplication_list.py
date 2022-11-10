# Given an array of integers. Calculate sum and multiplication of elements.
# Return the list: calcutlated sum and multiplication of elements.
# Example: [1, 7, 3]  Return: [11, 21]


def sum_and_mult(arr):
    sum_result = 0
    mult_result = 1
    for i in arr:
        sum_result += i
        mult_result *= i

    return [sum_result, mult_result]


test_list = [1, 7, 3]
result_list = sum_and_mult(test_list)
print(result_list)
