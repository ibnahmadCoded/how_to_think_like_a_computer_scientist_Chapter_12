def readposint():
    user_input = input("Please enter a positive integer: ")
    try:
        posint = int(user_input)
        if posint < 0:
            #Create a new instance of an exception
            my_error = ValueError("{0} is not a positive integer".format(posint))
            raise my_error
    except ValueError:
        print("{0} is not a positive integer".format(user_input))
    else:
        print("Your integer is ", user_input)
    finally:
        print("Thank you")
    
