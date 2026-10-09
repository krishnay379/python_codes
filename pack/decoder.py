print('''                                                                                                                                            
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba,  ,adPPYba, 8b,dPPYba,                     
a8"     "" ""     `Y8 a8P_____88 I8[    "" a8P_____88 88P'   "Y8                      
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  8PP""""""" 88                                     
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I "8b,   ,aa 88                                     
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"'  `"Ybbd8"' 88                            
''')
print('''                                                     
           88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88                                             

''')


alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def ceaser (original_text, shift_amount, encode_or_decode):
    output_text =""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original :
        if letter not in alphabets:
            output_text += letter
        else:
            shifted_positions = alphabets.index(letter) + shift_amount
            shifted_positions %= len(alphabets)
            output_text += alphabets[shifted_positions]
    print(f"Here is your decoded message :{output_text}")


should_countinue =True
while should_countinue:
    direction=input("Type encode for encryption and decode for dencryption\n").lower()
    original =input("Input your message \n").lower()
    shift = int(input("Number of places to shift\n"))

    ceaser(original_text= original,shift_amount=shift ,encode_or_decode=direction)

    restart =input("Type 'yes' if you want to do again . otherwise tyoe 'no'").lower()
    if restart =="no":
        should_countinue =False
        print("Goodbye")
