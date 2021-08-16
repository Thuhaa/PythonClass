"""
Write a program that awards users points according to the input the program
receives, after comparing it with a random number the program generates between 0 and 10
1. The program should award points and print the points that the users gets.
- If the user's number is within one value of the right number,

Pseudocode = Code written in a human readable way
x = right number
y = users number
x-y = 1 == 20 points
x-y = 2 == 10 points
x-y == 0; x==y User is correct User will get 1000 points
x - y > 2 == 0 points

the user gets 20 points
- If the user is within two values of the right number, the user gets 10 points
- If the user's number is the right one, the user gets 1000 points
- Use the python standard library
- Use functions


- Check if the number is correct
- Nearer = 20 abs(right_number
- Further = 10
- functions, passing arguments, if-else, datatypes, type conversion
- Functions separate code parts
"""
# Solving problems- Step by step
import random


def check_users_input_validity(users_input):
    if users_input > 10 or users_input < 0:
        print("You should enter a number between 0 and 10")
    else:
        game()


def game():
    right_number = random.randint(0,10)
    if abs(right_number - users_input) == 1:  # Bonus 10 matches
        print("You have won 20 points: The correct number is right_number", right_number)
    elif right_number == users_input:  # Jackpot!!!
        print("You have won 1000 points")
    elif abs(right_number - users_input) == 2:  # Bonus 9 Matches
        print("You have  won 10 points: The correct number is: ", right_number)
    else:  # Not close to getting the answer
        print("You have have not won any point: The correct number is: ", right_number)


users_input = int(input("Enter a number between 0 and 10: "))
check_users_input_validity(users_input)  # Call the function
