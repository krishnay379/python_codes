import random
rock='''    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''


paper='''    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissor ='''    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_image=[rock,paper,scissor]

user_choice =int(input("what do you choice ? Type 0 for rock 1 for papaer and 2 for scissor.\n"))
if user_choice >=0 and user_choice <3:
    print(game_image[user_choice])
computer_choice = random.randint(0,2)
print(game_image[computer_choice])
print(f"computer's choice {computer_choice}")
if user_choice ==0:
    if computer_choice == 0:
        print("It's draw")
    elif computer_choice==1:
        print("👎👎***********************You lose!*********************")
    else :
        print("👍👍**************************You win********************")
elif user_choice==1:
     if computer_choice == 0:
        print("You win!")
     elif computer_choice == 1:
        print("It's draw")
     else :
        print("You lose")
elif user_choice==2:
    if computer_choice ==0:
        print("You lose!")
    elif computer_choice ==1:
        print("You win")
    else :
        print("It's draw")
else:
    print("you choice worng entry , you lose")