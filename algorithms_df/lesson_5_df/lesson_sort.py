list_of_numbers = [5, 3, 1, 6]
print(list_of_numbers)
print(sorted(list_of_numbers))
print(list_of_numbers)
list_of_numbers.sort()
print(list_of_numbers)
list_of_numbers.sort(reverse=True)
print(list_of_numbers)

list_of_words = ['banana', 'kiwi', 'apple', 'orange']
print(list_of_words)
print(sorted(list_of_words))
print(sorted(list_of_words, key=len))
print(sorted(list_of_words, key=len, reverse=True))


