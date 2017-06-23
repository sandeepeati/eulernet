# number of sundays fell on the first day of a month in the twentieth century

# function for finding a leap year or not

def leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    return False

first_day_ly = [1, 32, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366]
first_day_nly = [1, 32, 61, 92, 122, 153, 183, 214, 245, 275, 306, 336, 367]

# since jan1 1900 is monday and 1900 is a non leap year, jan1 1901 is tuesday

sunday = 6
count = 0
for i in range(1901,2001):
    if leap_year(i):
        while sunday <= 366:
            if sunday in first_day_ly:
                count += 1
            sunday += 7
    else:
        while sunday <= 365:
            if sunday in first_day_nly:
                count += 1
            sunday += 7
    sunday -= 365

print(count)


