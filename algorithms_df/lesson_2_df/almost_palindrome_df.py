# O()

def is_almost_palindrome(s):
    for i in range(len(s)):
        t = s[:i] + s[i + 1:]
        if t == t[::-1]:
            return True
    return False


test_s_pos = 'radkar'
test_s_neg = 'radario'
print(is_almost_palindrome(test_s_pos))
print(is_almost_palindrome(test_s_neg))
