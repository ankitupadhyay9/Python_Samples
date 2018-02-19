
##################  IF - ELSE logical operators ####################

def cigar_party(cigars, is_weekend):
  if is_weekend:
    if cigars >= 40:
      return True
    return False
  if cigars >= 40 and cigars <= 60:
    return True
  
  return False


'''
Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum.

lone_sum(1, 2, 3) → 6
lone_sum(3, 2, 3) → 2
lone_sum(3, 3, 3) → 0
'''
 def lone_sum(a, b, c):
  if a != b and b != c and c != a:
    return a+b+c
  elif a == b and a != c:
    return c
  elif b == c and a != b:
    return a
  elif a == c and a!= b:
    return b
  elif a == b and b == c:
    return 0

'''
Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13..19 inclusive -- then that value counts as 0, 
except 15 and 16 do not count as a teens. 
Write a separate helper "def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule. I
n this way, you avoid repeating the teen code 3 times (i.e. "decomposition"). Define the helper below and at the same indent level as the main no_teen_sum().
'''
def no_teen_sum(a, b, c):
  return fix_teen(a) + fix_teen(b) + fix_teen(c)

def fix_teen(n):
  if n >= 13 and n <= 19 and n != 15 and n != 16:
    return 0
  else:
    return n


'''
For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more, so 15 rounds up to 20. 
Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 5, so 12 rounds down to 10. Given 3 ints, a b c, 
return the sum of their rounded values. 
To avoid code repetition, write a separate helper "def round10(num):" and call it 3 times. 
Write the helper entirely below and at the same indent level as round_sum()
'''
def round_sum(a, b, c):
  return round10(a) + round10(b) + round10(c)

def round10(num):
  if num%10 == 0:
    return num
  elif num%10 == 5:
    return num+5
  elif num%10 > 5:
    return num - (num%10) + 10
  elif num%10 < 5:
    return num - (num%10)



