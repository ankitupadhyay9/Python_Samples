'''
One Away: There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.
EXAMPLE
pale, ple -> true 
pales, pale -> true 
pale, bale -> true 
pale, bake -> false
'''

def oneEditAway(str1,str2):
  hash1 = {}
  hash2 = {}
  differ = 0
  # create hash table of both the strings and then compare them
  for i in range(len(str1)):
    if str1[i] in hash1:
      hash1[str1[i]] += 1
    else:
      hash1[str1[i]] = 1
  for i in range(len(str2)):
    if str2[i] in hash2:
      hash2[str2[i]] += 1
    else:
      hash2[str2[i]] = 1
  
  if abs(len(hash1) - len(hash2)) > 1:
    return False
  if len(hash1) > len(hash2):
    
    for word, times in hash1.items():
      if word not in hash2:
        differ +=1 
        if differ > 1 :
          return False
        if times > 1:
          return False
      if word in hash2:
        if abs(hash1[word] - hash2[word]) > 1:
          return False
  else:
    for word, times in hash2.items():
      if word not in hash1:
        differ +=1 
        if differ > 1 :
          return False
        if times > 1:
          return False
      if word in hash1:
        if abs(hash2[word] - hash1[word]) > 1:
          return False
  return True

print oneEditAway('pales','pale')
      
