"""
Welcome to the color game>>>
please enter the name for score board

1> start game
2> exit

if 1
please enter the color: redasddfa
 validate the color if the given color is not present in the
 list then tell user you have entered invalid color

 if color is validated then
 match it with machine generated color
 if matching then display the message like
 you wom the game
 number of attempts : 1
 total number of attempts: 5

 if not matching then display the message:

 your guess was wrong please try again
 number of attempts left: 04

 once after completing the game till 5th attempts tell user
 1> see score board
 2> play again
 3> exit

 if he  choose 1 then:
 number of game won:01
 number of game loose:01
 name of the player: abc
  \
"""

import random
from unicodedata import name
win =  0
lost  = 0
def play_game():
    global win ,lost
    attempt = 5
    list = ["Red" , "Blue" , "White" , "Black" , "Green" , "Yellow" , "Purple" , "Pink" , "Brown"]
    select = random.choice(list)
    for i in range(1,attempt+1):
        attempt -=1
        color = input("Enter the color name:- ").lower
        if color in list:
            if(color==select):
                print("You won the game")
                print("Attempts needed: ",5-attempt)
                win +=1
                break
            else:
                print("You guess was wrong")
                print("Number of attempts left",attempt)
        else:
            print("Enter the valid color")
            if(attempt==0 and color!=select):
                print("You have lost the game")
                print("The color was:- ",select)
                lost+=1
                break
    return



if __name__ == "__main__":
    count =0
    print("Welcome the color game")
    print("Please choose from given option")
    choice = int(input("Enter 1 to play \n Enter 2 to exit:-"))
    while(choice==1):
        count+=1
        play_game()
        choice2  = int(input("Enter 1 to see scoreboard\n 2 to play again\n3 to exit:-"))
        if(choice2==1):
            print("Number of time winned:- ",win)
            print("Number of time game lost :- ",lost)
            print("Number of time game payed",count)
            break
        elif(choice2==3):
            print("You exited the game")
            break
        else:
             ("Enter correct number:-")
        
        while(choice2==2):
            play_game()
            choice2 = int(input("Enter 1 to see scoreboard\n2 to play again\n3 to exit:-"))
            count+=1
            break
        
            

    else:
        print("You exited the game")