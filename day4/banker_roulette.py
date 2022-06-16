# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
import random
#Write your code below this line 👇

x = len(names)-1
random_names=random.randint(0,x)
person = names[random_names]
print(f"{person} will pay the bill today!")






