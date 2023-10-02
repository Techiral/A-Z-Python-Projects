import random

# Flag variable for starting or ending next round
flag_next_round = True

# Flag variables for input validation
validate_start = True
validate_next_round = True

# Initializing empty dictionary to store player details
player_details = {}

while True:
    try:
        no_of_players = int(input("How many players are playing? "))
        if no_of_players > 0:
            break
        else:
            print("\nERROR ::: NUMBER OF PLAYERS MUST BE GREATER THAN 0 \n")
    except ValueError:
         print("\nERROR ::: NUMBER OF PLAYERS MUST BE A NUMBER \n")

for individual_player_id in range(1,(no_of_players+1)):
    # Getting player's name for each id and adding it to player_details dictionary with id as key and name as value
    print("\n" + "Enter details of player " + str(individual_player_id))
    player_name = input("Enter player's name : ")
    player_details[individual_player_id] = player_name

print("\nGAME SETUP COMPLETE!")

while validate_start:
    start_game = (input("Do you want to start the game(yes/no) ?")).lower()

    if start_game == 'yes':
        validate_start = False
        if len(player_details) == 1:
            flag_next_round = False
            for key,value in player_details.items():
                print("\nWINNER is Player "+str(key)+" "+value)
        while flag_next_round:
            if len(player_details)>1:
                out_player_id = random.randint(1,no_of_players)
                print("\n"+ str(out_player_id) + " is the generated number")
                try:
                    if player_details[out_player_id]:
                        print("Player " + str(out_player_id) +" "+ player_details[out_player_id]+ " is out!! \n")
                        del player_details[out_player_id] # Removing the player from the dictionary
                except KeyError:
                    print("Player already out! \n")
                if len(player_details)>1:
                    while validate_next_round:
                        next_round = (input("Let's move to next round, shall we ?(yes/no) ")).lower()
                        if next_round == 'no':
                            flag_next_round = False
                            validate_next_round = False
                            print("-----------EXITED----------------")
                        elif next_round == 'yes':
                            validate_next_round = False
                        else:
                            print("\nERROR ::: Enter 'yes' or 'no' \n")
                else:
                    flag_next_round = False
                    for key,value in player_details.items():
                        print("\nWINNER is Player "+str(key)+" "+value)
    elif start_game == 'no':
        print("-----------EXITED----------------")
        break
    else:
        print("\nERROR ::: Enter 'yes' or 'no' \n")


        
