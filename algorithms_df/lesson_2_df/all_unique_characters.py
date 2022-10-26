# Given a string, determine if it consists of all unique characters.
# For example, the string 'abcde' has all unique characters and should return True.
# The string 'aabcde' contains duplicate characters and should return False.

def all_unique_char(s):
    count = {}
    for letter in s:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 1:
            return False

    return True


string1 = 'abcde'
string2 = 'aabcde'
print(all_unique_char(string1))
print(all_unique_char(string2))

