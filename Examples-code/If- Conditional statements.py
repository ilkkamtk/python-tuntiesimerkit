# # Voting age check: 
# voting_age = 18

# user_age = int(input("Please enter your age: "))

# if user_age >= voting_age:
#     print("You are old enough to vote in Finnish parliamentary elections.")
# else:
#     """
#     # explicitly calculated 
#     years_left = voting_age - user_age
#     print("You are not yet old enough to vote in Finnish parliamentary elections.")
#     print("You need to wait", years_left, "more year(s) to reach the voting age of 18.")
#     """
#     print("You are not yet old enough to vote in Finnish parliamentary elections.")
#     print("You need to wait " + str(voting_age - user_age) + " more year(s) to reach the voting age of 18.")
#     # print using f-string
#     print(f"You need to wait {voting_age - user_age} more year(s) to reach the voting age of 18.")

# # Electricity calculator 

# limit_1 = 50
# limit_2 = 200

# limit1_price = 0.10
# limit2_price = 0.08
# limit3_price = 0.06

# consumption = float(input("Please enter your electricity consumption in kWh: "))

# if consumption <= limit_1:
#     bill = consumption * limit1_price
# elif consumption <= limit_2:
#     bill = (limit_1 * limit1_price) + ((consumption - limit_1) * limit2_price)
# else:
#     bill = (limit_1 * limit1_price) + ((limit_2 - limit_1) * limit2_price) + ((consumption - limit_2) * limit3_price)

# # use round(variable,decimal numbers)
# print("Your electricity bill is €" + str(round(bill, 2)))

# Scholarship check: 
phys = float(input("Please enter your result in physics: "))
maths = float(input("Please enter your result in mathematics: "))
chem = float(input("Please enter your result in chemistry: "))

if phys < 50 or maths < 50 or chem < 50:
    print("One or more of your results is below 50, so you are not eligible for a scholarship.")
elif phys > 90 and mathematics > 90:
    print("Congratulations, you have been granted a scholarship.")
elif chem > 95:
    print("Congratulations, you have been granted a scholarship.")
# elif (phys > 90 and maths > 90) or chem > 95:
#     print("Congratulations, you have been granted a scholarship.")
else:
    print("Unfortunately, you have not been granted a scholarship.")

# Vowel check: 

letter = input("Enter a letter: ")

# \ can be used to split a long line when writing 
if letter == "a" or letter == "e" or \
   letter == "i" or letter == "o" or \
   letter == "u":
    print("It's a vowel.")
elif letter == "y":
    print("Sometimes it's a vowel... Sometimes it's a consonant.")
else:
    print("It's a consonant.")


