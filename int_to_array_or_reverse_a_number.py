# this function creates an array out of an integer
# this can also be used to reverse a number

def createArrayFromInt(n):
  arr = []
  while n > 10:
    arr.append(int(n%10))
    n = n/10
  arr.append(int(n))
  return arr
  
print createArrayFromInt(123)


## Recursive version - own
def createArrayFromInt(n):
  if n <= 10:
    return str(int(n))

  return str(int(n%10)) + createArrayFromInt(n/10)