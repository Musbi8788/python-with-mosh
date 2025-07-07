# print("musbi")
# print("o-------")
# print(" |||||||")
# print("*" * 20)
# print("m" * 9)

# variable
# price = 10
# rating = 4.5
# name = "Musbi"
# is_published = False
# print(price)

# full_name = 'John Smith'
# age = 20
# is_new_patient = True

# input
# name =input("what is your name? ")
# print("Hi " + name)

# name = input("what's your name? ")
# favourite_color = input("what's your favourite color? ")
# print(name + " like " + favourite_color)

# check the age
# brith_year = input("Birth year: ")
# print(type(brith_year))
# age = 2024 - int(brith_year)
# print(type(age))
# print(age)

# weight_lbs = input("Weight(lbs): ")
# weight_kg = float(weight_lbs) * 0.45
# print(weight_kg)

# course = "Python's course for Beginners"
# anther = course[:]
# print(anther)

# name = "jennifer"
# print(name[1:-1])
#
# # formatted string
# first = "Musbi"
# last = "Jawo"
# message = first + " [" + last + "] is a coder "
# msg = f"{first} [{last}] is a coder"
# print(msg)

# string methods
# course = "Python for Beginners"
# print(len(course))
# print(course.upper())
# print(course)
# find the position
# print(course.find("Beginners"))

# print(course.replace("Beginners", "Absolute Beginners"))
# check if python is in the course
# print("Python " in course)

# Arithmetic Operations
# print( 10 * 3)
#
# x = 10
# x = x + 3
# x += 3
# print(x)

# x = 10 + 3 * 2 ** 2
# print(x)

# x = (2+3) * 10 - 3
# print(x)

# math function
# import math
# x = 2.9
# it return the n num to p
# print(abs(-2.9))
# print(math.ceil(x))

# if statements
# is_hot = False
# is_cold = False
#
# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("It's a cold day")
#     print("Wear warm clothes")
# else:
#     print("It's a lovely day")
# print("Enjoy your day")

# price = 1000000
# has_good_credit = True
#
# if has_good_credit :
#     down_payments = 0.1 * price
# else:
#     down_payments = 0.2 * price
#
# print(f"Down payment: ${down_payments}")

#logical operators
# has_high_income = True
# has_good_credit= True
# has_criminal_record = True
#
# if has_good_credit and not has_criminal_record:
#     print("Eligible for loan")

#comparison operators
# temperature = 35
#
# if temperature > 30 :
#     print("It's a hot day")
# else:
#     print("It's a not a hot day")

# user = "Musbi"
# if len(user) < 3:
#     print("name must be at least 3 characters")
# elif len(user) > 50 :
#     print("name can be a maximum of 50 characters")
# else:
#     print("name looks good")

#project weight converter

# weight = int(input("Weight: "))
# check = input("(L)bs or (K)g: ").lower()
#
# if check == "l":
#     con = weight * 0.45
#     print(f"You are {con} Kilos")
#
# elif check == "k":
#     con = weight / 0.45
#     print(f"You are {con} pounds")


# while loop

# i = 1
# while i <= 50:
#     print("*" * i)
#     i += 1
# print("Done")

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break
else:
    print("Sorry, you failed.")