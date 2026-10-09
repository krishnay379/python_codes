print('''
      *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print("Welcome to tresure land \nYour mission is to find tresure")
choice1 = input('Do you want to enter a cave ? type "yes " or "no"').lower()
if choice1 == "yes":
    choice2 = input('You\'re at a crossroad where do you want to go? type "left" or "right"').lower()
    if choice2 == "left":
        choice3 = input('Yov\'ve cam to a lake .Island is in middle of lake .\nDo you want to wait for boat or swim? type "swim " or "wait" ').lower()
        if choice3 == "wait":
            choice4 = input(' You\'ve came to island unarmed .\n There are three doors in house . one red one blue and one green ./n which colour you choice ?').lower()
            if choice4 == "red":
                print(" You have came to room of fire . Game over")
            elif choice4 == "blue":
                print(" You have came to tresure room. you win")
            elif choice4 == "green":
                print("You have came to room full of monsters . game over")
            else: 
                print(" You have choice a door that not exist . game over")
    else :
        print("You have fell into trap . \ngame over")
else :
    print("Game over")
