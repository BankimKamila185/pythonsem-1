def count_occurrences(arr, element):

  count = 0
  for num in arr:
    if num == element:
      count += 1
  return count

arr = [1, 2, 3, 4, 2, 5, 2]
element = 2
result = count_occurrences(arr, element)
print("The number of occurrences of", element, "in the array is:", result)
