# convert Roman number to Integer
'''
Given a roman numeral, convert it to an integer.
Input is guaranteed to be within the range from 1 to 3999.
'''

def romanToInt(self, s):
    """
    :type s: str
    :rtype: int
    """
    res = 0
    #print s
    # create a hash table of roman numbers
    roman = {}
    roman['I'] = 1
    roman['IV'] = 4
    roman['V'] = 5
    roman['IX'] = 9
    roman['X'] = 10
    roman['XL'] = 40
    roman['L'] = 50
    roman['XC'] = 90
    roman['C'] = 100
    roman['CD'] = 400
    roman['D'] = 500
    roman['CM'] = 900
    roman['M'] = 1000
    
    for i in range(len(s)-1):            
        if roman[s[i]] < roman[s[i+1]]:
            res = res - roman[s[i]]
        else:
            res = res + roman[s[i]]
       
    return res + roman[s[len(s)-1]]