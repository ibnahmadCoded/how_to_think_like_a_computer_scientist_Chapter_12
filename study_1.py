user_input = input('Type a number:')
try:
    #Try to do something that could fail.
    user_input_as_number = float(user_input)
except ValueError:
    #This will be executed if a ValueError is raised
    print('You did not enter a number.')
else:
    #This will be executed if no exception got raised in the Try statement
    print('The square of your number is ', user_input_as_number ** 2)
finally:
    #THis will be executed whether or not an exception is raised.
    print("Thank you")
