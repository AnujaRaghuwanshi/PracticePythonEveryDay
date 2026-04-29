# Hangman

import random
from hangman_words import word_list
from hangman_art import stages, logo
print(logo)
chosen_word = random.choice(word_list)

print(chosen_word)


placeholder =""

for pos in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)

correct_letters = []
game_is_over = False
lives = 6

while not game_is_over:
    print(" number of lives: ", lives)
    guess = input("Guess a letter: ").lower()
    display = ""
    if guess in correct_letters:
        print("you guessed the letter ", guess)
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display  += "_"
    print(display)


    if guess not in chosen_word:
        lives -= 1
        print("you have guessed the letter which is not in the word ", guess)
        if lives == 0:
            game_is_over = True
            print("You Lose!")
            print("the word is ", chosen_word)

    if "_" not in display:
        game_is_over = True
        print("you win")

    print(stages[lives])






















#
# import hangman_art as art
# import hangman_words as words
# import random
#
#
# def get_guess():
#     while True:
#         g = input("Guess a letter: ").lower()
#         # repeated guesses of the same letter should not count as a "bad" guess
#         if g in guessed_letter_list:
#             print(f"You have already guessed the letter \"{g}\".")
#         # make sure the guess is a single character
#         elif g not in letter_list:
#             print("The guess has to be a single letter. Please try again.")
#         else:
#             # "return" will also break out the infinite loop, just like "break"
#             return g
#
#
# # typing a whole list of all letters manually is tedious, so just making one from a simple string
# letter_list = list("abcdefghijklmnopqrstuvwxyz")
# # to store letters that have already been guessed
# guessed_letter_list = []
#
# # randomly pick a word, then save it as a list of characters
# chosen_word = list(random.choice(words.word_list))
# # the display list, fill it with "_" for each character
# display = []
# for i in range(len(chosen_word)):
#     display.append("_")
#
# # set conditions to break out of main loop
# game_over = False
# is_winner = False
# # the number of lives at the beginning actually depends on the number of elements in the "stages" list
# # better to avoid hard-coding it to "6" though
# lives = len(art.stages) - 1
#
# print(art.logo)
# print(f"Pssst, the solution is \"{''.join(chosen_word)}\".")
#
# while not game_over:
#     # get the input, using a function to make the code more readable
#     guess = get_guess()
#
#     # add the letter to the "guessed" list
#     guessed_letter_list.append(guess)
#
#     # evaluate the guess, and update the display list if needed
#     good_guess = False
#     for i in range(len(chosen_word)):
#         if chosen_word[i] == guess:
#             display[i] = guess
#             # set to True if there was at least one match
#             good_guess = True
#
#     if good_guess:
#         # check for win condition
#         # count the "_" in the display list, none means all characters have been guessed already
#         if display.count("_") == 0:
#             is_winner = True
#             game_over = True
#     else:
#         print(f"The letter \"{guess}\" is not in the word. You lose a life.")
#         lives -= 1
#         # check for game over condition
#         if lives == 0:
#             game_over = True
#
#     # print the display list as a string and the corresponding "art"
#     print(" ".join(display))
#     print(art.stages[lives])
#
# # after game over, print the final result
# if is_winner:
#     print("You win!")
# else:
#     print("Game over.")
