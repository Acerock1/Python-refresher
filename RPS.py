import random

def get_choices():
    player_choice = input("CHOOSE: ROCK, PAPER OR SCISSORS ").capitalize()  # Capitalize the input
    options = ("Rock", "Paper", "Scissors")
    computer_choice = random.choice(options)

    
    choices = {'Player': player_choice, 'Computer': computer_choice}
    return choices  

def check_win(player, computer):
    print(f"Player chose {player} and Computer chose {computer}")

    if player == computer:
        return "It's a tie"
    elif player == 'Rock':
        if computer == 'Paper':
            return "Paper wraps Rock! You lose!"
        else:
            return 'Rock smashes Scissors! You win!'
    elif player == 'Scissors':
        if computer == 'Paper':
            return 'Scissors cuts Paper! You win!'
        else:
            return 'Rock smashes Scissors! You lose!'
    elif player == 'Paper':
        if computer == 'Rock':
            return 'Paper wraps Rock! You win!'
        else:
            return 'Scissors cuts Paper! You lose!'

parameters = get_choices()


result = check_win(parameters['Player'], parameters['Computer'])
print(result)
