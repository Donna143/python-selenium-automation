def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False

    count = {}
    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

        for letter2 in s2:
            if letter2 in count:
                count[letter2] -= 1
            else:
                count[letter2] = 1
                # return False

            for k in count:
                if count[k] != 0:
                    return False

            return True

    # return sorted(s1) == sorted(s2)


test_s1 = 'abcDe'
test_s2 = 'abced'
print(is_anagram(test_s1, test_s2))