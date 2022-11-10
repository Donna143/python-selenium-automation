# Your input is a list of integers, and you have to reorder its entries so that the even
# entries appear first. You are required to solve it without allocating additional storage
# (operate with the input list).
# Example: [7, 3, 5, 6, 4, 10, 3, 2]  Return [6, 4, 10, 2, 7, 3, 5, 3]


def even_first(arr):
    i = 0
    even_num = 0
    for j in range(len(arr)):
        if arr[j] % 2 == 0:
            even_num = arr[j]
            arr.pop(j)
            arr.insert(i, even_num)
            i += 1
    return arr


test_list = [7, 3, 5, 6, 4, 10, 3, 2]
test_list2 = [6, 1, 7, 8, 6, 5, 11, 10]
result_list = even_first(test_list)
result_list2 = even_first(test_list2)
print(result_list)
print(result_list2)