def merge_sort_desc(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    return merge_arrays_desc(merge_sort_desc(arr[:middle]), merge_sort_desc(arr[middle:]))


def merge_arrays_desc(left_arr, right_arr):
    merged_array = []
    i = j = 0

    while i < len(left_arr) or j < len(right_arr):
        if i == len(left_arr):
            merged_array.append(right_arr[j])
            j += 1
            continue
        if j == len(right_arr):
            merged_array.append(left_arr[i])
            i += 1
            continue

        if left_arr[i] >= right_arr[j]:
            merged_array.append(left_arr[i])
            i += 1
        else:
            merged_array.append(right_arr[j])
            j += 1

    return merged_array


test_list = [4, 6, 3, 1]
print(merge_sort_desc(test_list))
