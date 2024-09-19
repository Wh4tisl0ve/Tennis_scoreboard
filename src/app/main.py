from app.game_logic.tennis_game import TennisGame


def main():
    game = TennisGame()

    for i in range(5):
        game.player1_goals()
        print(game.get_dict())

    for i in range(3):
        game.player2_goals()
        print(game.get_dict())

    dict_game = game.get_dict()
    print("".ljust(10) + "| player1 | player2")
    print("-" * 32)
    print("Match:".ljust(9) + str(dict_game['player1_match']['value']).rjust(10) + " | " +
          str(dict_game['player2_match']['value']).rjust(10))
    print("Sets:".ljust(9) + str(dict_game['player1_match']['player1_set']['value']).rjust(10) + " | " +
          str(dict_game['player2_match']['player2_set']['value']).rjust(10))
    print("Points:".ljust(9) + str(dict_game['player1_match']['player1_set']['points']).rjust(10) + " | " +
          str(dict_game['player2_match']['player2_set']['points']).rjust(10))


if __name__ == '__main__':
    main()
