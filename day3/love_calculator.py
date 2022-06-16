# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()
count_t1 = lower_case_name1.count("t")
count_r1 = lower_case_name1.count("r")
count_u1 = lower_case_name1.count("u")
count_e1 = lower_case_name1.count("e")
count_l1 = lower_case_name1.count("l")
count_o1 = lower_case_name1.count("o")
count_v1 = lower_case_name1.count("v")
count_e2 = lower_case_name1.count("e")

count_t2 = lower_case_name2.count("t")
count_r2 = lower_case_name2.count("r")
count_u2 = lower_case_name2.count("u")
count_e3 = lower_case_name2.count("e")
count_l2 = lower_case_name2.count("l")
count_o2 = lower_case_name2.count("o")
count_v2 = lower_case_name2.count("v")
count_e4 = lower_case_name2.count("e")

true_count = count_t1 + count_r1 + count_u1 + count_e1 + count_t2 + count_r2 + count_u2 + count_e3


love_count = count_l1 + count_o1 + count_v1 + count_e2 + count_l2 + count_o2 + count_v2 + count_e4

score = str(true_count) +str(love_count)

int_score= int(score)



if int_score <=10 or int_score >=90:
 print(f"Your score is {int_score}, you go togheter like coke and mentos.")
elif int_score >=40 and int_score <=50:
  print(f"Your score is {int_score}, you are alright togheter.")
else:
  print(f"Your score is {int_score}.")