# Compulsory Task 3

# This is an empty list that will contain all the names
incorrect_names = []

# This allows the user to enter a name and will continuously run in a loop until John is entered
while 1:
    name = input("Please enter your name: ")
    # This code will run if the name entered is not John
    if name != "John":
        incorrect_names.append(name)
    # This code will run if the name entered is John
    if name == "John":
        print("Incorrect names: " + str(incorrect_names))
        break

