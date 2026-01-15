"""
THIS IS A STONE-PAPER-SCISSORS GAME.
THE USER HAS TO SELECT(TYPE) THEIR CHOICE BETWEEN THE THREE.
IT WILL BE COMPARED WITH THE SYSTEM'S CHOICE ACCORDING TO THE GAME'S RULES.
THE RESULT "WIN" OR "LOSS" ALONGWITH THE SCORES WILL BE DISPLAYED.
USER CAN PLAY FOR AS LONG AS THEY LIKE.

"""



import random


SCISSORS = "scissors"
STONE = "stone"
PAPER = "paper"
choices = [SCISSORS, STONE, PAPER]

"""Prompt the user for their choice and validate it."""
def get_user_choice():
    
    while True:
        user_input = input(f"Enter your choice ({SCISSORS}, {STONE}, {PAPER}): ").lower()
        if user_input in choices:
            return user_input
        print(f"'{user_input}' is an invalid choice. Please try again.")


"""Randomly select the computer's choice."""
def get_computer_choice():
    
    return random.choice(choices)


"""Decide the winner, display the result, and return the outcome."""
def evaluate_and_display_result(user, computer):
   
    if user == computer:
        print(f"Computer chose {computer} --> Tie")
        return "tie"
    elif (user == SCISSORS and computer == PAPER) or \
         (user == STONE and computer == SCISSORS) or \
         (user == PAPER and computer == STONE):
        print(f"{computer} --> You win")
        return "win"
    else:
        print(f"{computer} --> You lose")
        return "lose"


"""Controls flow of game with end result or output."""
def play_game():
    wins, loses = 0, 0

    while True:
        choice = input("Enter 0 to play, 1 to exit: ")
        if choice == "1":
            print(f"Wins: {wins}  Loses: {loses}")
            print("Thanks for playing!")
            break
        elif choice == "0":
            user_choice = get_user_choice()
            computer_choice = get_computer_choice()
            result = evaluate_and_display_result(user_choice, computer_choice)

            if result == "win":
                wins += 1
            elif result == "lose":
                loses += 1

            print(f"Score - Wins: {wins}, Loses: {loses}\n")
        else:
            print("Invalid input. Please enter 0 to play or 1 to exit.")

if __name__ == "__main__":
    play_game()
