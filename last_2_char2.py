# this prints last 2 characters of string
def extra_end(str):
  str2 = ""
  for i in range(3):
    str2 = str2 + str[-2:]
  return str2


  # first 2 characters
  def first_two(str):
  if len(str) >=2:
    return str[0:2]
  return str

'''
Return True if the string "cat" and "dog" appear the same number of times in the given string.

cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('1cat1cadodog') → True
'''
  def cat_dog(str):
  cat = 0
  dog = 0
  for i in range(2,len(str)):
    if str[i] == 't' and str[i-1] == 'a' and str[i-2] == 'c':
      cat = cat + 1
    if str[i] == 'g' and str[i-1] == 'o' and str[i-2] == 'd':
      dog = dog + 1
  if cat == dog:
    return True
  return False




 # return how many times string code appears in string
 # except we'll accept any letter for the 'd', so "cope" and "cooe" count.
 def count_code(str):
  code = 0
  for i in range(3,len(str)):
    if str[i] == 'e' and str[i-2] == 'o' and str[i-3] == 'c':
      code = code + 1
  return code






# compare end part of 2 strings
'''
Given two strings, return True if either of the strings appears at the very end of the other string, 
ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). 
Note: s.lower() returns the lowercase version of a string.

end_other('Hiabc', 'abc') → True
end_other('AbC', 'HiaBc') → True
end_other('abc', 'abXabc') → True
'''
  def end_other(a, b):
  if len(a) > len(b) and a[-len(b)::].lower() == b.lower():
    return True
  elif len(b) > len(a) and b[-len(a)::].lower() == a.lower():
    return True
  elif a.lower() == b.lower():
    return True
  return False



 ''' 
 Find first occurence of a character in a string
 return -1 if not found
 '''
 def findNeedle(str,needle):
  for i in range(len(str)):
    if str[i] == needle:
      return i

  return -1

print findNeedle("mystring","k")


