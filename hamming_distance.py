# program to calculate hamming distance
'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, calculate the Hamming distance.
Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.
'''
def binary(n):
  return '{0:b}'.format(n).rjust(4,'0')
  
def hammingDist(num1, num2):
  result = 0
  a = map(int, binary(num1))
  b = map(int, binary(num2))
  for i in range(4):
    #print i
    if a[i] != b[i]:
      result = result + 1
  return result
      
  

print hammingDist(4,1)