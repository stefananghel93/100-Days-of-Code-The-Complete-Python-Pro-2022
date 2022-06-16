# # 🚨 Don't change the code below 👇
age = input("What is your current age?")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# age_as_int = int(age)
# current_age_weeks = age_as_int * 52
# current_age_days = age_as_int * 365
# current_age_months = age_as_int * 12

# y90_weeks = 90 * 52
# y90_days = 365 * 90
# y90_months = 12 * 90

# days_left = y90_days - age_as_int * 365
# weeks_left = y90_weeks - age_as_int * 52
# months_left = y90_months - age_as_int * 12

# message = (
#     f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left."
# )
# print(message)
age_as_int = int(age)
years_left = 90-age_as_int
days_left=years_left*365
months_left=years_left*12
weeks_left=years_left*52
print(days_left)

message = (
f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left."
)
print(message)