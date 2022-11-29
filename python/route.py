import random;

class Route: 
  id = int
  start = []
  end = []
  
  def __init__(self, start, end):
    self.id = random.randint(0, 100000);
    self.start = start;
    self.end = end;