# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
sum = 0
for n in student_heights:
  sum += n
items = 0
for i in student_heights:
  items += 1 
average = round(sum/items)
print(average)



