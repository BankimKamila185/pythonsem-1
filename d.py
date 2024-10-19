year = int(input("Enter a year: "))
is_leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
print(f"{year} is a leap year." if is_leap else f"{year} is not a leap year.")
