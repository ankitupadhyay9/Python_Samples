'''
arr =['a','b','c','d','c','b','k']
arr2 = ['a','b','b','a']

print arr[:int(len(arr))-int(len(arr)/2)-1:-1]
print arr[0:int(len(arr))-int(len(arr)/2)-1]

#print len(arr2)-len(arr2)/2
print arr2[:int(len(arr2)-len(arr2)/2)-1:-1]
print arr2[0:int(len(arr2)-len(arr2)/2):]
'''

def checkPalindrome(str):
  if len(str)%2 == 0:
    if str[:int(len(str)-len(str)/2)-1:-1] == str[0:int(len(str)-len(str)/2):]:
      return "True"
  else:
    if str[:int(len(str))-int(len(str)/2)-1:-1] == str[0:int(len(str))-int(len(str)/2)-1]:
      return "True"
  return "False"

myStr = ['A','B','C','C','B','A']
print checkPalindrome(myStr)  