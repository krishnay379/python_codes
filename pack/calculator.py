def add (n1, n2):
    return n1 + n2

def substract(n1,n2):
    return n1-n2


def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operators ={
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print('''     _____________________
    |  _________________  |
    | | kris         0. | |
    | |_________________| |
    |  ___ ___ ___   ___  |
    | | 7 | 8 | 9 | | + | |
    | |___|___|___| |___| |
    | | 4 | 5 | 6 | | - | |
    | |___|___|___| |___| |
    | | 1 | 2 | 3 | | x | |
    | |___|___|___| |___| |
    | | . | 0 | = | | / | |
    | |___|___|___| |___| |
    |_____________________|
    ''')

    should_accunulate = True
    num1 =float(input("Enter first number"))
    while should_accunulate :
        for symbol in operators:
            print(symbol)
        operation_symbol = input("Pick an operator")

        num2 = float(input("What is second number"))
        answer = operators[operation_symbol](num1,num2)
        print(f"{num1}{operation_symbol}{num2}={answer}")

        choice = input(f"Type 'y' to countinue calculating with {answer}. Type 'n ' to restart calculator" )

        if choice == "y":
            num1=answer
        else :
            should_accunulate=False 
            print("\n" *20)
            calculator()

calculator()