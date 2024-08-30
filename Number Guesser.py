import random

lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the upper bound: "))

number_to_guess = random.randint(lower_bound, upper_bound)

while True:
    guess = int(input("Guess the number: "))
    
    if guess < number_to_guess:
        print("Too low!")
    elif guess > number_to_guess:
        print("Too high!")
    else:
        print("Congratulations! You guessed the number.")
        break
