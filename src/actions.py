class Action:
  pass 

class EscapeAction(Action):
  pass

class MovimentAction(Action):
  def __init__(self, dx: int, dy: int):
    super().__init__()

    self.dx = dx
    self.dy = dy