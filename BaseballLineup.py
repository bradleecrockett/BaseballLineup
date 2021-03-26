

def make_players(num):
    players = []
    for i in range(num):
        players.append(str(i+1))
    return players


def line_up(players):
    for i in range(len(players)):
        print(i+1, "-", players[i])

    last = players[-1]
    players.insert(0, last)
    return players[:-1]

def game_positions(players):
    positions = ["Pitcher", "Left Center", "Bench", "Short Stop", "Right Field", "1st Base", "Bench", "2nd Base", "Left Field", "3rd base", "Right Center", "Bench"]
    # four innings worth of positions for each game
    for inning in range(4):
        print("*" * 20)
        for i in range(len(players)):
            print(positions[i], "--", players[i])
        print()



def main():
    players = ["Ryan #1", "Cody #2", "Channing #3", "Marshall #4", "Owen #6", "Christian #7", "Gianna #8", "Hudson #9", "Kaden #10", "Carter #11", "Knox #12", "Jackson #13"]
    print("Welcome to Baseball Lineup")

    for game in range(10):
        print("Game", game+1)
        print("~"*20)
        players = line_up(players)
        game_positions(players)
        print("~" * 20)







if __name__ == '__main__':
    main()