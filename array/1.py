def reverse_array(arr):

  
  reversed_arr = []

  for i in range(len(arr) - 1, -1, -1):
    reversed_arr.append(arr[i])

  return reversed_arr

array=input('Enter items')
reversed_array = reverse_array(array)
print(reversed_array)  