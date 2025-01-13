import random

lower_bound = 0
upper_bound = 50
max_attempts = 5

secret_number = random.randint(lower_bound, upper_bound)


def get_guess():
    while True:
        try:
            guess = int(input(f"Guess a number between {lower_bound} and {upper_bound} \n"))
            if lower_bound <= guess <= upper_bound:
                return guess
            else:
                print(" Invalid input. Please enter a number specified within the range")
        except ValueError:
            print("Please enter a valid number.")


def check_guess(guess, secret_number):
    if guess == secret_number:
        return "correct"
    elif guess < secret_number:
        return "Too Low"
    else:
        return "Too High"


def play_game():
    attempts = 0
    won = False

    while attempts < max_attempts:
        attempts += 1
        guess = get_guess()
        result = check_guess(guess, secret_number)

        if result == "correct":
            print(f" Congratulations, You guessed the secret number {secret_number} correct in {attempts} attempts.\n")
            won = True
            break
        else:
            print(f"{result}. Try again!")

    if not won:
        print(f"Sorry, you are out of attempts. The secret number is {secret_number}")


if __name__ == "__main__":
    print("Welcome to the number guessing game!")
    play_game()
