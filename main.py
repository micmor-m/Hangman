import random
from hangman_words import word_list
from hangman_art import stages, logo

end_of_game = False
# word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
lives = 6
print(logo)
# print(f'The solution is {chosen_word}.')

display = []
for ch in chosen_word:
    display.append("_")

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print("You already guessed it.")

    i = 0
    for ch in chosen_word:
        if ch == guess:
            display[i] = guess
        i += 1
    if guess not in chosen_word:
        print(f"{guess} is not in the word")
        print(stages[lives])
        lives -= 1

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if lives < 0:
        end_of_game = True
        print("You lose.")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
