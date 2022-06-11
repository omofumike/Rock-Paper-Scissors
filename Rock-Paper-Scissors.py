import random

while True:

    print("Rock Paper Scissors \n"
    "RULES OF THE GAME \n"
    "Paper vs Scissors = Scissor wins \n"
    "Rock vs Paper = Paper wins \n"
    "START GAMES!!!")

    player_choice = input("Enter your choice: R for Rock, \n P for Paper, \n S for Scissor \n")
    print("You select %s" %player_choice)
    choices= ["R", "P", "S"]
    computer_choice = random.choice ("choice")
    print("Computer's Choice is %s" %computer_choice)
    print("****checking****")

    if player_choice == computer_choice:
        print("It's a tie")
        keep_playing = input("Would you like to play again? 'y' for Yes 'n' for No")
        if keep_playing.lower() != "y":
            break
    elif player_choice == "s":
        if computer_choice == "p":
            print("Scissors cuts paper, you win!")
        else:
            print("Rock smashes scissors, you loos!")
    elif player_choice == "R":
        if computer_choice == "s":
            print("Rock smashes scissors, you win!")
        else:
            print("Paper covers rock, you win!")

    elif player_choice == "p":
        if computer_choice == "R":
            print("Paper cover's rock, you win!")
        else:
            print("Scissors cuts paper, you loose!")
    
    continue_game = input("Would you like to play again? 'y' for Yes 'n' for No\n")
    if continue_game.lower() != "y":
        break



