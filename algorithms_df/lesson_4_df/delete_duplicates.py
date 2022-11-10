# Write a program that takes as input a sorted array and updates it so that all duplicates
# have been removed and the remaining elements have been shifted left to fill the emtied indices.
# Fill the remaining indices with zeroes.
# Return the number of valid elements.
# You cannot use sets for this coding challenge.


def delete_duplicates(arr):
    write_index = 1

    for i in range(1, len(arr)):
        if arr[write_index - 1] != arr[i]:
            arr[write_index] = arr[i]
            write_index += 1

    for i in range(write_index, len(arr)):
        arr[i] = 0

    print(arr)
    return write_index


test_list = [2, 3, 3, 3, 5, 6, 7, 7, 8, 8, 10, 11]
result = delete_duplicates(test_list)
print(result)
