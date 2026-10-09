import random
letter= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
number =['1','2','3','4','5','6','7','8','9','0']
symbol=['!','@','#','$','%','^','&','*','(',')']
print("Welcome , to password generator")
en_letter=int(input("How many letter required in password?"))
en_number=int(input("How many nubmer is password?"))
en_symbol=int(input("How many symbols in password"))

password =" "
# easy method
for char in range (0,en_letter):
    password+= random.choice(letter)

for integer in range (0,en_number):
    password +=random.choice(number)

for char in range(0,en_symbol):
    password += random.choice(symbol)
print(password)


# hard method
password_list=[]
for char in range(0,en_letter):
    password_list.append(random.choice(letter))
for char in range(0,en_number):
    password_list.append(random.choice(number))
for char in range(0,en_symbol):
    password_list.append(random.choice(symbol))
# print(password_list)
random.shuffle(password_list)
# print(password_list)

password=""
for char in password_list:
    password += char
print(password)