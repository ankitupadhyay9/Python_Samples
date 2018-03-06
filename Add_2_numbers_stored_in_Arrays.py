# numbers stored in array in reverse
# find the sum of numbers and store them in array in reverse

def findSum(a,b):
  if len(a) == 0:
    return b
  elif len(b) == 0:
    return a
    
    
  # if one array is greater in length then append 0s to the smaller one
  if len(a) > len(b):
    diff = len(a) - len(b)
    for i in range(diff):
      b.append(0)
  elif len(b) > len(a):
    diff = len(b) - len(a)
    for i in range(diff):
      a.append(0)
    
  carry = 0
  res = []
  for i in range(len(a)):
    s = carry + a[i] + b[i]
    if s >= 10:
      carry = int(s/10)
      s = s%10
    else:
      carry = 0
  
    res.append(s)
  if carry > 0:
    res.append(carry)

  return res

a = [9,9,9,9,9,9,9]
b = [1,6,8,2,6,7]

print findSum(a,b)

