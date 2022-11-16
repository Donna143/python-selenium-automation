

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


test_list = [4, 1, 2, 7, 4, 11, 3]
print(test_list)
print(sorted(test_list))
print(selection_sort(test_list))
