# TASK 4 : Rock-Paper-Scissors Game USING PYTHON (CLI)

import random

def get_user_choice():
    print("\nChoose one: Rock, Paper, or Scissors")
    choice = input("Your choice: ").strip().lower()
    if choice not in ["rock", "paper", "scissors"]:
        print("❌ Invalid input! Please choose again.")
        return get_user_choice()
    return choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "win"
    else:
        return "lose"

def display_result(user, computer, result):
    print(f"\n🧍‍♂️ You chose: {user.capitalize()}")
    print(f"💻 Computer chose: {computer.capitalize()}")

    if result == "win":
        print("🎉 You WIN this round!")
    elif result == "lose":
        print("😢 You LOST this round.")
    else:
        print("🤝 It's a TIE!")

def play_game():
    user_score = 0
    computer_score = 0
    round_num = 1

    while True:
        print(f"\n====== Round {round_num} ======")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)

        display_result(user_choice, computer_choice, result)

        # Score Tracking
        if result == "win":
            user_score += 1
        elif result == "lose":
            computer_score += 1

        print(f"\n📊 Score: You {user_score} - {computer_score} Computer")

        # Play Again
        play_again = input("\nDo you want to play another round? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("\nThanks for playing! Final Score:")
            print(f"🧍‍♂️ You: {user_score} | 💻 Computer: {computer_score}")
            break

        round_num += 1

# Start the game
play_game()
