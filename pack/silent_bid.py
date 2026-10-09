print('''                                                                                  
          88 88                                        88          88          88  
          "" 88                         ,d             88          ""          88  
             88                         88             88                      88  
,adPPYba, 88 88  ,adPPYba, 8b,dPPYba, MM88MMM          88,dPPYba,  88  ,adPPYb,88  
I8[    "" 88 88 a8P_____88 88P'   `"8a  88             88P'    "8a 88 a8"    `Y88  
 `"Y8ba,  88 88 8PP""""""" 88       88  88             88       d8 88 8b       88  
aa    ]8I 88 88 "8b,   ,aa 88       88  88,            88b,   ,a8" 88 "8a,   ,d88  
`"YbbdP"' 88 88  `"Ybbd8"' 88       88  "Y888          8Y"Ybbd8"'  88  `"8bbdP"Y8  
'''  )

# ask user for input

def find_highest_bid(bidding_dictionary):
    winner =""
    highest_bid =0

    max(bidding_dictionary)
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid :
            highest_bid = bid_amount
            winner = bidder
    print(f"The highest bidder is {winner} and highest bid is{highest_bid}")

# Turn into dictionary
bid = {}
countinue_bidding =True
while countinue_bidding:
    name = input("What is your name ? \n")
    bid[name] = int(input("What is your bid ? $"))
    should_countinue = input("Are there more bids ?. Type 'yes' or 'no' \n").lower()
    if should_countinue =="no":
        countinue_bidding =False
        find_highest_bid(bid)
    elif should_countinue == "yes":
        print("\n"*50)
    



