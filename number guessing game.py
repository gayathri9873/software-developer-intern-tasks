import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)
attempts = 0

# Sample guesses (for demonstration purposes)
sample_guesses = [55, 30, 20, 45, secret_number]  # last guess is always correct

print("Welcome to the Number Guessing Game!")
print("I have chosen a number between 1 and 100. Can you guess it?\n")

for guess in sample_guesses:
    attempts += 1
    print(f"Enter your guess: {guess}")
    
    if guess < secret_number:
        print("Too low! Try again.\n")
    elif guess > secret_number:
        print("Too high! Try again.\n")
    else:
        print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.\n")
        break
