import pandas as pd
datas = pd.read_csv("nato_phonetic_alphabet.csv")
# datas.to

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
result= {row.letter: row.code for (index,row) in datas.iterrows()}
# {"A": "Alfa", "B": "Bravo"}
# print(result)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def repet():
    word = input("enter a letter: ").upper()
    try:
       output= [result[letter] for letter in word]
    except KeyError :
        print("Sorry , only letter in alphabet plea123se")
        repet()
    else:
        print(output)

repet()