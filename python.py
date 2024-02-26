def ComputerCHOICE():
    return "rock"


def games_played():
    games_played = 0
    while game_played > 3:


def playerCHOICE():
    playerCHOICE = input("please choose rock, paper, or scissors  ").lower()
    if playerCHOICE == ComputerCHOICE():
        print("you tied")
    elif playerCHOICE == "scissors":
        print("computer plays rock you lose")
    elif playerCHOICE == "paper":
        print("you won!!!")
    else:
        print("error please re run code")
game_played = games_played + 1

playerCHOICE()
