file = open('Vokstest.txt','r')
lines = file.readlines()
lines.sort()

with open('Vokstest.txt', 'w') as f:
 for line in lines:
  f.write(line)   # <-- Write the lines back
file.close()