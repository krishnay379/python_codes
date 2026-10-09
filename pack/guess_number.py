import random
print('''
                                                                                       █████                       
                                                                                      ░░███                        
  ███████ █████ ████  ██████   █████   █████     ████████   █████ ████ █████████████   ░███████   ██████  ████████ 
 ███░░███░░███ ░███  ███░░███ ███░░   ███░░     ░░███░░███ ░░███ ░███ ░░███░░███░░███  ░███░░███ ███░░███░░███░░███
░███ ░███ ░███ ░███ ░███████ ░░█████ ░░█████     ░███ ░███  ░███ ░███  ░███ ░███ ░███  ░███ ░███░███████  ░███ ░░░ 
░███ ░███ ░███ ░███ ░███░░░   ░░░░███ ░░░░███    ░███ ░███  ░███ ░███  ░███ ░███ ░███  ░███ ░███░███░░░   ░███     
░░███████ ░░████████░░██████  ██████  ██████     ████ █████ ░░████████ █████░███ █████ ████████ ░░██████  █████    
 ░░░░░███  ░░░░░░░░  ░░░░░░  ░░░░░░  ░░░░░░     ░░░░ ░░░░░   ░░░░░░░░ ░░░░░ ░░░ ░░░░░ ░░░░░░░░   ░░░░░░  ░░░░░     
 ███ ░███                                                                                                          
░░██████                                                                                                           
 ░░░░░░                                                                                                            

''')
print("Welcome to guess a number game ")
easy_level =10
hard_level=5

number =random.randint(1,100)
# print(number)

def game():
    def guess_no(guess,number,turn):  
        if guess < number :
            print("Guess number is smaller")
            return turn -1
        # checks answer against guess, returns tje number if guess remaining
        elif guess > number :
            print("Guess number is higher")
            return turn -1
        else :
            print(" You guess right number ")

    def set_difficulty():
        level= input("Choose  a difficulty. Type 'easy' or 'hard':")
        if level == "easy":
            return easy_level
        else :
            return hard_level

    turn = set_difficulty()

    guess =0
    while guess != number:
        print(f"You have {turn} attempts remaining to gues a number ")
        guess = int(input("Guess a number "))
        turn = guess_no(guess, number,turn)
        if turn == 0 :
            print("You run out of turns , You loose")
            return
        elif guess != number:
            print("guess again")

game()