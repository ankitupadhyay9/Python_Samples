## make choclate problem
def make_chocolate(small, big, goal):
  if small + (big*5) < goal:
    return -1
  elif goal%5 > small:
    return -1
  elif goal < 5 and goal <= small:
    return goal
  elif goal%5 == 0 and big*5 >= goal:
    return 0
  elif goal%5 == 0 and (big*5 + small) >= goal:
    return small - big
  elif goal%5 <= small:
    return goal - big*5
  