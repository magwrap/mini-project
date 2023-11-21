import random
from bots.base_bot import BaseBot


class ManualBot(BaseBot):
    def __init__(self, uid):
        self.rand = random.Random(uid)
        super().__init__(uid, f"{self.__class__.__name__}_{uid}", [self.rand.randrange(255) for _ in range(3)])
        self.cols = 0
        self.rows = 0

    def init_board(self, cols: int, rows: int, obstacles: [(int, int)], time_given: int) -> None:
        self.cols = cols
        self.rows = rows

    def make_a_move(self, time_left: int) -> (int, int):
        x = int(input(f"X (<{self.cols}):"))
        y = int(input(f"Y (<{self.rows}):"))
        return x, y
