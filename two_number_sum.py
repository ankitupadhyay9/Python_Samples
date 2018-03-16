# complexity O(n*n)
# find indexes of numbers which add up to the given number
def twoSum(arr, sum):
  for i in range(len(arr)):
    for j in range(i+1, len(arr)):
      if arr[i] + arr[j] == sum:
        return i,j

myarray = [1,7,2,0]
print str(twoSum(myarray, 33))


# complexity O(n) - 2 pass 
# In this approach we copy the array in a hash table
# and then we scan the hash table for the complement 
# i.e. if i + some = sum 
# some = sum - i
def twoSum(arr, sum):
  myHash = {}
  for i in range(len(arr)):
    myHash[arr[i]] = i
  
  for i in range(len(arr)):
    if (sum-arr[i]) in myHash and myHash.get(sum-arr[i]) != i:
      return myHash.get(sum-arr[i]) , i
  return -9,-9

myArray = [1,7,2,10]
print str(twoSum(myArray, 12))


# complexity O(n) - 1 pass 
def twoSum(arr, sum):
  myHash = {}
  # here we are checking while creating the hash table itself
  for i in range(len(arr)):
    myHash[arr[i]] = i
    if (sum-arr[i]) in myHash and myHash.get(sum-arr[i]) != i:
      return myHash.get(sum-arr[i]) , i
  
  return -9,-9

myArray = [1,7,2,10]
print str(twoSum(myArray, 12))