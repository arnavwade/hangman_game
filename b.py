import random

print("Welcome to the Hangman game!")

words = ["harddrive", "desktop", "computer", "mouse", "keyboard", "monitor"]
word = random.choice(words)
guessed_word = ["_"] * len(word)
attempts = 5
guessed_letters = []

print("Guess one letter at a time!")
print("You have only 5 attempts.")

while attempts > 0 and "_" in guessed_word:

    print("\nWord:", "".join(guessed_word))
    print("Attempts remaining for you:", attempts)

    guess = input("Guess your letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter!")
        continue

    if guess in guessed_letters:
        print("You have already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")

        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess

    else:
        attempts = attempts - 1
        print("Wrong guess! Try again.")

if "_" not in guessed_word:
    print("Congratulations, you won!!")
    print("The word was:", word)

else:
    print("Game Over!!")
    print("The correct word was:", word)

print("Thank you for playing Hangman Game!")
