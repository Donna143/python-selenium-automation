
def recursion(number):
    if number == 0:
        return
    print(number)
    number -= 1
    recursion(number)
    

recursion(10)
