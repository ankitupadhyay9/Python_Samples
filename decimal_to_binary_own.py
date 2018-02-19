# this function converts decimal to binary for numbers upto 536,870,912
def convertToBinary(num):
  binary_table = []
  b = 0
  # create a table of powers of 2s
  while b < 30:
    binary_table.append(2**b)
    b = b + 1
  
  # this will be something like binary_table = [1,2,4,8,16,32,64,128,256,512,1024...]
  #instead I found a better way
  binary_table = [2**b for b in range(30)]
  my_keys = {}
  n = num
  # try to find the value in binary_table
  # if found add it in the hash table
  while n > 0:
    i = 0
    while n >= binary_table[i]:
      i = i + 1
    
    if binary_table[i-1] in my_keys:
      my_keys[binary_table[i-1]] += 1
    else:
      my_keys[binary_table[i-1]] = 1
    n = n - binary_table[i-1]
   
  # my_keys will be something like {4: 1, 8: 1, 16: 1, 32: 1, 64: 1}
  i = 0
  arr = []
  # then create the binary numbers using keys
  while 2**i <= num:
    if 2**i in my_keys:
      arr.append(1)
    else:
      arr.append(0)
    i = i + 1
  return arr[::-1]

print convertToBinary(124)
    
    
