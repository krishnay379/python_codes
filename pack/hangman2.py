import random 
import hangman_words
from hangman_words import word_list
from hangman_arts import stages , logo

# numbers of lives
lives = 6

# chose random word from list
chosen_word=random.choice(words)
# print(chosen_word)

# To make space bar for word
placeholder =""
word_length = len(chosen_word)
for letter in range(word_length):
    placeholder +="-"
print(placeholder)

# game state variable
game_over= False
correct_letter = [] # store correct guseed letter 

# loop for game 
while not game_over:
    # Take input from user 
    guess =input("Guess a letter. ").lower()


    display =""
    for letter in chosen_word:
        if letter == guess: # if gussed letter match 
            display += letter
            correct_letter.append(guess)

        elif letter in correct_letter:
            display += letter
        else:
            display +="_"
    print(display)

# if wrong guess , reduces lives
    if guess not in chosen_word:
        lives -=1
        if lives == 0:
            game_over = True
            print("*********************************You Lose*******************************************")


#  if no underscore player win
    if "_" not in display:
        game_over = True
        print("*************************************You win******************************************")
    print(stages[lives])