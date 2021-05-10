import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = word_list[random.randint(0, len(word_list) - 1)]

guess = input("Guess a letter: ").lower()

for ch in chosen_word:
    if ch == guess:
        print("Yes the letter is in the word!")