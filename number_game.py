import random


start = input("Welcome traveler, would you like to continue to a journey of riddles?: ")
if start.lower() != "yes":
    quit()

random_number = random.randint(0, 100)
print(random_number)