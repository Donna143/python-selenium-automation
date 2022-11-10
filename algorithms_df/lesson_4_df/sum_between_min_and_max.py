# Find a sum of elements between min and max elements.
# Min and max elements are not included.
# All numbers are unique.


def sum_between_min_and_max(arr):
    min_item = max_item = arr[0]
    min_index = max_index = i = 0

    while i < len(arr):
        if arr[i] > max_item:
            max_item = arr[i]
            max_index = i
        if arr[i] < min_item:
            min_item = arr[i]
            min_index = i
        i += 1

    return sum(arr[min(min_index, max_index) + 1:max(min_index, max_index)])


test_list1 = [5, 2, 6, 4, 22, 10]
test_list2 = [8, 33, 2, 6, 1, 0, 22]
test_result1 = sum_between_min_and_max(test_list1)
test_result2 = sum_between_min_and_max(test_list2)
print(test_result1)
print(test_result2)
