sum_evens = sum(number for number in range(100) if number % 2 == 0)
sum_odds = sum(number for number in range(100) if number % 2 != 0)

print(f"The sum of all evens is {sum_evens}.")
print(f"The sum of all odds is {sum_odds}.")
