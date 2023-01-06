#!/usr/bin/python3

""""" 
ROCK PAPER SCISSORS 
"""""

# import random
import random

# use tuple instead of a list: 

options = ("rock", "paper", "scissors")

# to allow the player continue playing then add a while loop and add all the code below inside: 
# creeate a variable and set it to True
continuePlaying = True

while continuePlaying:
    # to reset player and computer each time begin a new game a new player will be selected and computer will pick a random selection.  

    # player variable will store the player selection
    player = None

    # computer will pick at random  from the option variable and use the function choice() and pass the option variable 
    computer = random.choice(options)


     # create a while loop thethe player selection and check for the condition to ensure players are selecting the right option input validation: while loop will continue looping as long as the right selection has not been selected 
    while player not in options:

        # request the user to select a choice: 
        player = input("Please pick a choice (rock, paper, scissors): ")

    #use a f string to print the player selection: 

    print(f"Player: {player}")

    #f string to print computer selection: 
    print(f"Computer: {computer}")


    # checking for the score winner losers or tie:
    if player == computer:
        print("It is a tie game") 
    elif player == "rock" and computer =="scissors": 
        print("PLAYER WIN!!!")
    elif player == "paper" and computer == "rock":
        print("PLAYER WIN AS WELL!!")
    elif player == "scissors" and computer == "paper": 
        print("PLAYER WIN ONCE AGAIN")
    # after checking for all the winnning posibilities then create an else to check when player lose
    else:
        print("Player lose") 
   #check if the player will like to continue playing yes or no and set the input to be converted to lower case and if the user select n for no then set continuePlaying variable to false and print a message thanking the user for playing: 
    if not input("Please play again (y/n): ").lower() == "y":
        continuePlaying = False 

print("It was a pleasure playing with you :) hope to play with you soon! ")


