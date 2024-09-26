import json

from app.game_logic.tennis import Tennis


def main():
    game = Tennis()
    for i in range(85):
        game.player1_goals()

    print(json.dumps(game.get_dict(), indent=4))


if __name__ == '__main__':
    main()
