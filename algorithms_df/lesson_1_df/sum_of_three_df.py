# O(1)

def sum_of_three(n):
    result = 0
    while n != 0:
        result = result + (n % 10)
        n = n // 10
    return result

    # for i in str(n):
    #     result = result + int(i)
    # return result


print(sum_of_three(512))
