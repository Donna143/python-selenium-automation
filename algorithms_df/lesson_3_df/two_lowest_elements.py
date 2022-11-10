# Two Lowest Elements
# When given a list of elements, find the two lowest elements.
# They can be equal to each other or different.
# Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3

# O()

def two_lowest(arr):
    arr.sort()
    return arr[:2]
    # return arr[0], arr[1]


test_arr = [198, 3, 4, 9, 10, 9, 2]
print(two_lowest(test_arr))
