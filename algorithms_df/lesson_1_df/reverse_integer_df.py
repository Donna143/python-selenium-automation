def reverse_integer(x):
    string = str(x)

    if string[0] == '-':
        return int('-' + string[:0:-1])
    else:
        return int(string[::-1])


test_x_pos = 123
test_x_neg = -876
print(reverse_integer(test_x_pos))
print(reverse_integer(test_x_neg))
