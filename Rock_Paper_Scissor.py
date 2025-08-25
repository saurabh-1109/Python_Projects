# rock paper scissor game 

import random

# Option for the user 
print('''
     -1: "rock",
      0: "paper",
      1: "scissor",
      10: "Scorecard",
      100: "Exit",
      200: "Play Again"
''')

# Dict for the options 
comp = {
    -1: "rock",
    0: "paper",
    1: "scissor",
}

def rock_paper_scissor():

    #points of payers
    userpoint = 0      
    comppoint = 0
    nr = 0
    
    while True:
        yourchoice = int(input("Enter Your Choice: "))   # input from user
        
        if yourchoice not in [-1, 0, 1, 10, 100, 200]:
            print("Invalid choice. Choose Again.")
            continue
        
        if yourchoice == 100:           # exit programm 
            print("Exiting...")
            break
        
        if yourchoice == 10:            # score card 
            print(f'''
                SCORECARD:
                    Your score = {userpoint}
                    Computer score = {comppoint}
                    Number of draws = {nr}
            ''')
            continue
        
        if yourchoice == 200:           # new game 
            print("--------------------------------------------------------------------------------------------")
            print("Starting New Game")
            print('''
                -1: "rock",
                0: "paper",
                1: "scissor",
                10: "Scorecard",
                100: "Exit",
                200: "Play Again"
            ''')
            userpoint = 0
            comppoint = 0
            nr = 0
            continue
        
        computer = random.choice([-1, 0, 1])  # Generating random number from computer

        # sending user option to dict for kerword
        youroption = comp[yourchoice]
        compoption = comp[computer]
        
        print(f"You choose {youroption}")
        print(f"Computer choose {compoption}")
        
        if computer == yourchoice:     
             # game draw
            print("Game Draw....")
            nr += 1
        else:
            # User win option 
            if (computer == -1 and yourchoice == 0) or \
               (computer == 0 and yourchoice == 1) or \
               (computer == 1 and yourchoice == -1):
                print("You Won....")
                userpoint += 1
            else:
                #computer wins
                print("You Lost....")
                comppoint += 1

rock_paper_scissor()
