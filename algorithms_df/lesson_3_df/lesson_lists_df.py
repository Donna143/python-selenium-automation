my_list = [1, 1, 8, 6, 1, 2, 3, 4, 5]
my_second_list = [6, 7]

# concatenate lists
final_list = my_list + my_second_list
print(final_list)

# list index
print(my_list[0])
print(my_list[1])
print(my_list[len(my_list)-1])
print(my_list[-1])

# add item to list
print(my_list)
my_list.append(17)
print(my_list)

# remove all elements from list
# my_list.clear()
# print(my_list)

# count how many elements
result = my_list.count(1)
print(result)

# get index of element
result = my_list.index(1)
print(result)
# result = my_list.index(9)
# print(result)

# insert element
result = my_list.insert(0, 99)
print(my_list)

# remove element
result = my_list.pop(-1)
print(my_list)
result = my_list.remove(3)
print(my_list)

# reverse list
my_list.reverse()
print(my_list)

# ascending or descending order
my_list.sort()
print(my_list)
my_list.sort(reverse=True)
print(my_list)