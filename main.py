import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

print(f'Pssst, the solution is {chosen_word}.')

display = []
for ch in chosen_word:
    display.append("_")

guess = input("Guess a letter: ").lower()

i = 0
for ch in chosen_word:
    if ch == guess:
        display[i] = guess
    i += 1

print(display)