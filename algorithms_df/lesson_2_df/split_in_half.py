# Given a string. Split it into two equal parts. Swap these parts and return the result.
# If the string has odd characters, the first part should be one character greater than the second part.
# Example: string = 'bbbbbcaaaaa'  Result = 'aaaaabbbbbc'

def split_in_half(s):
    if len(s) == 0:
        return ''

    if len(s) == 1:
        return s

    if len(s) % 2 == 0:
        half = len(s) // 2
    else:
        half = len(s) // 2 + 1

    return s[half:] + s[0:half]


string1 = 'bbbbbcaaaaa'
string2 = 'abcdefgh'
string3 = 'a'
print(split_in_half(string1))
print(split_in_half(string2))
print(split_in_half(string3))


