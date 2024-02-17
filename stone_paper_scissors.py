import random
def get_choices():
    player_choice = input("Enter a choice b/w (Rock/Paper/Scissors) : ")
    options = ["Rock","Paper","Scissors"]
    computer_choice = random.choice(options)
    choices = {"player" : player_choice,"computer":computer_choice}
    return choices

def check_win(player,computer):
    print(f"You choose : {player}\nComputer choose : {computer}")
    if player==computer:
        return "It's a tie"
    elif player=="Rock":
        if computer=="Paper":
            return "Paper covers Rock, You Lose!!!"
        elif computer=="Scissors":
            return "Rock breaks Scissors.You Win!!!"
    elif player=="Paper":
        if computer=="Rock":
            return "Paper covers Rock, You Win!!!"
        elif computer=="Scissors":
            return "Scissors cut the Paper,You Lose!!!"
    elif player=="Scissors":
        if computer=="Rock":
            return "Rock breaks Scissors,You Lose!!!"
        elif computer=="Paper":
            return "Scissors cut Paper.You Win!!!"

choices = get_choices()
result = check_win(choices["player"],choices["computer"])
print(result)
