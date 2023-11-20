import random

def play_game(level_range, max_attempts):
    #to generate a random number inside of the chosen level range 
    number = random.randint(*level_range)
    guessed = False
    attempts = 0

    #inicial message
    print(f"Chose a number between {level_range[0]} and {level_range[1]}.")
    print("If you guess right, YOU WIN!")

    while not guessed and attempts < max_attempts:
        user_number = int(input("Enter your guess: "))
        #for the player to choose the level he wants 
        attempts += 1

        #indications to find the random number 
        if user_number < number:
            print("It's a bigger number!")
        elif user_number > number:
            print("It's a smaller number!")
        else:
            print("CONGRATULATIONS! YOU WIN!")
            guessed = True

    if guessed:
        player_name = input("Enter your name: ")
        update_leaderboard(player_name, attempts)
    #for the player to be in the leader board 

def load_leaderboard():
    try:
        with open("leaderboard.txt", "r") as file:
            leaderboard = eval(file.read())
    except FileNotFoundError:
        print("Leaderboard file not found. Creating a new one.")
    finally:
        return leaderboard
#to open the leaderboard.txt or create one in case it's not found 
    
def update_leaderboard(player_name, attempts):
    leaderboard = load_leaderboard()
    leaderboard[player_name] = attempts
    sorted_leaderboard = dict(sorted(leaderboard.items(), key=lambda item: item[1]))
    print("\nLeaderboard:")
    for rank, (name, score) in enumerate(sorted_leaderboard.items(), start=1):
        print(f"{rank}. {name}: {score} attempts")
    save_leaderboard(sorted_leaderboard)
#to add the name of the player and the number of attemps and order the dictionnary by the number of attemps 

def save_leaderboard(leaderboard):
    with open("leaderboard.txt", "w") as file:
        file.write(str(leaderboard))
#save de txt in the computer 

def main():
    print("\nWelcome to the Random Number Game!")
    print("1. Easy (0-99)")
    print("2. Intermediate (0-1000)")
    print("3. Advanced (0-1000000)")
    print("4. Expert (0-1000000000000)")
    #to offer the choice of level to the player 

    choice = input("Choose a level (1-4): ")

    if choice in ('1', '2', '3', '4'):
        level_range = (0, 99) if choice == '1' else (0, 1000) if choice == '2' else (0, 1000000) if choice == '3' else (0, 1000000000000)
        max_attempts = 10  
        play_game(level_range, max_attempts)
    else:
        print("Invalid choice. Please choose a level between 1 and 4.")

if __name__ == "__main__":
    main()
