# O(1)

# 2017 is not a leap year
# 1900 is not a leap year
# 2012 is a leap year
# 2000 is a leap year

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f'{year} is a leap year')
            else:
                print(f'{year} is not a leap year')
        else:
            print(f'{year} is a leap year')
    else:
        print(f'{year} is not a leap year')


is_leap_year(2017)
is_leap_year(1900)
is_leap_year(2012)
is_leap_year(2000)
