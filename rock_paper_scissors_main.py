
#Program to play Rock-Paper-Scissor game
#with user

import random

def play():
    rykker = [ "R", "P", "S"]
    choice = random.choice(rykker)
    guess = inner()
    decision(guess, choice)

def inner():
    print("Let's play rock, paper, scissors. Enter R for Rock, P for paper, S for scissors")
    sow = input("R, P, S, ...")
    boolean = True
    while boolean == True:
        if sow != "R":
            if sow != "P":
                if sow != "S":
                    sow = input("Heisss, you no dey hear word? I said enter either R, P, or S. Abi you wan collect woto woto")
        boolean = False        

    return sow

def decision(guess, choice):
    if guess == "S" and choice == "R":
        print("Loser oh, loser oh, you don lose: Rock blunts Scissors")
        
    elif guess == "R" and choice == "S":
        print("Cool! you won. That's unexpected: Rock blunts Scissors")
    elif guess == "P" and choice == "R":
        print("Cool! you won. huh?: Paper covers Rock")
    elif guess == "R" and choice == "P":
        print("Yikes, you lost. ntorr: Paper covers Rock")
    elif guess == "P" and choice == "S":
        print("Scissors cuts paper bruv. You lose")
    elif guess == "S" and choice == "P":
        print("All power belongs to you comrade: Scissors cuts paper")
    elif guess == choice:
        print("Draw, you get luck")
        play()
    
play()
#@George Akor
#theStormGod
