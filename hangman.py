import random 
# asci art of hangman
stages = [r'''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \
     |
    _|___''',r'''
    
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
    _|___''',r'''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
    _|___
''',r'''
      _______
     |/      |
     |      (_)
     |      \|/
     |       
     |      
     |
    _|___
''',r'''
      _______
     |/      |
     |      (_)
     |      \|
     |       
     |      
     |
    _|___
''',r'''
      _______
     |/      |
     |      (_)
     |       |
     |       
     |      
     |
    _|___
''',r'''
      _______
     |/      |
     |      
     |      
     |       
     |      
     |
    _|___''']
# word list for game
words=["camel","star","dog","true","game","baloon","apple","backspace","dot","nice","back","cat"] 

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
    print(f"****************************************{lives}/6 LIVES LEFT*********************")
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
            print(f"****************************IT WAS {chosen_word}.You Lose********************")


#  if no underscore player win
    if "_" not in display:
        game_over = True
        print("**********************************You win**********************************")
    print(stages[lives])        
        