# Given a string, determine if it consists of all unique characters.
# For example, the string 'abcde' has all unique characters and should return True.
# The string 'aabcde' contains duplicate characters and should return False.

def all_unique_char(s):
    # return len(set(s)) == len(s)

    # chars = set()
    # for let in s:
    #     if let in chars:
    #         return False
    #     else:
    #         chars.add(let)
    # return True
    
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

