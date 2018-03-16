'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

'''


str = "((()))"
# create a hash table of all string characters and assign it to zero
my_hash = {'{':0,'}':0, '(':0, ')':0}
for i in str:
  # increase the value when that key is found
  if i in my_hash:
    my_hash[i] += 1
  else:
    my_hash[i] = 1
if my_hash['{'] == my_hash['}'] and my_hash['('] == my_hash[')']:
  print "True"
else:
  print "False"

for word, times in my_hash.items():
  print word, times
