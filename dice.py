import random

def roll_dice():
    return random.randint(1, 6)

def play_dice_roller():
    print("Welcome to the Dice Rolling Simulator!")
    play_again = True

    while play_again:
        input("Press Enter to roll the dice...")
        ai_result = roll_dice()
        result = roll_dice()
        print("I rolled a", ai_result)
        print("You rolled a", result)
        if result<ai_result:
            print("You Lose!")
        elif result>ai_result:
            print("You Win!")
        else:
            print("It's a Draw!")

        play_again_input = input("Do you want to roll again? (y/n): ")
        play_again = play_again_input.lower() == 'y'

    print("Thank you for playing the Dice Rolling Simulator!")

def play_number_guessing_game():
    target_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        guess = int(input("Take a guess: "))
        attempts += 1

        if guess < target_number:
            print("Too low! Try again.")
        elif guess > target_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the number in", attempts, "attempts.")
            break

        if attempts == 5:
            print("Oops! You've reached the maximum number of attempts.")
            print("The number I was thinking of was:", target_number)
            break

    print("Thank you for playing the Number Guessing Game!")
def play_word_guessing_game():
    words = ['apple', 'banana', 'orange', 'grape', 'melon']
    target_word = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("Welcome to the Word Guessing Game!")
    print("I'm thinking of a word. It consists of", len(target_word), "letters.")

    while attempts > 0:
        display_word = ''
        for letter in target_word:
            if letter in guessed_letters:
                display_word += letter + ' '
            else:
                display_word += '_ '

        print("Word:", display_word)
        print("Attempts remaining:", attempts)

        if '_' not in display_word:
            print("Congratulations! You guessed the word correctly.")
            break

        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("You have already guessed that letter. Try again.")
        elif guess in target_word:
            print("Good guess!")
            guessed_letters.append(guess)
        else:
            print("Wrong guess!")
            attempts -= 1

    if attempts == 0:
        print("Oops! You've run out of attempts.")
        print("The word I was thinking of was:", target_word)

    print("Thank you for playing the Word Guessing Game!")

def main():
    print("Welcome to the Game Selector!")
    print("Please choose a game to play:")
    print("1. Dice Rolling Simulator")
    print("2. Number Guessing Game")
    print("3. Word Guessing Game")
    print("4. Quit")

    while True:
        choice = input("Enter your choice (1-3, 4 to exit): ")

        if choice == '1':
            play_dice_roller()
        elif choice == '2':
            play_number_guessing_game()
        elif choice == '3':
            play_word_guessing_game()
        elif choice == '4':
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()