VALID_OPTIONS = ['rock', 'paper', 'scissors']
# the first item is the winner and the second is the loser
WINNING_COMBOS = [['paper', 'rock'], ['rock', 'scissors'], ['scissors', 'paper']]


def rps(player1, player2):
    """
    player1,player2 must be strings-either "rock","paper" or "scissors\"
    """
    if player1.lower() not in VALID_OPTIONS:
        return 'Invalid input'
    if player2.lower() not in VALID_OPTIONS:
        return 'Invalid input'
    if player1 == player2:
        return 'tie game'
    elif [player1, player2] in WINNING_COMBOS:
        return 'player1 wins'
    elif [player2, player1] in WINNING_COMBOS:
        return 'player2 wins'

# test
# print(rps('rock', 'scissors'))
# print(rps('rock', 'paper'))
# print(rps('rock', 'rock'))
# print(rps('roc', 'scissors'))
