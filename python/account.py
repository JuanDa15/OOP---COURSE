import random;

class Account: 
  id = int
  name = str
  document = str
  email = str
  password = str
  
  def __init__(self, name, document, email, password):
    self.id = random.randint(0, 100000)
    self.name = name
    self.document = document
    self.email = email
    self.password = password