# Write a terminal game that allows the user to play a game of rock, paper, scissors
# against the computer. The game should be interactive and allow the user to input
# their choice and see the result of the game. In each round, the user should enter 
# one of ("rock", "paper", "scissors"). The user should be warned if they enter an invalid
# option. The computer should internally randomly select one of these as well 
# and play out the round. After each round, the user should be informed back whether 
# they won, tied or lost. The user should also be asked whether they want to play again.
# The game should keep track of the number of rounds, the number of wins, losses and ties 
# and display these at the end of the game.

import random

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    rounds = 0
    wins = 0
    losses = 0
    ties = 0
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please try again.")
            continue
        computer_choice = random.choice(["rock", "paper", "scissors"])
        print(f"Computer chose: {computer_choice}")
        if user_choice == computer_choice:
            print("It's a tie!")
            ties += 1
        elif user_choice == "rock" and computer_choice == "scissors":
            print("You win!")
            wins += 1
        elif user_choice == "scissors" and computer_choice == "paper":
            print("You win!")
            wins += 1
        elif user_choice == "paper" and computer_choice == "rock":
            print("You win!")
            wins += 1
        else:
            print("You lose!")
            losses += 1
        rounds += 1
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again != "yes":
            break
    print(f"Game over! Rounds: {rounds}, Wins: {wins}, Losses: {losses}, Ties: {ties}")

if __name__ == "__main__":
    play_game()

# Run the game
# python app.py
# Output:
# Welcome to Rock, Paper, Scissors!
# Enter your choice (rock, paper, scissors): rock
# Computer chose: scissors
# You win!
# Do you want to play again? (yes/no): yes
# Enter your choice (rock, paper, scissors): rock
# Computer chose: paper
# You lose!
# Do you want to play again? (yes/no): yes
# Enter your choice (rock, paper, scissors): rock
# Computer chose: rock
# It's a tie!
# Do you want to play again? (yes/no): no
# Game over! Rounds: 3, Wins: 1, Losses: 1, Ties: 1