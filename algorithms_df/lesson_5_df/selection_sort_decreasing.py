

def selection_sort_decr(arr):
    for i in range(len(arr)):
        max_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[max_index]:
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]

    return arr


test_list = [4, 1, 2, 7, 4, 11, 3]
print(test_list)
print(sorted(test_list, reverse=True))
print(selection_sort_decr(test_list))