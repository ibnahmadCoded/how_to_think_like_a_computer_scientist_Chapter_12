filename = input("Enter a file name: ")
try:
    f = open(filename, "r")
except FileNotFoundError:
    print("There is no file named", filename)
