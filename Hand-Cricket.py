from random import randint
#Toss Logic
def Toss():
    player_toss_input=input('This is Toss. What you want to take even or odd:')
    player_toss_no=int(input('Enter your number:'))
    Computer_Toss=randint(1,10)
    print(f'Opponent has given {Computer_Toss}')
    if (player_toss_input=='even'):
        if (Computer_Toss + player_toss_no)%2==0:
            print('Wow you win the Toss!!')
            print('You will Bat now')
            Toss_result= 'win'
            return Toss_result
        else:
            print('Oops! You lose the Toss.')
            print('You will ball first')
            Toss_result= 'lose'
            return Toss_result
    elif(player_toss_input=='odd'):
        if (Computer_Toss + player_toss_no)%2!=0:
            print('Wow you win the Toss!!')
            Toss_result= 'win'
            return Toss_result
        else:
            print('Oops! You lose the Toss.')
            Toss_result= 'lose'
            return Toss_result
#Batting Logic
def Batting():
    Player_Score=0
    flag=False
    #Not Out
    while True:
        def get_valid_input():
            while True:
                try:
                    user_input = int(input("Enter Run between 1 and 10: "))
                    if 1 <= user_input <= 10:
                        return user_input
                    else:
                        print("Please enter a valid integer between 1 and 10.")
                except ValueError:
                    print("Please enter a valid integer.")

        # Call the function to get valid input
        player_run_input= get_valid_input()
        Computer_run_input=randint(1,10)
        if player_run_input!=Computer_run_input:
            Player_Score+=player_run_input

            print(f'Opponent had {Computer_run_input}. Your Current Score is incresed by {player_run_input} runs and now it is {Player_Score} Runs')
    #Out
        if player_run_input==Computer_run_input:
            print(f'Opponent has given {Computer_run_input}./n OUT!!!')
            print(f'You played great and scored a total of {Player_Score} Runs')
            return Player_Score
            flag=True
            break
#Balling Logic
def Balling():
    Opponent_Score=0
    flag=False
    #Not_Out
    while True:
        Computer_run_input=randint(1,10)
        def get_valid_input():
            while True:
                try:
                    user_input = int(input("Enter Run between 1 and 10: "))
                    if 1 <= user_input <= 10:
                        return user_input
                    else:
                        print("Please enter a valid integer between 1 and 10.")
                except ValueError:
                    print("Please enter a valid integer.")

        # Call the function to get valid input
        player_ball_input= get_valid_input()
        if Computer_run_input!=player_ball_input :
            Opponent_Score+=Computer_run_input
            print(f'Opponent had {Computer_run_input}. Opponent Current Score is incresed by {Computer_run_input} runs and now it is {Opponent_Score} Runs')
        if Computer_run_input==player_ball_input:
            print(f'Opponent has given {Computer_run_input}. OUT!!!')
            print(f'Opponent scored a total of {Opponent_Score} Runs')
            return Opponent_Score
            flag=True
            break


#Connecting the Funtions to the final logic of the game
Opponent_Score=0
Player_Score=0
Toss_Outcome=Toss()
if Toss_Outcome=='win':
    Player_Score+=Batting()
    
    Opponent_Score+=Balling()
elif Toss_Outcome=='lose':
    
    Opponent_Score+=Balling()
    Player_Score+=Batting()

#Score_Check Funtion
def Score_Check():
     print(f'Here are your Scores:')
     print(f'Opponent Scored ---> {Opponent_Score}')
     print(f'Your Score --->{Player_Score}')
    
Scores_of_Both_Teams=Score_Check()
if Opponent_Score<Player_Score:
    print(f'Wow, what a match.')
    # print(f'{Scores_of_Both_Teams}')
    print(f'Congratulations!!, You Won by {Player_Score-Opponent_Score} Runs')
elif Opponent_Score==Player_Score:
    print(f'Wow, what a match.')
    # print(f'{Scores_of_Both_Teams}')
    print(f'Sadly, this is Tie!!')
else:
    print(f'Wow, what a match.')
    # print(f'{Scores_of_Both_Teams}')
    print(f' Opponent Won  by {Opponent_Score-Player_Score} Runs')
