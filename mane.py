import random
playing = True
number = random.randint(0,10)
print("Welcome to the Number Guessing Game")
print("I am thing of a number between 0 and 10.")
print("You have 3 attempts to guess the number.")
while playing:
    attempts = 3
    while attempts >0:
        guess=input("Make a guess:")
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue
        guess=int(guess)
        if guess < 0 or guess > 10:
            print("Please enter a number between 0 and 10.")
            continue
        if guess ==number:
            print(f"You got it! the answer was {number}.")
            break
        else:
            attempts-= 1
            if attempts > 0:
                print(f"Wrong guess. you have {attempts} attempts left.")
            else:
                print(f"You have  run out of attempts. The number was {number}.")
                break