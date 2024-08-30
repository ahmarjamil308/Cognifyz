import random
number_to_guess = random.randint(1, 5)

while True:
    guess = int(input("Guess the number (between 1 and 5): "))
    
    if guess < number_to_guess:
        print("Too low!")
    elif guess > number_to_guess:
        print("Too high!")
    else:
        print("Congratulations! You guessed the number.")
        break
