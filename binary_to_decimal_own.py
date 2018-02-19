def convertToDecimal(n):
  arr = list(str(n))
  print arr
  i = len(arr) - 1
  #print i
  dec = 0
  while i >= 0:
    dec = dec + 2**i*int(arr[(len(arr)-i-1)])
    #print i, 2**i,dec
    i = i - 1
  return dec

print convertToDecimal('0101011010')