##makebricks problem

def make_bricks(small, big, goal):
  if small + (big*5) == goal:
    return True
  elif small + (big*5) < goal:
    return False
  elif goal%5 > small:
    return False
  ##if we remove big bricks from total and reach the goal
  elif small + (big*5) > goal and (((small + (big*5)) - goal)%5 == 0):
    return True
  ##if we remove small bricks from total and reach the goal
  elif small + (big*5) > goal and ((small + (big*5)) - goal) <= small:
    return True
  return True