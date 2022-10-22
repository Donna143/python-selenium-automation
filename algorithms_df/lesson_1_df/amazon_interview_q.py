"""
HW 5
4** Amazon interview question:
Create a function that will take a string as an input
and return the 1st unique letter of a string.
"Google" => "l"
"Amazon" => "m"
If there are no unique letters, return an empty string: "xoxoxo" => "".
How would you test it? How would yyou handle edge cases?

"""


# def unique(string: str):
#     string = string.lower()
#     for l in string:  # O(n)
#         if string.count(l) == 1:  # O(n)
#             return l
# # => O(n^2)

def unique(string: str):  # O(n)
    # if type(string) != str:
    #     raise ValueError('Incorrect type')

    string1 = string.lower()
    d = {}
    for letter in string1:  # O(n)
        if letter not in d:
            d[letter] = 1
        else:
            d[letter] += 1
    print(d)

    for k,v in d.items():  # O(n)
        if v == 1:
            return k
    return ''


print(unique('Google'))
print(unique('Amazon'))
print(unique('xoxoxo'))
print(unique('73'))
print(unique('*%$'))
# print(unique(['d']))




