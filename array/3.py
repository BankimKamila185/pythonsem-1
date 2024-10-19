def sheesh(arr):
  

  x = (arr[0] + arr[-1]) * 5 // 2

  y = sum(arr)

  z = x - y

  return z


arr = [1, 2, 3, 5]
arr=[20,21,23,24]
z = sheesh(arr)
print("The missing number is:", z)