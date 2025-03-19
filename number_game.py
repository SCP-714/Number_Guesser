import random


start = input("Welcome traveler, would you like to continue to a journey of riddles?: ")
if start.lower() != "yes":
    quit()

top_of_range = input("Traveler please enter a number: ")

 

random_number = random.randint(0, top_of_range)

while True:
    user_guess = input("Make a Guess Traveler: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

    if user_guess <= 0:
        print("Please Provide A Number Greater Than 0 Next Time: ")
        quit()
    else:
        print("Please Provide A Number Next Time")
        quit()