from time import strptime

month_name = input("Enter the name of the month: ")
month_number = strptime(month_name, '%B').tm_mon

print(f"The month number for {month_name} is {month_number}")
