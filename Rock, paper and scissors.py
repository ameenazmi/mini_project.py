import random

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]
quit_flag = False

print("Let's play rock, paper, scissors!")
input("Press enter key to start")
while user_wins < 5 and computer_wins < 5:
    user_input = input("Type rock, paper, scissors or Q if you want to quick. ").lower()
    if user_input == "q":
        print("Okay, GoodBye!")
        quit_flag = True
        break
        
    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    computer_bot = options[random_number]

    if (user_input == "rock" and computer_bot == "scissors") or (user_input == "paper" and computer_bot == "rock") or (user_input == "scissors" and computer_bot == "paper"):
        print("You Won!")
        user_wins += 1
    
    elif user_input == computer_bot:
        print("It's tie")
    
    else:
        print("Computer Won!")
        computer_wins += 1

    print(f"User score: {user_wins} || Computer score: {computer_wins}")

if quit_flag is False:
    if user_wins > computer_wins:
        win_percentage = (user_wins/5) * 100
        print(f"Congratulations, you won by {win_percentage}%!")
    else:
        win_percentage = (computer_wins/5) * 100
        print(f"Congratulations, computer won by {win_percentage}%!")


