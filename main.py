from game.TTT_game import TTTGame
from game.settings import Settings

if __name__ == '__main__':
    settings_obj = Settings()

    while True:
        game = TTTGame(settings_obj)
        game.run()
