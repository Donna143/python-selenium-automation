# O(n)

def is_mountain(arr):
    i = 1
    while i < len(arr) and arr[i] > arr[i - 1]:
        i = i + 1
    if i == 1 or i == len(arr):
        return False
    while i < len(arr) and arr[i] < arr[i - 1]:
        i = i + 1

    return i == len(arr)


test1 = [1, 3, 5, 3, 2]     # True
test2 = [1, 2, 3, 4]        # False
test3 = [4, 3, 2, 1]        # False
test4 = [1, 3, 4, 2, 7]     # False
print(is_mountain(test1))
print(is_mountain(test2))
print(is_mountain(test3))
print(is_mountain(test4))