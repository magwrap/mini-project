"""
RULES

Win: If you have two in a row, play the third to get three in a row.

Block: If the opponent has two in a row, play the third to block them.

Fork: Create an opportunity where you can win in two ways.

Block Opponent's Fork:

Option 1: Create two in a row to force the opponent into defending, as long as it doesn't result in them creating a fork or winning. For example, if "X" has a corner, "O" has the center, and "X" has the opposite corner as well, "O" must not play a corner in order to win. (Playing a corner in this scenario creates a fork for "X" to win.)

Option 2: If there is a configuration where the opponent can fork, block that fork.

Center: Play the center.

Opposite Corner: If the opponent is in the corner, play the opposite corner.

Empty Corner: Play an empty corner.

Empty Side: Play an empty side.

"""
from bots.base_bot import BaseBot

# OFFICIAL BOT

class TeamYourNameBot(BaseBot):
    def __init__(self, uid) -> None:
        # Make your bot personal
        # Your code start here
        name = "TeamYourNameBot"
        color = (0, 255, 0)  # RGB color values, set the values between 0 and 255
        # Your code ends here
        super().__init__(uid, name, color)
        # Your code start here
        # E.g initialize extra object variables
        # Your code ends here

    def init_board(self, cols: int, rows: int, obstacles: [(int, int)], time_given: int) -> None:
        """
        This method is invoked at the game initialization.

        Parameters:
        cols: The size of the same board in columns.
        rows: The size of the game board in rows.
        obstacles: The list of (x, y) coordinates of blocked board cells.
        time_given: The total time given to the player bot for the game in ns.
        """
        pass

    def make_a_move(self, time_left: int) -> (int, int):
        """
        This method is called when the bot needs to make a move. It will calculate the best move with the given board.

        Parameters:
        time_left: a value indicating time remaining for the bot to complete a game in ns

        Returns:
        tuple: containing the bot move with the order (x, y)
        """
        # Implement the algorithm which will make the moves
        # Your code starts here
        x = -1
        y = -1
        # Your code ends here
        return x, y

    def notify_move(self, bot_uid: int, move: (int, int)) -> None:
        """
        This method is called when a move is made by a player.

        Parameters:
        bot_uid: The Unique ID of the player making the move.
        move: A tuple representing the move coordinates (x, y).
        """
        (x, y) = move
