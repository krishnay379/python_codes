menu = { 
    "espresso": {
        "ingredients" :{
            "water":50,
            "coffee":18,
        },
        "cost":1.50,
    },
    "latte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee":24,
        },
        "cost":2.50,
    },
    "cappuccino":{
        "ingredients":{
            "water":250,
            "milk":100,
            "coffee":24,
        },
        "cost":3.00,
    }
}
profit = 0
resources={
    "water":300,
    "milk":200,
    "coffee":100
}

def is_sufficient(order_ingredients):
    """Return when order can be made,False if ingredient is insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry , there is not enough {item}")
            return False
    return True

def process_coins():
    """Return total calculation of coins """
    print("please insert coins.")
    total=0
    total = int(input("Enter quarters coins")) * 0.25
    total += int(input("Enter dimes coins ")) *0.10
    total += int(input("Enter nickles coins" ))* 0.05
    total += int(input("Enter pennies coins" )) * 0.01
    return total

def is_transaction_sucessful(money_recieved,drink_cost):
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost,2)
        print(f"Here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else :
        print("Sorry, that's not enough money. Money refunded ")
        return False

def make_coffee (drink_name , order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}☕☕ ")

is_on = True
while is_on:
    choice=input("What would you like ? (espresso, latte, cappuccino)")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water {resources['water']}ml")
        print(f"milk :{resources['milk']}ml")      
        print(f"coffee :{resources['coffee']}g")
        print(f"money : {profit}")    

    # elif choice == "report":
        # print(resources)
    else:
        drink = menu[choice]
        print(drink)
        if is_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_sucessful(payment, drink["cost"]):
                make_coffee(choice , drink["ingredients"])