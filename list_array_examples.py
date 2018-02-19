#simple loop for lists or arrays
def count_evens(nums):
  even = 0
  for i in range(len(nums)):
    if nums[i]%2 == 0:
      even += 1
  return even

  #return the difference between smallest and largest number in array
  def big_diff(nums):
  big = 0
  small = 0
  for i in range(len(nums)):
    if i == 0:
      big = nums[i]
      small = nums[i]
    if nums[i] > big:
      big = nums[i]
    if nums[i] < small:
      small = nums[i]
  
  return big - small

  #return the sum of the array, dont count 13 and next element to 13
  def sum13(nums):
  sum = 0
  for i in range(len(nums)):
    if i == 0 and nums[i] != 13:
      sum = sum + nums[i]
    elif i > 0 and nums[i] != 13 and nums[i-1] != 13:
      sum = sum + nums[i]
  return sum


