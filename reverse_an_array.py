# reverse an array

# using the minus index
a = [1,2,3,4,5,6]
b = []
for i in a:
  b.append(a[-i])

print b

# string array using the loop
x = ['Ankit','Jasmeet','Sandip','Ganesan','Balaji']
y = []

for i in range(len(x)):
  y.append(x[len(x) - 1- i])

print y

# string array using string inbuilt function
x = ['Ankit','Jasmeet','Sandip','Ganesan','Balaji']
y = x[::-1]


print y
