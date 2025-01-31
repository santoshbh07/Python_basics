import random
from words import word_list

lives = 6
print(f"------------Total lives: {lives}------------")

chosen_word = random.choice(word_list)

placeholder = ""

for position in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)

game_over = False

correct_letters = []

while not game_over:
    guess = input("\nGuess a letter: ").lower()

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed letter {guess} which is not in the word. You lose a life!")
        print(f"------------Remaining lives: {lives}------------")
    
    if guess in correct_letters:
        print("You already guessed this letter, try another one!")
    
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if "_" not in display:
        game_over = True
        print("You win.")
    elif lives == 0:
        game_over = True
        print("You lost! The correct word was " + chosen_word)