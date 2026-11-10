
import random

words = ["PYTHON", "COMPUTER", "PROGRAM", "DATABASE",
         "INTERNET", "STUDENT"]

word = random.choice(words)
guessed = set()
wrong = 0
max_attempts = 6

stages = [
    """
     +---+
     |   |
         |
         |
         |
    =======
    """,
    """
     +---+
     |   |
     O   |
         |
         |
    =======
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
    =======
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
    =======
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
    =======
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
    =======
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
    =======
    """
]

print("WELCOME TO HANGMAN GAME!")

while wrong < max_attempts:
    print(stages[wrong])

    display = " ".join(
        letter if letter in guessed else "_"
        for letter in word
    )

    print("Word:", display)
    print("Wrong attempts:", wrong, "/", max_attempts)

    if all(letter in guessed for letter in word):
        break

    guess = input("Guess a letter: ").strip().upper()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one valid letter.")
        continue

    if guess in guessed:
        print("You already guessed this letter.")
        continue

    guessed.add(guess)

    if guess in word:
        print("Correct guess!")
    else:
        wrong += 1
        print("Wrong guess!")

if all(letter in guessed for letter in word):
    print("\nCongratulations! You won!")
    print("The word was:", word)
else:
    print(stages[wrong])
    print("\nGame Over! You lost.")
    print("The correct word was:", word)
