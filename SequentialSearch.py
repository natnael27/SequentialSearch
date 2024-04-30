def linear_search(arr, target):
 for i in range(len(arr)):
  if arr[i] == target:
   return i # Return the index if the target is found
 return -1 # Return -1 if the target is not found
# Example usage:
arr = [27, 34, 88, 1, 99, 77, 9, 8, 47, 66]
target = 1
print("Array:", arr)
print("Target:", target)
# Perform linear search
result = linear_search(arr, target)
if result != -1:
 print(f"Target found at index {result}.")
else:
 print("Target not found in the array.")
