import time
import random

def greeting():
    print("Welcome to the number guessing game!")
    print("I have selected a number between 1 and 100. Can you guess it?")
    print("I hope you succeed!!")
    
def set_difficulty():
    print("choose your difficulty level:")
    print("\t1. Easy (10 attempts)")
    print("\t2. Medium (7 attempts)")
    print("\t3. Hard (3 attempts)")
    print("\tChoose 1, 2, or 3!!!")

    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            return 10
        elif choice == 2:
            return 7
        elif choice == 3:
            return 3
        else:
            print("Invalid input. Choose 1, 2 or 3.")

def get_num_to_guess():
    return random.randint(1,100)

def game_start():
    chances = set_difficulty()
    num_to_guess = get_num_to_guess()
    attempts = 0
    start_time = time.time()

    print(f"\nGreat! You have selected the difficulty level with {chances} chances.")
    print("Let's start the game!")

    while attempts < chances:
        try:
            guess = int(input("Enter a number: "))
        except ValueError:
            print("Please enter a valid number!!!")
            continue

        attempts += 1

        if guess < num_to_guess:
            print(f"The number is greater than {guess}.")
        elif guess > num_to_guess:
            print(f"The number is smaller than {guess}.")
        else:
            end_time = time.time()
            elapsed_time = end_time - start_time 
            print(f"Congratulationss!! You Guessed the correct number in {attempts} attempts./n")
            print(f"Time taken : {elapsed_time:.2f} seconds.")
            return attempts
        
    print("Sorry, You couldn't find the correct number.")
    print(f"The correct number was {num_to_guess}.")
    return attempts

def main():
    high_scores = {
        'easy': float('inf'),
        'medium': float('inf'),
        'hard': float('inf')
    }
    while True:
        greeting()
        attempts = game_start()

        if attempts < high_scores['easy']:
            high_scores['easy'] = attempts
            print(f"New high score for easy difficulty: {attempts} attempts!")
        elif attempts < high_scores['medium']:
            high_scores['medium'] = attempts
            print(f"New high score for medium difficulty: {attempts} attempts!")
        elif attempts < high_scores['hard']:
            high_scores['hard'] = attempts
            print(f"New high score for hard difficulty: {attempts} attempts!")  

        print("current high scores:")
        print(f"Easy: {high_scores['easy']} attempts")
        print(f"Medium: {high_scores['medium']} attempts")
        print(f"Hard: {high_scores['hard']} attempts")

        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()

