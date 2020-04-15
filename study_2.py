def get_age():
    age = int(input("Please enter your age: "))
    if age < 0:
        #Create a new instance of an exception
        #my_error = ValueError("{0} is not a valid age".format(age))
        raise ValueError("{0} is not a valid age".format(age))
    return age
