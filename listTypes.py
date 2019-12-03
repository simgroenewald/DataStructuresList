# Compulsory Task 1

# Declares an empty list where the names will be stored
friends_names = []

# Asks the user to enter three of their friends names and stores it in the list

print("Please enter 3 of your friends names.")
for i in range(0, 3):
    name = input("Friend's name: ")
    friends_names.append(name)

# This prints out the name of the first friend
print("The first friend you listed was: " + friends_names[0])

# This prints out the name of the last friend
print("The last friend you listed was: " + friends_names[2])

# This prints out the length of the list
print("The length of your list is: " + str(len(friends_names)))

# Declares an empty list where the friends ages will be stored
friends_ages = []

# This will prompt the user to enter the age of a specific friend and store it in the list
for friend in friends_names:
    age = input("Please enter the age of your friend " + friend + ": ")
    friends_ages.append(age)

