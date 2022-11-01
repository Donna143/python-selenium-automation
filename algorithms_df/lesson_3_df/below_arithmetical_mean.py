# Below the Arithmetical Mean
# When given a list, the program should return a list of all the elements below
# the original list's arithmetical mean. The arithmetical mean is the sum of all
# elements divided by the number of elements.
# Example: [1, 3, 5, 6, 4, 10, 2, 3] (The arithmetical mean is 4.25).
# Return [1, 3, 4, 2, 3]

# O(n)

def below_mean(arr):
    total = 0
    for num in arr:
        total = total + num
    mean = total / len(arr)

    result_arr = []
    for num in arr:
        if num < mean:
            result_arr.append(num)

    return result_arr


test_arr = [1, 3, 5, 6, 4, 10, 2, 3]  # [1, 3, 4, 2, 3]
print(below_mean(test_arr))
