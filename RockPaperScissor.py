import random

print("WELCOME TO THE ROCK PAPER SCISSORS GAME")

rock='''
\t                _    
\t               | |   
\t _ __ ___   ___| | __
\t| '__/ _ \ / __| |/ /
\t| | | (_) | (__|   < 
\t|_|  \___/ \___|_|\_\\

'''
paper='''                            
\t _ __   __ _ _ __   ___ _ __ 
\t| '_ \ / _` | '_ \ / _ \ '__|
\t| |_) | (_| | |_) |  __/ |   
\t| .__/ \__,_| .__/ \___|_|   
\t| |         | |              
\t|_|         |_|              
'''
scissors='''
\t          _                        
\t         (_)                       
\t ___  ___ _ ___ ___  ___  _ __ ___ 
\t/ __|/ __| / __/ __|/ _ \| '__/ __|
\t\__ \ (__| \__ \__ \ (_) | |  \__ \\
\t|___/\___|_|___/___/\___/|_|  |___/
'''

game_images= [rock, paper, scissors]
users_choice=int(input("Enter your choice(0 for rock, 1 for paper, 2 for scissors)"))
if users_choice>2 or users_choice<0:
    print("Please enter a valid choice")
else:
    print("Your choice: ")
    print(game_images[users_choice])
    
    computers_choice= random.randint(0,2)
    print("Computer's choice: ")
    print(game_images[computers_choice])
    
    if users_choice==0:
        if computers_choice==0:
            print("It's a draw")
        elif computers_choice==1:
            print("You lose")
        else:
            print("You win")
    elif users_choice==1:
        if computers_choice==0:
            print("You win")
        elif computers_choice==1:
            print("It's a draw")
        else:
            print("You lose")
    else:
        if computers_choice==0:
            print("You lose")
        elif computers_choice==1:
            print("You win")
        else:
            print("It's a draw")
