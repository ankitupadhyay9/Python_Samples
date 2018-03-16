'''
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory. 
For example,
 Given input array nums = [1,1,2], 
Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length. 
'''

# first solution is by creating another array
arr = [1,2,2,5,6,7,7,8,9]
rem = []
# copy to the second array only when elements are not duplicate
for i in range(len(arr)):
  if i == 0:
    rem.append(arr[i])
  elif i > 0 and arr[i] != arr[i-1]:
    rem.append(arr[i])
count = 0
print rem
print arr

# another approach  - not using another array - O(n*n)
arr = [1,2,2,5,6,7,7,8,9]
temp = 0
dupCount = 0

for i in range(len(arr)):
  if i > 0 and arr[i] == arr[i-1]:
    # we found a duplicate
    dupCount += 1
    # loop through rest of the array to change the index by -1
    for j in range(i, len(arr)-1):
      arr[j] = arr[j+1]

# trim the array original length minus duplicates
arr = arr[0:len(arr)-dupCount+1]
print arr


# another approach  - not using another array - O(n)
arr = [1,2,3,5,6,7,7,8,9,9]
i = 0
nondup = 0
for j in range(len(arr)):
  if arr[i] != arr[j]:
    # till the time arr[i] = arr[j] then dont increment i
    # as soon as they are not equal that means there is a new element
    # so copy the new element
    i = i + 1
    nondup = nondup + 1
    arr[i] = arr[j]

arr = arr[0:nondup + 1]
print arr