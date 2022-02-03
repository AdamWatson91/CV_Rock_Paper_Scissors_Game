def playRPS(play_until):
    import random
    #CREATE LIST OF OPTIONS AVILABLE: Rock, Paper, Scissors
    all_choice = ['Rock', 'Paper', 'Scissors']
    #Set scores to 0 to begin game
    player_score = 0
    computer_score = 0
    # continue playing game for the specified number of times
    while player_score < play_until and computer_score < play_until:
        #RANDOMLY SELECT COMPUTERS CHOICE FROM OPTIONS
        computer_choice = random.choice(all_choice)
        #ASK USER TO INPUT THEIR CHOICE
        player_choice = input('Enter your weapon of choice (Rock, Paper, or Scissors):').title()
        #Decide winner and keep score
        if  player_choice == computer_choice:
            print(f"Both players selected+ {player_choice}. This round is a draw.")
        elif player_choice == "Rock":
            if computer_choice == "Scissors":
                print("Rock smashes scissors! You win this round.")
                player_score += 1
            else:
                print("Paper covers Rock! You lose this round.")
                computer_score += 1
        elif player_choice == "Paper":
            if computer_choice == "Rock":
                print("Paper covers Rock! You win this round.")
                player_score += 1
            else:
                print("Scissors cuts paper! You lose this round.")
                computer_score += 1
        elif player_choice == "Scissors":
            if computer_choice == "Paper":
                print("Scissors cuts paper! You win this round.")
                player_score += 1
            else:
                print("Rock smashes scissors! You lose this round.")
                computer_score += 1
        #Show score to keep track of progress
        print("The current score is: You "+str(player_score)+" - "+str(computer_score)+" Computer")
    #When game ends confirm outcome of the game
    if player_score == 5:
        print("Congratulations you win the game")
    else:
        print("Unfortunately you lost the game")

#RUN THE CODE AS A FUNCTION
playRPS(2)