import random

Gestures = ["Rock", "Paper", "Scissor"]

playerWins = 0
botWins = 0

def getWinType(playerG, botG):

    global playerWins
    global botWins

    if playerG == botG:
        return "Draw"
    

    elif playerG == "Rock" and botG == "Scissor":
        playerWins += 1
        return "You win!"
    
    elif playerG == "Paper" and botG == "Rock":
        playerWins += 1
        return "You win!"
    
    elif playerG == "Scissor" and botG == "Paper":
        playerWins += 1
        return "You win!"
    

    elif botG == "Rock" and playerG == "Scissor":
        botWins += 1
        return "I win!"
    
    elif botG == "Paper" and playerG == "Rock":
        botWins += 1
        return "I win!"
    
    elif botG == "Scissor" and playerG == "Paper":
        botWins += 1
        return "I win!"

while True:

    playerGesture = input("\nRock - Paper - Scissor: ").capitalize()
    botGesture = Gestures[random.randint(0, 2)]

    print(f"\nYou chose: {playerGesture}")
    print(f"I chose: {botGesture}")

    win = getWinType(playerGesture, botGesture)

    print(f"{win} ({playerWins} : {botWins})")