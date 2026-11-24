# Function to right rotate the list 'arr' by 'k' places in-place
def rotate_right(arr, k):
  # Find the total number of elements in the array
  n = len(arr)

  # If the array is empty or has only 1 element, rotation changes nothing
  if n <= 1:
    return arr

  # Handle cases where k is larger than or equal to n (e.g., rotating 5 elements by 7 is same as by 2)
  k = k % n

  # If k is 0 after modulo, no rotation is needed
  if k == 0:
    return arr

  # Helper function to reverse a portion of 'arr' from index 'left' to 'right'
  def reverse(left, right):
    # Keep swapping until the two pointers meet or cross in the middle
    while left < right:
      # Swap the elements at 'left' and 'right' positions
      arr[left], arr[right] = arr[right], arr[left]
      # Move the left pointer one step forward
      left += 1
      # Move the right pointer one step backward
      right -= 1

  # Step 1: Reverse the entire array (moves the last k elements to the front in reverse order)
  reverse(0, n - 1)

  # Step 2: Reverse the first k elements to restore their original order
  reverse(0, k - 1)

  # Step 3: Reverse the remaining elements from index k to n - 1 to restore their original order
  reverse(k, n - 1)

  # Return the rotated array
  return arr


# Example usage
nums = [1, 2, 3, 4, 5, 6, 7]  # Original array
k = 3 # Number of right rotations
result = rotate_right(nums, k)  # Rotate the array by 3 places
print(result)  # Output: [5, 6, 7, 1, 2, 3, 4]
