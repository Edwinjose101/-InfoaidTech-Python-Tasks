import random

def welcome():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")
    print()

def get_player_name():
    return input("What's your name? ")

def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    while attempts < 10:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess == secret_number:
            print(f"Congratulations, {player_name}! You guessed the correct number in {attempts} attempts.")
            return True
        elif guess < secret_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

    print(f"Sorry, {player_name}. You've run out of attempts. The correct number was {secret_number}.")
    return False

def play_again():
    return input("Do you want to play again? (yes/no): ").lower() == 'yes'

# Main game loop
while True:
    welcome()
    player_name = get_player_name()
    
    if play_game():
        if not play_again():
            print("Thanks for playing. Goodbye!")
            break
    else:
        if not play_again():
            print("Thanks for playing. Goodbye!")
            break

