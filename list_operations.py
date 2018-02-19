#list operations

# return true if first and last element of the array is 6
def first_last6(nums):
  if len(nums) == 1 and nums[0] == 6:
    return True
  elif len(nums) > 1 and (nums[0] == 6 or nums[len(nums)-1] == 6):
    return True
  return False


# return True if first and last element of the array are equal and array size >= 1
def same_first_last(nums):
  
  if len(nums) >= 1 and (nums[0] == nums[len(nums) - 1]):
    return True
  return False

 #return True if they have the same first element or they have the same last element
 def common_end(a, b):
  if a[0] == b[0] or a[len(a)-1] == b[len(b)-1]:
    return True
  return False


#return sum of all elements of array
def sum3(nums):
  a = 0
  for i in range(len(nums)):
    a = a + nums[i]
  return a

 #concatenate 2 list of integers
 def rotate_left3(nums):
  return nums[1:] + map(int, str(nums[0]))



 #loop a string in reverse order
 def reverse3(nums):
  result = []
  for i in range(len(nums)-1, -1, -1):
    result.append(nums[i])
  
  return result


 #loop a list of ints
 def max_end3(nums):
  result = []
  if nums[0] > nums[len(nums)-1]:
    for i in range(len(nums)):
      result.append(nums[0])
    return result
  for i in range(len(nums)):
    result.append(nums[len(nums)-1])
  return result


 #loop through a list and print sum of first 2 elements
 def sum2(nums):
  result = 0
  if len(nums) == 0:
    return 0
  for i in range(len(nums)):
    result = result + nums[i]
    if i > 0:
      return result
  return result


#concatenate middle elements of 2 arrays
def middle_way(a, b):
  
  return [a[int(math.ceil(len(a)/2))], b[int(math.ceil(len(a)/2))]]


 #return an array containing first and last elements of array
 def make_ends(nums):
  return [nums[0], nums[len(nums)-1]]

#return True if an array contains 2 or 3
def has23(nums):
  for i in range(len(nums)):
    if nums[i] == 2 or nums[i] == 3:
      return True
  return False


  

