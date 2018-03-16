str = "ok now count unique words in this string but dont count Unique words thrice thrice Thrice"
print(str)
myhash = {}
for w in (str.split()):
  if w.lower() in myhash:
    myhash[w.lower()] += 1
  else:
    myhash[w.lower()] = 1
for word, times in myhash.items():
  print((word,times))
  