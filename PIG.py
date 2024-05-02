import random

input("Press Enter to start ")

def roll():
    min_roll = 1
    max_roll = 12
    roll = random.randint(min_roll, max_roll)

    return roll

while True:
    players = input("Enter the number of players (1-5): ")
    if players.isdigit():
        players = int(players)
        if 1<= players <= 5:
            break
        else:
            print("ERROR!")
            print("Number of player must be between 1-5")
    else:
        print("You must enter the number!")

max_score = 100
player_score = [0 for _ in range(players)]
print("\nRULES")
print("- Every point in your roll will be add to your points")
print("- First player to get near to 100 points will be the winner")
print("- If you rolled (1), your point will be reset to 0")

rounds = 0
while max(player_score) < max_score:

    for player_index in range(players):
        print(f"\nTurn player {player_index + 1} has started.\n")
        current_score = 0

        while True:
            
            roll_key = input("Enter (y) to roll the dice ").lower()
            if roll_key != "y":
                print("Your turn end!")
                break

            value = roll()
            if value == 1:
                current_score = 0
                print(f"Unlucky your score now is {current_score}")
                break

            else:
                current_score += value
                print(f"Your roll: {value}")
                print(f"Your score: {current_score}")
        
        player_score[player_index]+= current_score
        print(f"\nPlayer {player_index + 1} score: {player_score[player_index]}")

    rounds += 1
print(f"\nYou have played {rounds} round")
print(f"\nThe winner is player {player_score.index(max(player_score))+ 1}\n")
        


