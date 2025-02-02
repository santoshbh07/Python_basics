import random
from game_data import data

score = 0

def format_data(account):
    """takes the account data and returns the printable format"""
    account_name = account["name"]
    account_descr = account["description"]
    account_handle = account["instagram_handle"]
    return f"{account_name} - {account_descr} Insta: {account_handle}"

def check_answer(user_guess, a_followers, b_followers):
    """takes the user's guess and the followers of both accounts, returns if the guess is correct"""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

account_b = random.choice(data) 

game_should_continue = True
while game_should_continue:
    #Generate a random account from the game data
    # Making account at position B become the next account at position A.
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"A: {format_data(account_a)}")
    print(f"B: {format_data(account_b)}")

    # Ask user for a guess
    guess = input("Who has more followers?: Type 'A' or 'B': ").lower()

    # Check if user is correct.
    ## - Get follower count of each account
    a_follower_count = account_a["instagram_followers"]
    b_follower_count = account_b["instagram_followers"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Give user feedback on their guess
    if is_correct:
        score += 1
        print(f"You are right! Current score: {score}\n")
    else:
        print(f"Sorry, that's wrong! Final score: {score}\n")
        game_should_continue = False
