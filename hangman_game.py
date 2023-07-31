import random
def choose_word():
    words = ["elephant", "banana", "mountain", "sunshine", "butterfly"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

print("Welcome to Hangman!\nRules of the game:\n1. You need to guess the word letter by letter.\n2. You have 9 attempts to guess the letters.")
word_to_guess = choose_word()
guessed_letters = []
attempts_left = len(word_to_guess) + 2
while attempts_left > 0:
    print("Word:", display_word(word_to_guess, guessed_letters))
    letter = input("Enter a letter: ").lower()
    if len(letter) != 1 or not letter.isalpha():
        print("Please enter a single letter.")
        continue
    if letter in guessed_letters:
        print("You already guessed this letter. Try again.")
        continue
    guessed_letters.append(letter)
    if letter in word_to_guess:
        print("Correct! Word:", display_word(word_to_guess, guessed_letters))
    else:
        attempts_left -= 1
        if attempts_left == 0:
            print("Incorrect! Game over. The word was:", word_to_guess)
        else:
            print(f"Incorrect! You have {attempts_left} attempt(s) left. Word:", display_word(word_to_guess, guessed_letters))
    if "_" not in display_word(word_to_guess, guessed_letters):
        print("Congratulations! You guessed the word:", word_to_guess)
        break