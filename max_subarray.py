'''
Find maximum sum a subarray can have in an array
Kadane's Algorithm
'''

def maxSubArray(arr):
  max_so_far = 0
  max_ending_here = 0
  
  for i in range(len(arr)):
    max_ending_here = max_ending_here + arr[i]
    
    if max_ending_here < 0:
      max_ending_here = 0
    if max_so_far < max_ending_here:
      max_so_far = max_ending_here
  
  return max_so_far


myArr = [-1,-2,10,-9,8,3,1,-8]
print maxSubArray(myArr)