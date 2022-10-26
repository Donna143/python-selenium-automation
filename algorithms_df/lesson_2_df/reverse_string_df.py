# O(n)

def reverse_string(s):
    # return s[::-1]

    reversed_s = ''
    index = len(s) - 1
    while index >= 0:
        reversed_s += s[index]
        index -= 1
    return reversed_s


test_s = 'abcde'
print(reverse_string(test_s))
