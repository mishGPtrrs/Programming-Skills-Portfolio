# password

#define the password
password = "12345"

#initialize the user's input
user_input = ""

#use while loop to ask the user for the password until correct
while user_input != password:
    user_input = input("enter password: ")

    if user_input == password:
        print("access granted :D")
    else:
        print("incorrect password, please try again.")