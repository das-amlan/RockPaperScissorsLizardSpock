import random


def play():
    player = input("'r' for rock, 'p' for paper, 's' for scissors, 'l' for lizard, 'sp' for Spock: ")
    computer = random.choice(['r', 'p', 's', 'sp'])

    print(f"\nPlayer: {player}")
    print(f"Opponent: {computer}")

    if player == computer:
        return "\nIt is a tie"

    if is_win(player, computer):
        return "\nYou won!"
    return "\nYou lost"


def is_win(user, opp):
    # Scissors cuts Paper
    # Paper covers Rock
    # Rock crushes Lizard
    # Lizard poisons Spock
    # Spock smashes Scissors
    # Scissors decapitates Lizard
    # Lizard eats Paper
    # Paper disproves Spock
    # Spock vaporizes Rock
    # (and as it always has) Rock crushes Scissors
    # Video
    if (user == 'r' and opp == 's') or (user == 's' and opp == 'p') \
            or (user == 'p' and opp == 'r') or (user == 'r' and opp == 'l')\
            or (user == 'l' and opp == 'sp') or (user == 'sp' and opp == 's')\
            or (user == 's' and opp == 'l') or (user == 'l' and opp == 'p')\
            or (user == 'p' and opp == 'sp') or (user == 'sp' and opp == 'r'):
        return True


print(play())
