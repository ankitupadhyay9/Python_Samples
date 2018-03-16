'''
657. Judge Route Circle 
Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place. 

The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle. 

Example 1:

Input: "UD"
Output: true

Example 2:

Input: "LL"
Output: false
'''

def judgeCircle(self, moves):
    """
    :type moves: str
    :rtype: bool
    """
    moves_hash = {"R":0, "L":0, "U":0,"D":0}
    total = 0
    for i in moves:
        moves_hash[i] += 1
    print moves_hash
    if moves_hash["R"] == moves_hash["L"] and moves_hash["U"] == moves_hash["D"]:
        return True
    return False