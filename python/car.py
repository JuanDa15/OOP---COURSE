import random;

class Car: 
  id = int
  license = str
  driver = str
  passengers = int
  
  def __init__(self,license,driver, passengers):
    self.id = random.randint(0,50000)
    self .license = license
    self.driver = driver
    self.passengers = passengers
  
  def get_info(self):
    print('license:' + self.license + ', driver:' + self.driver)
  