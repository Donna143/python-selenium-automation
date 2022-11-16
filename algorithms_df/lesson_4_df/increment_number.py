# Write a program that takes as input a list of digits encoding a nonnegative decimal
# integer D and updates the list to represent the integer D + 1.
# For example, if the input is [1, 2, 9] then you should update the array to [1, 3, 0].


def increment_number(arr):
    full_num = ''
    for num in arr:
        full_num = full_num + str(num)
    full_num = str(int(full_num)+1)
    arr.clear()
    for num in full_num:
        arr.append(int(num))

    # arr[-1] += 1
    # for i in reversed(range(1, len(arr))):
    #     if arr[i] != 10:
    #         break
    #     arr[i] = 0
    #     arr[i - 1] += 1
    # if arr[0] == 10:
    #     arr[0] = 1
    #     arr.append(0)

    return arr


test_list = [1, 2, 9]
test_list2 = [9, 9, 9]
result_list = increment_number(test_list)
result_list2 = increment_number(test_list2)
print(result_list)
print(result_list2)
