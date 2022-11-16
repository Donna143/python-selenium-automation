

def bubble_sort_decr(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


test_list = [4, 2, 6, 3, 1]
print(test_list)
print(sorted(test_list, reverse=True))
print(bubble_sort_decr(test_list))
