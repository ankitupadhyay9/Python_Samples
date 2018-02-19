# move zeroes to the end of the array without changing the relative position of other elements
arr = [0,1,0,3,12]
for i in range(len(arr)):
  if arr[i] == 0:
    arr.append(0)
    arr.pop(i)

print arr

#more optimal approach
#find non zero elements, if found move them 
#in the end fill the tail of the array with Zeroes

arr = [0,0,0,0,12]
lastNonZero = 0

for i in range(len(arr)):
  if arr[i] != 0:
    arr[lastNonZero] = arr[i]
    lastNonZero += 1
  '''elif arr[i] != 0 and i > 0:
    lastNonZero += 1
    arr[lastNonZero] = arr[i]
'''
for i in range(lastNonZero,len(arr)):
  arr[i] = 0

print arr