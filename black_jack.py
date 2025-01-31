import random

def adjust_for_ace(cards):
    """If the total is over 21 and there is an Ace (11) in the hand, change one Ace to 1."""
    total = sum(cards)
    while total > 21 and 11 in cards:
        # Replace only one occurrence of 11 with 1 at a time
        ace_index = cards.index(11) 
        cards[ace_index] = 1 
        total = sum(cards)
    return cards

def dealer_draw(dealer_cards, deck):
    """Dealer draws cards until the hand's total is at least 17.
    Ace handling is applied after each draw."""
    dealer_cards = adjust_for_ace(dealer_cards)
    while sum(dealer_cards) < 17:
        dealer_cards.append(random.choice(deck))
        dealer_cards = adjust_for_ace(dealer_cards)
    return dealer_cards

def win_logic(user_cards, computer_cards):
    user_total = sum(user_cards)
    comp_total = sum(computer_cards)
    if user_total > 21:
        print("You went over 21, you lose!")
    elif comp_total > 21:
        print("Computer went over 21, you win!")
    elif user_total > comp_total:
        print("You win!")
    elif comp_total > user_total:
        print("Computer wins!")
    else:
        print("It's a draw!")

def black_jack():
    print("Welcome to Black Jack!")

    # The deck includes an Ace (11) and other cards; note: missing a 9 in the original list.
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

    # Deal two cards each for the user and the computer
    user_cards = [random.choice(deck), random.choice(deck)]
    computer_cards = [random.choice(deck), random.choice(deck)]

    # Adjust for aces in initial hands if needed
    user_cards = adjust_for_ace(user_cards)
    computer_cards = adjust_for_ace(computer_cards)

    user_total = sum(user_cards)
    computer_total = sum(computer_cards)

    print(f"Your cards: {user_cards}, value: {user_total}")
    print(f"Computer's first card: {computer_cards[0]}")

    # Player's decision to pick another card
    want_to_pick_a_card = input("Do you want to pick one more card? (y/n): ").lower()

    if want_to_pick_a_card == "y":
        user_cards.append(random.choice(deck))
        user_cards = adjust_for_ace(user_cards)
        user_total = sum(user_cards)
        print(f"Your cards: {user_cards}, value: {user_total}")

    # Dealer's turn: draw until reaching at least 17.
    computer_cards = dealer_draw(computer_cards, deck)
    computer_total = sum(computer_cards)
    print(f"Computer's cards: {computer_cards}, value: {computer_total}")

    win_logic(user_cards, computer_cards)

# Main game loop for replayability.
while True:
    black_jack()
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != "y":
        print("Thanks for playing!")
        break