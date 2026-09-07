import random

secret_number = random.randint(1, 10)
attempts = 0

while True:
    guess = int(input("Guess a number between 1 and 10: "))
    attempts += 1
    
    if guess == secret_number:
        print(f"Correct! It took you {attempts} attempts.")
        break  
    else:
        print("Wrong guess, try again!")
