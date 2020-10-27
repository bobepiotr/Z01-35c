import random as ran
import sys

elements = ["paper", "rock", "scissors"]
win_sets = [("paper", "rock"), ("rock", "scissors"), ("scissors", "paper")]


def game(rounds=3):
    winner = "draw"
    players_points = 0
    computers_points = 0

    players_pick = ""
    comp_pick = ""

    for i in range(rounds):
        print("--------------ROUND " + str(i + 1) + "--------------")

        while players_pick not in elements:
            players_pick = input("What's your pick? ")

        comp_pick = ran.choice(elements)
        print("That's " + players_pick + " vs " + comp_pick)

        if (players_pick, comp_pick) in win_sets:
            players_points += 1
            print("You've WON this round")
        elif players_pick == comp_pick:
            print("Draw...")
        else:
            computers_points += 1
            print("You've LOST this round")
        players_pick = ""
        print("")

    draws = rounds - computers_points - players_points

    print("-----------SCOREBOARD-----------")
    print('{:16} {:>4} {:>4} {:>4}'.format("Player name", "W", "L", "D"))
    print('{:16} {:>4} {:>4} {:>4}'.format("Player", players_points, computers_points, draws))
    print('{:16} {:>4} {:>4} {:>4}'.format("Computer", computers_points, players_points, draws))

    if players_points > computers_points:
        winner = "Player"
    elif players_points < computers_points:
        winner = "Computer"

    if (winner != "draw"):
        print("The winner is " + winner)
    else:
        print("That's a draw")


def main(args):
    if (len(args) > 1):
        try:
            rounds = int(args[1])
            game(rounds)
        except ValueError:
            print("Integer excepted")
    else:
        game()


if __name__ == "__main__":
    main(sys.argv)
