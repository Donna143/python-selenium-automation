# Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'.
# For this problem, you can falsely "compress" strings of single or double letters.
# For instance, it is okay for 'AAB' to return 'A2B1' even though this technically takes more space.
# The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.

def compress(s):
    if len(s) == 0:
        return ''

    if len(s) == 1:
        return s + '1'

    compressed = ''
    cnt = 1
    i = 1

    while i < len(s):
        if s[i] == s[i - 1]:
            cnt += 1
        else:
            compressed = compressed + s[i - 1] + str(cnt)
            cnt = 1
        i += 1

    compressed = compressed + s[i - 1] + str(cnt)
    return compressed


print(compress('AAAABBBBCCCCCDDEEEE'))

