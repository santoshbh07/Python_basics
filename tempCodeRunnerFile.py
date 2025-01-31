import random

def black_jack():
    print("Welcome to Black Jack!")

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 10, 10, 10]

    random_card1 = random.choice(cards)
    random_card2 = random.choice(cards)
    random_card3 = random.choice(cards)
    random_card4 = random.choice(cards)

    user_cards = []
    user_cards.append(random_card1)
    user_cards.append(random_card2)

    computer_cards = []
    computer_cards.append(random_card3)
    computer_cards.append(random_card4)

    user_cards_sum = sum(user_cards)
    computer_cards_sum = sum(computer_cards)

    print(f"Your cards: {user_cards}, value: {user_cards_sum}")
    print(f"Computer's first card: {computer_cards[0]}")

    def win_logic():
        if user_cards_sum>21:
            print("You went over 21, you lose!")
        elif computer_cards_sum>21:
            print("Computer went over 21, you win!")
        elif user_cards_sum<=21 and user_cards_sum>computer_cards_sum:
            print("You win!")
        elif computer_cards_sum>=17 and computer_cards_sum>user_cards_sum:
            print("Computer wins!")
        elif user_cards_sum == computer_cards_sum:
            print("It's a draw!")

    want_to_pick_a_card = input("Do you want to pick one more card? (y/n): ")

    if want_to_pick_a_card == "y":
        random_card = random.choice(cards)
        user_cards.append(random_card)
        user_cards_sum = sum(user_cards)
        print(f"Your cards: {user_cards}, value: {user_cards_sum}")

        while computer_cards_sum < 17:
            random_card = random.choice(cards)
            computer_cards.append(random_card)
            computer_cards_sum = sum(computer_cards)
        print(f"Computer's card: {computer_cards}, value: {computer_cards_sum}")

        win_logic()

    elif want_to_pick_a_card == "n":
        while computer_cards_sum < 17:
            random_card = random.choice(cards)
            computer_cards.append(random_card)
            computer_cards_sum = sum(computer_cards)
        win_logic()

black_jack()
play_again = input("Do you want to play again? (y/n): ")

if play_again == "y":
    print("\n" * 100)
    black_jack()
elif play_again == "n":
    print("Thanks for playing!")