'''
This function calculates Fibonocci number at nth place using Dynamic Programming
'''

fibHash = {}
def fibDP(n):
  if n == 1:
    return 1
  if n == 0:
    return 0
  if n in fibHash:
    print "resued"
    return fibHash[n]
    
  # store the computed value in Hash table
  # Memoization
  fibHash[n-1] = fibDP(n-1)
  fibHash[n-2] = fibDP(n-2)
  
  print fibHash
  return fibDP(n-1) + fibDP(n-2)

print fibDP(10)
  