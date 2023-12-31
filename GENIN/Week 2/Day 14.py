data =[
    {
        'name': 'Instagram',
        'follower_count': 254,
        'description': 'Social media platform',
        'country': 'United States of America'
    },
    {
        'name': 'Ajanlekoko Owonikoko',
        'follower_count': 142,
        'description': 'Ethical Hacker',
        'country': 'Russia'
    },
    {
        'name': 'Alejandro Sebastian',
        'follower_count': 432,
        'description': 'Musician and Director',
        'country': 'Mexico'
    },
    {
        'name': 'Josheph Adeshina',
        'follower_count': 185,
        'description': 'Robotics Engineer',
        'country': 'Canada'
    },
    {
        'name': 'Femi Falana',
        'follower_count': 1520,
        'description': 'Lawyer',
        'country': 'Nigeria'
    },
    {
        'name': 'Solomon Grundy',
        'follower_count': 331,
        'description': 'Skit maker',
        'country': 'DR Congo'
    }
]
    #Displaying Art
import random
def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return(f"{account_name}, a {account_descr}, from {account_country}")
def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
score = 0
game_should_continue = True
account_b = random.choice(data)
while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
         account_b = random.choice(data)
    print(f"Compare A: {format_data(account_a)}")
    print(f"Against B: {format_data(account_b)}")
    guess = input("Who has more followers? Type 'A' or 'B':\n").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    if is_correct:
        score += 1
        print(f"You're right! Your current Score is: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final Score is {score}")    

