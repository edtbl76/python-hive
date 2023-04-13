from random import randint

options = ["ROCK", "PAPER", "SCISSORS"]
message = {
    "tie": "It's a tie!",
    "won": "You won",
    "lost": "Loser!!!!"
}


def decide_winner(user_choice, computer_choice):
    print(f"You selected      : {user_choice}")
    print(f"Computer Selected : {computer_choice}")

    if user_choice == computer_choice:
        print(message["tie"])
    elif user_choice == options[0] and computer_choice == options[2]:
        print(message["won"])
    elif user_choice == options[1] and computer_choice == options[0]:
        print(message["won"])
    elif user_choice == options[2] and computer_choice == options[1]:
        print(message["won"])
    else:
        print(message["lost"])


def play_RPS():
    user_choice = input("Enter Rock, Paper, or Scissors: ").upper()
    computer_choice = options[randint(0, 2)]
    decide_winner(user_choice, computer_choice)


play_RPS()
