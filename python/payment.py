import random;

class Payment:
  id = str
  
  def __init__(self):
    self.id = random.randint(0, 10000)
    
class Card(Payment):
  number = int
  cvv = int
  date = str
  
  def __init__(self, number, cvv, date):
    super(Card, self).__init__()
    self.number = number
    self.cvv = cvv
    self.date = date
    
class Paypal(Payment):
  
  email = str
  
  def __init__(self, email):
    super(Paypal, self).__init__()
    self.email = email
    
    
class Card(Payment):
  
  def __init__(self):
    super(Card, self).__init__()