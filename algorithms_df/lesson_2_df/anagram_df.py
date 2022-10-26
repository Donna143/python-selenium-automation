# O(n)
def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False

    for i in s1:
        if i not in s2:
            return False
    return True

    # count = {}
    # for letter in s1:
    #     if letter in count:
    #         count[letter] += 1
    #         print(count)
    #     else:
    #         count[letter] = 1
    #         print(count)
    #
    # for letter in s2:
    #     if letter in count:
    #         count[letter] -= 1
    #         print(count)
    #     else:
    #         count[letter] = 1
    #         print(count)
    #         # return False
    #
    # for k in count:
    #     if count[k] != 0:
    #         return False
    #
    # print(count)
    # return True

    # return sorted(s1) == sorted(s2)


test_s1 = 'AbcDe'
test_s2 = 'abced'
print(is_anagram(test_s1, test_s2))

