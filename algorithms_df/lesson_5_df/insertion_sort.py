

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr


test_list = [4, 2, 6, 7, 1, 3]
print(test_list)
print(sorted(test_list))
print(insertion_sort(test_list))
