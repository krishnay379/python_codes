import random
logo = r"""
 _     _       _                 _                        
| |__ (_) __ _| |__   ___ _ __  | | _____      _____ _ __ 
| '_ \| |/ _` | '_ \ / _ \ '__| | |/ _ \ \ /\ / / _ \ '__|
| | | | | (_| | | | |  __/ |    | | (_) \ V  V /  __/ |   
|_| |_|_|\__, |_| |_|\___|_|    |_|\___/ \_/\_/ \___|_|   
         |___/                                            
"""
vs = r"""           
__   _____ 
\ \ / / __|
 \ V /\__ \
  \_/ |___/
"""
print(logo)

data = [
    {
        'name':'Breaking Bad',
        'year':'2008-2013',
        'genre':'Crime, Drama, Thriller',
        'rating':9.5
    },
    {
        'name':'Band of Brothers',
        'year':'2001',
        'genre':'Drama, History, War',
        'rating':9.4
    },
    {
        'name':'The Wire',
        'year':'2002-2008',
        'genre':'Crime, Drama, Thriller',
        'rating':9.3
    },
    {
        'name':'Game of Thrones',
        'year':'2011-2019',
        'genre':'Action, Adventure, Drama',
        'rating':9.2
    },
    {
        'name':'The Sopranos',
        'year':'1999-2007',
        'genre':'Crime, Drama',
        'rating':9.19
    },
    {
        'name':'The Twilight Zone',
        'year':'1959-1964',
        'genre':'Drama, Fantasy, Horror',
        'rating':9.1
    },
    {
        'name':'Better Call Saul',
        'year':'2015-2022',
        'genre':'Crime, Drama',
        'rating':8.9
    },
    {
        'name':'True Detective',
        'year':'2014-Present',
        'genre':'Crime, Drama, Mystery',
        'rating':8.89
    },
    {
        'name':'Friends',
        'year':'1994-2004',
        'genre':'Comedy, Romance',
        'rating':8.88
    },
    {
        'name':'Fargo',
        'year':'2014-2023',
        'genre':'Crime, Drama, Thriller',
        'rating':8.87
    },
    {
        'name':'Seinfeld',
        'year':'1989-1998',
        'genre':'Comedy',
        'rating':8.86
    },
    {
        'name':'Peaky Blinders',
        'year':'2013-2022',
        'genre':'Crime, Drama',
        'rating':8.8
    },
    {
        'name':'Fawlty Towers',
        'year':'1975-1979',
        'genre':'Comedy',
        'rating':8.79
    },
    {
        'name':'The Marvelous Mrs. Maisel',
        'year':'2017-2023',
        'genre':'Comedy, Drama',
        'rating':8.7
    },
    {
        'name':'House',
        'year':'2004-2012',
        'genre':'Drama, Mystery',
        'rating':8.69
    },
    {
        'name':'House of Cards',
        'year':'2013-2018',
        'genre':'Drama',
        'rating':8.68
    },
    {
        'name':'Rome',
        'year':'2005-2007',
        'genre':'Action, Drama, Romance',
        'rating':8.67
    },
    {
        'name':'Gomorrah',
        'year':'2014-2021',
        'genre':'Crime, Drama, Thriller',
        'rating':8.66
    },
    {
        'name':'Sons of Anarchy',
        'year':'2008-2014',
        'genre':'Crime, Drama, Thriller',
        'rating':8.6
    },
    {
        'name':'Boardwalk Empire',
        'year':'2010-2014',
        'genre':'Crime, Drama',
        'rating':8.59
    },
]
def form_data(account):
    account_name = account["name"]
    account_year = account["year"]
    account_genre = account["genre"]
    return f"{account_name} ,a {account_genre} from {account_year}"
def check_answer(user_guess, account_a,account_b):
    if a_ratings > b_ratings:
        return user_guess == "a"
    else :
        return user_guess == "b"


score =0
game_countinue = True
account_b =random.choice(data)

while game_countinue:
    account_a = account_b
    account_b =random.choice(data)
    if account_a == account_b :
        account_b = random.choice(data)


    print(f"compare A: {form_data(account_a)}")
    print(vs)
    print(f"Agianst B: {form_data(account_b)}")

    # user guess
    guess = input("Which has high ratings ? Type 'A' or 'B' " ).lower()

    # clear screen 
    print("\n"*20)
    print(logo)
    a_ratings = account_a["rating"]
    b_ratings = account_b["rating"]

    is_correct = check_answer(guess,a_ratings,b_ratings)

    # Give user feedback on their guess
    if is_correct:
        score += 1
        print(f"You are right. current score: {score}")
    else :
        print(f"Sorry You are wrong . Final score{score}")
        game_countinue = False