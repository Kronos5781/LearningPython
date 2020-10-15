import random

#Random Number Gen
def get_random_number(start, range):
    number = random.randint(start, range)
    return number

#Get user input
guessed_number = input("Enter a Number between 0 and 10:")

#Gen Random Number and lookup if the ser guessed correctly
rand_number = get_random_number(0, 10)
if guessed_number == rand_number:
    print("GJ")
elif int(guessed_number) < rand_number:
    print("to low!")
elif int(guessed_number) > rand_number:
    print("to high!")