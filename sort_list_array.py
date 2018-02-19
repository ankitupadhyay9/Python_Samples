# Sorting an array or list


# Bubble sort
# Idea is to bubble up the largest (or smallest) item
# second largest, third largest and so on
# complexity O(n*n)
def sortList(myList):
  
  for i in range(len(myList)):
    for j in range(len(myList) - 1 - i):
      if myList[j] > myList[j + 1]:
        # swap the tuple
        (myList[j],myList[j + 1]) = (myList[j + 1], myList[j])
  return myList

arr = [2,100,1,10,9,0,-1]
print sortList(arr)

# if it is a string
# do a minor change in above function
def sortList(myList):
  
  for i in range(len(myList)):
    for j in range(len(myList) - 1 - i):
      if myList[j] > myList[j + 1]:
        # swap the tuple
        (myList[j],myList[j + 1]) = (myList[j + 1], myList[j])
  return "".join(myList)

str = list("dbcaA")
print sortList(str)


# Insertion sort
# Complexity O(nlogn) , worst O(n*n)
myArray = [3,1,4,5,10,2,7,100]
res = [myArray[0]]


  
for i in range(1,len(myArray)):
  res.append(myArray[i])
  j = i
  while j > 0:
    if res[j] < res[j-1]:
      # "swapping"
      (res[j],res[j-1]) = (res[j-1], res[j])
      j = j -1
    else:
      break

print res  
    

# Mergesort
# Divide and Conquer
# Complexity always O(nlogn)
def merge(a,b):
  c = []
  while len(a) > 0 and len(b) > 0:
    if a[0] < b[0]:
      c.append(a[0])
      a.remove(a[0])
    else:
      c.append(b[0])
      b.remove(b[0])
  if len(a) == 0:
    c = c + b
  else:
    c = c + b
  return c
  
def mergeSort(myList):
  
  if len(myList) == 1:
    return myList
  else:
    
    middle = int(len(myList)/2)
    
    a = mergeSort(myList[:middle])
    b = mergeSort(myList[middle:])
    return merge(a,b)


  
myArray = [3,1,4,2,7,9,10]
print mergeSort(myArray)




