# Given a list of random numbers.
# Find and return the max element and the index of this element
# Example: [1, 45, 33, 76, 9, 10], print [3, 76]


def find_max_index(arr):
    max_index = 0
    max_element = arr[max_index]

    for i in range(1, len(arr)):
        if arr[i] > max_element:
            max_index = i
            max_element = arr[i]

    return [max_index, max_element]


def find_max_index2(arr):
    return [arr.index(max(arr)), max(arr)]


test_list = [1, 45, 33, 76, 9, 10]
print(find_max_index(test_list))
test_list = [1, 45, 33, 76, 9, 10]
print(find_max_index2(test_list))