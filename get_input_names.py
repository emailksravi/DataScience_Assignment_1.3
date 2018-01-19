"""
Problem Statement :
Write a Python program to accept the user's first and last name and then getting them
printed in the the reverse order with a space between first name and last name.
"""
import re

# Get Name Function - Generic
def get_String_Input(prompt_message):
    input_string = input(prompt_message)
    return input_string


# Validate to allow only string and spaces. No other characters allowed in First,last Names
def validate_string(input_string):
    return bool(re.search("^[a-zA-Z ]+$", input_string))


# Function to loop input until correct string provided
def loop_until_input(prompt_message):
  while True:
    userInput = get_String_Input(prompt_message).strip()
    
    if validate_string(userInput):
        return userInput
        break
    else:
        continue

# Get Name details into variables
first_name = loop_until_input("Enter First Name ")
last_name = loop_until_input("Enter Last Name ")

# print lastname firstname 
print ("print lastname firstname : ", last_name , first_name)

# print lastname firstname - strings reversed
print ("print lastname firstname - strings reversed : ", last_name[::-1] , first_name[::-1])
