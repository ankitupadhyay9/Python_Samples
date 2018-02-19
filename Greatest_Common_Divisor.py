# Iterative solution
def findGCD(a,b):
  
  while a != b:
    if a > b:
      a = a - b
    else:
      b = b - a
  return a

print findGCD(108,12)

# recursive solution
def findGCDRecur(a,b):
  if a == 0 or b == 0:
    return 0
  if a == b:
    return a
  if a > b:
    return findGCDRecur(a-b,b)
  else:
    return findGCDRecur(a,b-a)
