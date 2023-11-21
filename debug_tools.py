def read_bot_scores() -> None:
  print("bot scores")

  bot_scores: dict = {}
  with open("bot_outcome.txt", "r") as outcome:
    scores: list = outcome.readlines()

    for bot in set(scores):
      bot_scores[bot] = scores.count(bot)
    
    for key, value in bot_scores.items():
      print(f"{key[:-2]} --> {value}")

def read_game_state() -> None:
  print("game state: ")

  game_state: dict = {}
  with open("game_state.txt", "r") as outcome:
    states: list = outcome.readlines()

    for state in set(states):
      game_state[state] = states.count(state)

    for key, value in game_state.items():
      print(f"{key[:-2]} --> {value}")
    


  


read_bot_scores()
print(" ")
read_game_state()