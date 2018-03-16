'''
Given a string, compute recursively (no loops) a new string where all the lowercase 'x' chars have been changed to 'y' chars.
'''

def replaceX (str):
  print 'input:',str
  if len(str) == 0:
    return str
  if len(str) == 1 and str == 'x':
    return 'y'
  elif len(str) == 1 and str != 'x':
    return str
  mid = int(len(str)/2)
  return replaceX(str[0:mid]) + replaceX(str[mid:len(str)])

print replaceX('abcxabc')