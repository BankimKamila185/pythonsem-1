def replace_odd_number(numbers):
  

  for i in range(len(numbers)):
    if numbers[i] % 2 != 0:
      numbers[i] = -1
  return numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = replace_odd_number(numbers)
print(result)  
