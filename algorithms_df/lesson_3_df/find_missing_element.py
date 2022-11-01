# O(n)

import collections


def find_missing_1(arr1, arr2):
    arr1.sort()
    arr2.sort()

    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1
    return arr1[-1]


def find_missing_2(arr1, arr2):
    d = collections.defaultdict(int)

    for num in arr2:
        d[num] += 1

    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num] -= 1


list1 = [2, 5, 3, 1]
list2 = [2, 1, 3]
result = find_missing_2(list1, list2)
print(result)
