import random

def check_winner(player, computer):
    if (player == 3 or computer == 3):
        return True
    return False

def final_winner(player, computer):
    if (player > computer):
        return "You win!!!"
    elif (player < computer):
        return "computer wins!!!"
    else:
        return "Its a draw!!!"

def display_score(p,c):
    print ("You:" + str(p))
    print ("Computer:" + str(c))

def start_game():
    games = 5
    player_wins = 0
    computer_wins = 0
    print ("Lets start")
    while (games > 0):
        if (check_winner(player_wins, computer_wins)):
            break
        options = ["rock", "paper", "scissors"]

        computer_choice = options[random.randint(0, len(options) - 1)]
        player_choice = input("Rock, paper, or scissors says... GO!!!! ")
        print (computer_choice)

        if(computer_choice == player_choice):
            print ("Match! Try Again")
        elif(computer_choice == "rock" and player_choice == "paper"):
            player_wins += 1
            games -= 1
            display_score(player_wins, computer_wins)
        elif(computer_choice == "rock" and player_choice == "scissors" ):
            computer_wins += 1
            games -= 1
            display_score(player_wins, computer_wins)
        elif(computer_choice == "paper" and player_choice == "rock"):
            computer_wins += 1
            games -= 1
            display_score(player_wins, computer_wins)
        elif(computer_choice == "paper" and player_choice == "scissors"):
            player_wins += 1
            games -= 1
            display_score(player_wins, computer_wins)
        elif(computer_choice == "scissors" and player_choice == "rock"):
            computer_wins += 1
            games -= 1
            display_score(player_wins, computer_wins)
        elif(computer_choice == "scissors" and player_choice == "paper"):
            player_wins += 1
            games -= 1
            display_score(player_wins, computer_wins)


    print ("Game Over")

    print (final_winner(player_wins, computer_wins))


start_game()
