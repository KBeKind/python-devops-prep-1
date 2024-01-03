# user_input = float(input(""))

# divided = user_input / 3

# print(divided)

# Write a program that reads in a number and prints the either Small, Medium or Large depending on if the number is bellow 100 or above 200.

#     For example, if the user enters 150 the program should display “Medium”

#     Another example, is if the user enters 50 the program should display “Small”


# user_input = int(input(""))

# if user_input < 100:
#     print("Small")
# elif user_input <= 200:
#     print("Medium")
# else:
#     print("Large")


# Write a program that reads in a number and prints the sum of all values from 1 up to the number.

#     For example, if the user enters 5 the program should display 15.  15 is (1+2+3+4+5)

# user_input = int(input(""))

# sum = 0

# for num in range(1, user_input + 1):
#     sum += num

# print(sum)


# Write a program that reads in numbers until a -1 is entered and prints the sum of all numbers entered.
#     For example, if the user enters 5 10 15 -1 the program should 
#     display 30 (Each number will be separated by a carriage return).  30 is (5+10+15)


sum = 0
num = int(input(""))

while num != -1:
    sum += num
    num = int(input(""))

print(sum)