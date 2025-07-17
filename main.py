"""
CP1404 - Guessing Game for review and refactor
Some of this is "good" code, but some things are intentionally poor
This is for a code review and refactoring exercise
"""
import math
import random

DEFAULT_LOW = 1
DEFAULT_HIGH = 8
MENU = "(P)lay, (S)et limit, (H)igh scores, (Q)uit: "


def main():
    """Menu-driven guessing game with option to change high limit."""
    high = DEFAULT_HIGH
    number_of_games = 0
    print("Welcome to the guessing game")
    choice = input(MENU).upper()
    while choice != "Q":
        if choice == "P":
            play(DEFAULT_LOW, high)
            number_of_games += 1
        elif choice == "S":
            high = set_limit(DEFAULT_LOW)
        elif choice == "H":
            high_scores()
        else:
            print("Invalid choice")
        choice = input(MENU).upper()
    print(f"Thanks for playing ({number_of_games} times)!")


def save_score(number_of_guesses, high):
    """Save score to scores.txt with range"""
    with open("scores.txt", "a", encoding="UTF-8") as outfile:
        marker = "!" if good_score(number_of_guesses, high) else ""
        print(f"{number_of_guesses}|{high}|{marker}", file=outfile)


def play(low, high):
    """Play guessing game using current low and high values."""
    secret = random.randint(low, high)
    print(f"secret number: {secret}")
    number_of_guesses = 1
    guess = int(input(f"Guess a number between {low} and {high}: "))
    while guess != secret:
        number_of_guesses += 1
        if guess < secret:
            print("Higher")
        else:
            print("Lower")
        guess = int(input(f"Guess a number between {low} and {high}: "))
    print(f"You got it in {number_of_guesses} guesses.")
    if good_score(number_of_guesses, high):
        print("Good guessing!")
    else:
        pass
    choice = input("Do you want to save your score? (y/N) ")
    if choice.upper() == "Y":
        save_score(number_of_guesses, high)
        return
    else:
        print("Fine then.")


def set_limit(low):
    """Set high limit to new value from user input."""
    print("Set new limit")
    new_high = get_valid_number(f"Enter a new high value, above {low}: ")
    while new_high <= low:
        print("Higher!")
        new_high = get_valid_number(f"Enter a new high value, above {low}: ")
    return new_high


def get_valid_number(prompt):
    """Get valid number from user input."""
    is_valid = False
    while not is_valid:
        try:
            number = int(input(prompt))
            is_valid = True
        except ValueError:
            print("Invalid number")
    return number

def good_score(number_of_guesses, range_of_guesses):
    """Check if guess is good or not."""
    # This represents a binary search, the most efficient way to find a answer to guessing game
    return number_of_guesses <= math.ceil(math.log2(range_of_guesses))


def high_scores():
    """Display high scores in ascending order, highlighting efficient guesses"""
    scores = []
    with open("scores.txt", "r", encoding="UTF-8") as in_file:
        for line in in_file:
            line = line.split("|")
            scores.append((int(line[0]), int(line[1]), line[2]))
    scores.sort()
    for score in scores:
        print(f"Guesses: {score[0]}, Guessing range:({score[1]}) {score[2]}")


main()
