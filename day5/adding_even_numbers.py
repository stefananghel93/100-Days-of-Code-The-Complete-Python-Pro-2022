#Write your code below this row 👇

total = 0 
for x in range(0,101,2):
  total+=x
print(total)  

total2 = 0
for x in range(0,101,2):
  if x%2 ==0:
   total2 += x
print(total2)
